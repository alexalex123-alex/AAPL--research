import json,datetime,statistics,re
from pathlib import Path
R=Path(__file__).resolve().parent;raw=R/'data/raw';cutoff='2026-09-14';ledger=[]
F={t:json.loads((raw/f'{t}_companyfacts.json').read_text(encoding='utf-8'))['facts'] for t in ['AAPL','MSFT','GOOGL']}
def fact(t,tag,end,start=None,unit='USD',ns='us-gaap'):
    records=[x for x in F[t][ns][tag]['units'][unit] if x['end']==end and x.get('start')==start and x['filed']<=cutoff]
    if not records:raise ValueError((t,tag,start,end))
    x=sorted(records,key=lambda x:x['filed'])[-1];v=x['val']/1e6 if unit in ('USD','shares') else x['val']
    ledger.append(dict(ticker=t,tag=tag,start=start,end=end,filed=x['filed'],accession=x['accn'],value=v,units='USD millions' if unit=='USD' else 'million shares' if unit=='shares' else unit))
    return v
def apple_ttm(tag,year=2026):
    if year==2026:periods=[('2025-09-27','2024-09-29',1),('2026-06-27','2025-09-28',1),('2025-06-28','2024-09-29',-1)]
    else:periods=[('2024-09-28','2023-10-01',1),('2025-06-28','2024-09-29',1),('2024-06-29','2023-10-01',-1)]
    return sum(sign*fact('AAPL',tag,end,start) for end,start,sign in periods)
bs_tags=dict(cash='CashAndCashEquivalentsAtCarryingValue',securities_current='MarketableSecuritiesCurrent',receivables='AccountsReceivableNetCurrent',vendor_receivables='NontradeReceivablesCurrent',inventory='InventoryNet',other_current_assets='OtherAssetsCurrent',securities_long='MarketableSecuritiesNoncurrent',ppe='PropertyPlantAndEquipmentNet',other_long_assets='OtherAssetsNoncurrent',payables='AccountsPayableCurrent',other_current_liabilities='OtherLiabilitiesCurrent',deferred_revenue='ContractWithCustomerLiabilityCurrent',commercial_paper='CommercialPaper',debt_current='LongTermDebtCurrent',debt_long='LongTermDebtNoncurrent',other_long_liabilities='OtherLiabilitiesNoncurrent',equity='StockholdersEquity',assets='Assets',liabilities='Liabilities')
flow_tags=dict(revenue='RevenueFromContractWithCustomerExcludingAssessedTax',ebit='OperatingIncomeLoss',ni='NetIncomeLoss',pretax='IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest',tax='IncomeTaxExpenseBenefit',da='DepreciationDepletionAndAmortization',capex='PaymentsToAcquirePropertyPlantAndEquipment',cfo='NetCashProvidedByUsedInOperatingActivities',cfi='NetCashProvidedByUsedInInvestingActivities',cff='NetCashProvidedByUsedInFinancingActivities',sbc='ShareBasedCompensation',rd='ResearchAndDevelopmentExpense',sga='SellingGeneralAndAdministrativeExpense',dividends='PaymentsOfDividends',buybacks='PaymentsForRepurchaseOfCommonStock')
hist={}
for year,end,opening in [(2025,'2025-06-28','2024-06-29'),(2026,'2026-06-27','2025-06-28')]:
    h={k:fact('AAPL',tag,end) for k,tag in bs_tags.items()}
    for k,tag in flow_tags.items():h[k]=apple_ttm(tag,year)
    h['opening_cash']=fact('AAPL','CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents',opening)
    h['net_other']=h['pretax']-h['ebit'];hist[str(year)]=h
# Q3 2026 separately presents intangible assets of 20,342 on balance-sheet p.3.
# Aggregate with other noncurrent assets for compatibility with the historical schedule.
# The generic SEC intangible tag differs; prefer the published balance-sheet line and flag it.
hist['2026']['intangible_assets_disclosed']=20342.
hist['2026']['other_long_assets_reported']=hist['2026']['other_long_assets']
hist['2026']['other_long_assets']+=20342.
# Dimensional figures: FY2025 plus 9m2026 minus 9m2025, from the current 10-Q.
old=dict(iphone=209586,mac=33708,ipad=28023,wearables=35686,services=109158,products=307003,products_gp=112887,services_gp=82314) # FY2025 10-K category disclosures
category_ytd=dict(iphone=(196515,160561),mac=(27137,24982),ipad=(21700,21071),wearables=(27277,26673),services=(91728,80408),products=(272629,233287),products_gp=(108819,86190),services_gp=(69963,60670))
for key,(current,prior) in category_ytd.items():hist['2026'][key]=old[key]+current-prior
market=dict(date=cutoff)
def price(t):
    d=json.loads((raw/f'{t}_daily.json').read_text())['chart']['result'][0]
    pairs=[(datetime.datetime.fromtimestamp(ts,datetime.timezone.utc).strftime('%Y-%m-%d'),v) for ts,v in zip(d['timestamp'],d['indicators']['quote'][0]['close'])]
    return round(next(v for date,v in pairs if date==cutoff),2)
market['price']=price('AAPL');market['basic_shares']=fact('AAPL','EntityCommonStockSharesOutstanding','2026-07-17',unit='shares',ns='dei')
def shares_ttm(tag):return fact('AAPL',tag,'2025-09-27','2024-09-29','shares')+fact('AAPL',tag,'2026-06-27','2025-09-28','shares')*.75-fact('AAPL',tag,'2025-06-28','2024-09-29','shares')*.75
market['annual_diluted']=shares_ttm('WeightedAverageNumberOfDilutedSharesOutstanding');market['annual_basic']=shares_ttm('WeightedAverageNumberOfSharesOutstandingBasic')
market['dilution_reserve']=market['annual_diluted']-market['annual_basic'];market['valuation_shares']=market['basic_shares']+market['dilution_reserve']
series={}
for t in ['AAPL','SPY']:
    d=json.loads((raw/f'{t}_monthly.json').read_text())['chart']['result'][0]
    series[t]={datetime.datetime.fromtimestamp(ts,datetime.timezone.utc).strftime('%Y-%m'):v for ts,v in zip(d['timestamp'],d['indicators']['adjclose'][0]['adjclose']) if v and datetime.datetime.fromtimestamp(ts,datetime.timezone.utc).strftime('%Y-%m')<'2026-09'}
months=sorted(set(series['AAPL'])&set(series['SPY']));ret={t:[series[t][months[i]]/series[t][months[i-1]]-1 for i in range(1,len(months))] for t in series}
x,y=ret['SPY'],ret['AAPL'];mx,my=statistics.mean(x),statistics.mean(y)
beta=sum((a-mx)*(b-my) for a,b in zip(x,y))/sum((a-mx)**2 for a in x)
market['beta_diagnostic']=dict(value=beta,observations=len(x),first_month=months[0],last_month=months[-1],method='OLS monthly adjusted returns versus SPY; complete months only; retrieved snapshot, not vendor point-in-time beta')
peers=[]
for t in ['MSFT','GOOGL']:
    end='2026-06-30';cash=fact(t,'CashAndCashEquivalentsAtCarryingValue',end)
    sec=fact(t,'ShortTermInvestments' if t=='MSFT' else 'MarketableSecuritiesCurrent',end)
    debt=fact(t,'LongTermDebtCurrent',end)+fact(t,'LongTermDebtNoncurrent',end)
    if t=='GOOGL':debt+=fact(t,'CommercialPaper',end)
    if t=='MSFT':
        shrecords=[a for a in F[t]['dei']['EntityCommonStockSharesOutstanding']['units']['shares'] if a['filed']<=cutoff]
        sr=sorted(shrecords,key=lambda a:a['end'])[-1];shares=fact(t,'EntityCommonStockSharesOutstanding',sr['end'],unit='shares',ns='dei')
        ni=fact(t,'NetIncomeLoss',end,'2025-07-01');ebit=fact(t,'OperatingIncomeLoss',end,'2025-07-01')
    else:
        shares=fact(t,'CommonStockSharesOutstanding',end,unit='shares')
        def ttm(tag):return fact(t,tag,'2025-12-31','2025-01-01')+fact(t,tag,end,'2026-01-01')-fact(t,tag,'2025-06-30','2025-01-01')
        ni=ttm('NetIncomeLoss');ebit=ttm('OperatingIncomeLoss')
    peers.append(dict(ticker=t,price=price(t),shares=shares,cash_and_securities=cash+sec,debt=debt,ni=ni,ebit=ebit,earnings_end=end,price_date=cutoff,qualification='Cloud/enterprise mix and AI capex' if t=='MSFT' else 'Advertising, investment gains and aggregate-class price proxy'))
data=dict(cutoff=cutoff,base_label='TTM ended June 27, 2026; available July 31, 2026',forecast_convention='Five 12-month decision periods ending September 14, 2027-2031; latest published June opening balances are proxies, not September actuals',historical=hist,market=market,peers=peers)
(R/'data/inputs.json').write_text(json.dumps(data,indent=2),encoding='utf-8');(R/'data/fact_ledger.json').write_text(json.dumps(ledger,indent=2),encoding='utf-8')
print(json.dumps(dict(market=market,base=hist['2026'],peers=peers),indent=2))
