"""Five-year articulated Apple forecast and FCFF valuation. Standard library only.
All money and shares in millions; USD/share is their quotient.
"""
import copy, json, math
from pathlib import Path
ROOT=Path(__file__).resolve().parent
DATA=json.loads((ROOT/'data/inputs.json').read_text(encoding='utf-8'))
H=DATA['historical']; M=DATA['market']
ASSETS=('cash','securities_current','receivables','vendor_receivables','inventory','other_current_assets','securities_long','ppe','other_long_assets')
LIABS=('payables','other_current_liabilities','deferred_revenue','commercial_paper','debt_current','debt_long','other_long_liabilities')
WC_A=('receivables','vendor_receivables','inventory')
WC_L=('payables','deferred_revenue')
def near(a,b,label):
    if not math.isfinite(a) or not math.isfinite(b) or abs(a-b)>1e-5:
        raise ValueError(f'{label}: {a} versus {b}')
def wc(r): return sum(r[k] for k in WC_A)-sum(r[k] for k in WC_L)
def balance(r): return sum(r[k] for k in ASSETS)-sum(r[k] for k in LIABS)-r['equity']
def base_reconciliation():
    for year,h in H.items():
        near(balance(h),0,f'TTM{year} opening balance sheet')
        near(sum(h[k] for k in ASSETS),h['assets'],f'TTM{year} assets')
        near(sum(h[k] for k in LIABS),h['liabilities'],f'TTM{year} liabilities')
        near(h['opening_cash']+h['cfo']+h['cfi']+h['cff'],h['cash'],f'TTM{year} historical cash')
        near(h['pretax']-h['tax'],h['ni'],f'TTM{year} NI')
    h=H['2026'];near(h['products']+h['services'],h['revenue'],'TTM categories')
    near(sum(h[k] for k in ('iphone','mac','ipad','wearables')),h['products'],'TTM Products')
    near(h['products_gp']+h['services_gp']-h['rd']-h['sga'],h['ebit'],'TTM EBIT')
    # Reported product margin includes tariff-refund effects, not separately quantified.
    # 38% is a prudential normalized margin judgment, not a measured refund deduction.
    margin=.38;normalized_gp=h['products']*margin+h['services_gp']
    nebit=normalized_gp-h['rd']-h['sga'];ntax_rate=.18
    normalized=dict(reported_ebit=h['ebit'],reported_product_margin=h['products_gp']/h['products'],normalized_product_margin=margin,normalized_ebit=nebit,ebit_adjustment=nebit-h['ebit'],normalized_tax_rate=ntax_rate,normalized_nopat=nebit*(1-ntax_rate),delta_operating_nwc=wc(h)-wc(H['2025']),normalization_basis='Analyst margin reserve for tariff refunds and mix; amount of one-time refunds not identified. Tax normalized to 18%.')
    normalized['normalized_fcff']=normalized['normalized_nopat']+h['da']-h['capex']-normalized['delta_operating_nwc']-h['da']*(1-8000/11698)
    return normalized

h=H['2026']
BASE=dict(iphone_growth=[.10,.09,.08,.07,.06],mac_growth=[.07,.06,.05,.04,.03],ipad_growth=[.03]*5,wearables_growth=[.04]*5,services_growth=[.14,.13,.12,.11,.10],product_margin=.38,services_margin=h['services_gp']/h['services'],rd_ratio=.10,sga_ratio=h['sga']/h['revenue'],tax=.18,capex_ratio=.04,dep_ratio=(h['da']*8000/11698)/h['ppe'],other_amort_ratio=(h['da']*(1-8000/11698))/h['revenue'],sbc_ratio=h['sbc']/h['revenue'],inventory_days=h['inventory']/(h['products']-h['products_gp'])*365,wc_scale=1.,net_other=h['net_other'],dividends=h['dividends'],buybacks=h['buybacks'],cash_floor=30000.,terminal_growth=.025,terminal_roic=.30,rf=.0497,beta=1.075,erp=.045,kd=.06)
def wacc(a):
    eq=M['price']*M['basic_shares'];debt=sum(H['2026'][k] for k in ('commercial_paper','debt_current','debt_long'))
    ke=a['rf']+a['beta']*a['erp'];return (ke*eq+a['kd']*(1-a['tax'])*debt)/(eq+debt)
BASE['wacc']=wacc(BASE)
def assumptions(case='base'):
    a=copy.deepcopy(BASE)
    if case=='low':
        a.update(iphone_growth=[0,0,.01,.02,.02],mac_growth=[.01]*5,ipad_growth=[0]*5,wearables_growth=[0]*5,services_growth=[.06]*5,product_margin=.35,services_margin=.72,rd_ratio=.11,tax=.20,capex_ratio=.05,wc_scale=1.15,wacc=.115,terminal_growth=.02,terminal_roic=.20)
    elif case=='high':
        a.update(iphone_growth=[.18,.16,.14,.12,.10],mac_growth=[.10,.09,.08,.07,.06],ipad_growth=[.06]*5,wearables_growth=[.08]*5,services_growth=[.20,.18,.16,.14,.12],product_margin=.41,services_margin=.80,rd_ratio=.10,capex_ratio=.045,wacc=.085,terminal_growth=.03,terminal_roic=.40)
    elif case!='base':raise ValueError('Unknown case')
    return a

def validate_assumptions(a):
    for k,v in a.items():
        values=v if isinstance(v,list) else [v]
        if not all(isinstance(x,(int,float)) and math.isfinite(x) for x in values): raise ValueError(f'Nonfinite {k}')
    for k in ['iphone_growth','mac_growth','ipad_growth','wearables_growth','services_growth']:
        if len(a[k])!=5 or any(x<=-1 for x in a[k]): raise ValueError(f'Invalid five-year path {k}')
    for k in ['product_margin','services_margin','rd_ratio','sga_ratio','tax','capex_ratio','sbc_ratio','dep_ratio']:
        if not 0<=a[k]<1: raise ValueError(f'Invalid fraction {k}')
    if a['cash_floor']<0 or a['buybacks']<0 or a['dividends']<0 or a['wc_scale']<=0 or a['inventory_days']<0: raise ValueError('Invalid operating/funding input')
    if not 0<=a['terminal_growth']<a['wacc'] or a['terminal_roic']<=a['terminal_growth']: raise ValueError('Require 0 <= g < WACC and terminal ROIC > g')
def project(a):
    validate_assumptions(a); base_reconciliation(); p=copy.deepcopy(H['2026']); rows=[]
    for i in range(5):
        r={k:p[k] for k in ASSETS+LIABS+('equity',)}; r['year']=2027+i
        for k in ['iphone','mac','ipad','wearables','services']: r[k]=p[k]*(1+a[k+'_growth'][i])
        r['products']=sum(r[k] for k in ['iphone','mac','ipad','wearables']); r['revenue']=r['products']+r['services']
        r['products_gp']=r['products']*a['product_margin']; r['services_gp']=r['services']*a['services_margin']
        r['gross_profit']=r['products_gp']+r['services_gp']; r['cogs']=r['revenue']-r['gross_profit']
        r['rd']=r['revenue']*a['rd_ratio']; r['sga']=r['revenue']*a['sga_ratio']
        r['ebit']=r['gross_profit']-r['rd']-r['sga'] # D&A and SBC already in margins/opex.
        r['net_other']=a['net_other']; r['pretax']=r['ebit']+r['net_other']
        r['tax']=max(r['pretax'],0)*a['tax']; r['ni']=r['pretax']-r['tax']
        r['depreciation']=p['ppe']*a['dep_ratio']; r['other_amort']=r['revenue']*a['other_amort_ratio']; r['da']=r['depreciation']+r['other_amort']
        r['capex']=r['revenue']*a['capex_ratio']; r['other_reinvestment']=r['other_amort']
        r['ppe']=p['ppe']+r['capex']-r['depreciation']
        # Aggregate non-PP&E assets: amortization is offset by replacement expenditure.
        r['other_long_assets']=p['other_long_assets']+r['other_reinvestment']-r['other_amort']
        for k in WC_A+WC_L:
            if k=='inventory': r[k]=(r['products']-r['products_gp'])*a['inventory_days']/365
            else: r[k]=H['2026'][k]/H['2026']['revenue']*r['revenue']*(a['wc_scale'] if k in WC_A else 1.)
        r['delta_wc']=wc(r)-wc(p); r['sbc']=r['revenue']*a['sbc_ratio']
        r['cfo']=r['ni']+r['da']+r['sbc']-r['delta_wc']
        r['cfi']=-r['capex']-r['other_reinvestment']
        r['dividends']=min(a['dividends'],max(0,p['cash']+r['cfo']+r['cfi']-a['cash_floor']))
        r['buybacks']=min(a['buybacks'],max(0,p['cash']+r['cfo']+r['cfi']-r['dividends']-a['cash_floor']))
        r['cff']=-r['dividends']-r['buybacks'] # Debt maturities refinanced; no net borrowing.
        r['opening_cash']=p['cash']; r['cash']=p['cash']+r['cfo']+r['cfi']+r['cff']
        r['equity']=p['equity']+r['ni']+r['sbc']-r['dividends']-r['buybacks']
        r['nopat']=r['ebit']*(1-a['tax'])
        # SBC treated as an economic cost: its CFO addback is reversed in FCFF.
        r['fcff']=r['nopat']+r['da']-r['capex']-r['other_reinvestment']-r['delta_wc']
        r['fcff_from_cfo']=r['cfo']-r['sbc']-r['net_other']*(1-a['tax'])-r['capex']-r['other_reinvestment']
        r['assets']=sum(r[k] for k in ASSETS); r['liabilities']=sum(r[k] for k in LIABS)
        check_row(r,a); rows.append(r); p=r
    return rows
def check_row(r,a):
    if not all(math.isfinite(v) for v in r.values()): raise ValueError('Nonfinite forecast')
    near(balance(r),0,f"FY{r['year']} balance sheet")
    near(r['cash'],r['opening_cash']+r['cfo']+r['cfi']+r['cff'],'Forecast cash tie')
    near(r['fcff'],r['fcff_from_cfo'],'Operating FCFF versus cash-flow bridge')
    if r['cash']<a['cash_floor']-1e-5: raise ValueError('Cash-floor breach: funding assumption insufficient')
    if any(r[k]<-1e-5 for k in ASSETS+LIABS): raise ValueError('Negative asset or liability')
def dcf_path(path,k,g,cash,debt,shares,terminal_fcff=None):
    if len(path)!=5 or not all(math.isfinite(v) for v in path): raise ValueError('Five finite FCFF values required')
    if not all(math.isfinite(v) for v in (k,g,cash,debt,shares)) or k<=g or k<=0 or g<0 or shares<=0 or debt<0: raise ValueError('Invalid DCF boundary or bridge')
    terminal_fcff=path[-1]*(1+g) if terminal_fcff is None else terminal_fcff
    if not math.isfinite(terminal_fcff) or terminal_fcff<=0: raise ValueError('Nonpositive terminal FCFF: perpetuity unresolved')
    explicit=sum(v/(1+k)**i for i,v in enumerate(path,1)); tv=terminal_fcff/(k-g); pvt=tv/(1+k)**5
    ev=explicit+pvt; equity=ev+cash-debt
    near(equity-ev,cash-debt,'EV to equity bridge')
    return dict(fcff=path,pv_explicit=explicit,terminal_fcff=terminal_fcff,terminal_value=tv,pv_terminal=pvt,ev=ev,nonoperating_assets=cash,debt=debt,equity=equity,shares=shares,per_share=equity/shares,terminal_share=pvt/ev)
def value(rows,a):
    for r in rows: check_row(r,a)
    h=H['2026']; cash=h['cash']+h['securities_current']+h['securities_long']-a['cash_floor']
    debt=h['commercial_paper']+h['debt_current']+h['debt_long']
    # Terminal growth requires total reinvestment at an explicit incremental ROIC.
    nopat6=rows[-1]['nopat']*(1+a['terminal_growth'])
    term=nopat6*(1-a['terminal_growth']/a['terminal_roic'])
    result=dcf_path([r['fcff'] for r in rows],a['wacc'],a['terminal_growth'],cash,debt,M['valuation_shares'],term)
    result['terminal_nopat']=nopat6; result['terminal_reinvestment']=nopat6-term
    return result
def scenarios():
    out={}
    for case in ['low','base','high']:
        a=assumptions(case); rows=project(a); out[case]=dict(assumptions=a,statements=rows,valuation=value(rows,a))
    return out
def comps():
    h=H['2026']; rows=[]; bridge=h['cash']+h['securities_current']+h['securities_long']-sum(h[k] for k in ('commercial_paper','debt_current','debt_long'))
    for p in DATA['peers']:
        if p['ni']<=0 or p['ebit']<=0: raise ValueError('Nonmeaningful peer denominator')
        q=dict(p); q['market_cap']=p['price']*p['shares']; q['ev']=q['market_cap']+p['debt']-p['cash_and_securities']
        q['pe']=q['market_cap']/p['ni']; q['ev_ebit']=q['ev']/p['ebit']
        q['apple_pe_price']=q['pe']*h['ni']/M['valuation_shares']; q['apple_ev_ebit_price']=(q['ev_ebit']*h['ebit']+bridge)/M['valuation_shares']
        rows.append(q)
    # Trading EV includes all liquid assets consistently; operating-cash reserve is a DCF choice.
    return rows
def reverse_dcf(rows,a):
    target=M['price']; low,high=-.30,1.
    def calc(shift):
        path=[r['fcff']*(1+shift)**i for i,r in enumerate(rows,1)]
        terminal=rows[-1]['nopat']*(1+shift)**5*(1+a['terminal_growth'])*(1-a['terminal_growth']/a['terminal_roic'])
        h=H['2026']; return dcf_path(path,a['wacc'],a['terminal_growth'],h['cash']+h['securities_current']+h['securities_long']-a['cash_floor'],sum(h[k] for k in ('commercial_paper','debt_current','debt_long')),M['valuation_shares'],terminal)
    if not calc(low)['per_share']<=target<=calc(high)['per_share']: raise ValueError('Reverse-DCF target outside bracket')
    for _ in range(100):
        mid=(low+high)/2
        if calc(mid)['per_share']<target: low=mid
        else: high=mid
    shift=(low+high)/2; result=calc(shift); near(result['per_share'],target,'Reverse DCF target')
    result['annual_uplift_over_base']=shift; result['interpretation']='Uniform annual operating cash-flow/NOPAT uplift over base; not uniquely implied revenue growth.'
    return result
def sensitivity(rows,a):
    return [dict(wacc=k,g=g,value=value(rows,dict(a,wacc=k,terminal_growth=g))['per_share']) for k in [.08,.09,.10,.11,.12] for g in [.015,.02,.025,.03,.035]]
def whatifs():
    specs=[('Services regulation',dict(services_growth=[.04]*5,services_margin=.68)),('China / hardware replacement shock',dict(iphone_growth=[-.10,-.05,0,.02,.02],product_margin=.33)),('AI investment overrun',dict(rd_ratio=.13,capex_ratio=.06)),('Combined structural downside',dict(services_growth=[.03]*5,services_margin=.66,iphone_growth=[-.10,-.05,0,.01,.01],product_margin=.32,rd_ratio=.10,wacc=.115,terminal_growth=.015,terminal_roic=.15))]
    out=[]
    for name,change in specs:
        a=assumptions(); a.update(change); rows=project(a); out.append(dict(name=name,changes=change,valuation=value(rows,a),year5_ebit=rows[-1]['ebit'],year5_fcff=rows[-1]['fcff'],minimum_cash=min(r['cash'] for r in rows),buyback_curtailment=sum(BASE['buybacks']-r['buybacks'] for r in rows)))
    return out
def driver_tests():
    result=[]
    for name,key,lo,hi in [('Services growth','services_growth',.05,.15),('Products margin','product_margin',.35,.42),('R&D intensity','rd_ratio',.09,.12),('Capex intensity','capex_ratio',.03,.06),('WACC','wacc',.08,.12)]:
        vals=[]
        for v in [lo,hi]:
            a=assumptions(); a[key]=[v]*5 if key=='services_growth' else v; rows=project(a); vals.append(dict(input=v,ebit=rows[-1]['ebit'],fcff=rows[-1]['fcff'],per_share=value(rows,a)['per_share']))
        narrow=[]
        for v in [lo+(hi-lo)*.25,lo+(hi-lo)*.75]:
            a=assumptions(); a[key]=[v]*5 if key=='services_growth' else v; rows=project(a); narrow.append(value(rows,a)['per_share'])
        result.append(dict(driver=name,key=key,low=vals[0],high=vals[1],value_span=abs(vals[1]['per_share']-vals[0]['per_share']),half_range_span=abs(narrow[1]-narrow[0])))
    return result
def committee_action(cases,stresses,price):
    low=cases['low']['valuation']['per_share']; base=cases['base']['valuation']['per_share']; high=cases['high']['valuation']['per_share']
    # Explicit proposed rule for student review, not a fund's established mandate.
    if price<=.8*base and price<=low: return 'Initiate, conditional on thesis checks and human approval'
    return 'Watch / defer; no position'
def duration_challenge(cases):
    """Terminal-method challenge: extend a declining operating growth fade.

    The five-year statements stay fixed. Beyond year5, incremental ROIC funds
    growth, and annual FCFF/NOPAT are modeled inside terminal value at year5.
    This is a labeled terminal persistence judgment, not a second observed fact.
    """
    out=[]
    for case in ['base','high']:
        a=cases[case]['assumptions'];rows=cases[case]['statements'];g=a['terminal_growth'];k=a['wacc'];roic=a['terminal_roic']
        exit_growth=rows[-1]['nopat']/rows[-2]['nopat']-1
        for years in [0,5,10,15]:
            normal=cases[case]['valuation'];nopat=rows[-1]['nopat'];tv5=0.;flows=[]
            for step in range(1,years+1):
                growth=g+(max(g,exit_growth)-g)*(years-step+1)/(years+1)
                if growth>=roic:raise ValueError('Growth fade requires ROIC above growth')
                nopat*=1+growth;fcff=nopat*(1-growth/roic)
                tv5+=fcff/(1+k)**step;flows.append(dict(year=5+step,growth=growth,nopat=nopat,fcff=fcff))
            tail=nopat*(1+g)*(1-g/roic)/(k-g)
            tv5+=tail/(1+k)**years
            pvt=tv5/(1+k)**5;ev=normal['pv_explicit']+pvt;equity=ev+normal['nonoperating_assets']-normal['debt']
            out.append(dict(case=case,fade_years_after_year5=years,exit_nopat_growth=exit_growth,terminal_roic=roic,wacc=k,g=g,per_share=equity/normal['shares'],terminal_share=pvt/ev,terminal_cash_flow_path=flows,basis='Analyst-selected persistence/fade; not company guidance'))
    return out
def all_results():
    cases=scenarios(); stresses=whatifs(); rows=cases['base']['statements']; a=cases['base']['assumptions']
    return dict(as_of=DATA['cutoff'],units='USD millions; shares millions; prices USD/share',market=M,normalization=base_reconciliation(),cases=cases,comps=comps(),sensitivity=sensitivity(rows,a),reverse=reverse_dcf(rows,a),whatifs=stresses,drivers=driver_tests(),duration_challenge=duration_challenge(cases),action='Initiate - Alex Schwanke stated judgment; valuation support unresolved',model_action=committee_action(cases,stresses,M['price']),entry_review_price=min(.8*cases['base']['valuation']['per_share'],cases['low']['valuation']['per_share']))
if __name__=='__main__':
    out=all_results(); print(json.dumps({k:v['valuation']['per_share'] for k,v in out['cases'].items()},indent=2)); print(out['action'])
