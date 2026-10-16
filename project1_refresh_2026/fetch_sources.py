import urllib.request,json,datetime,hashlib,shutil
from pathlib import Path
R=Path(__file__).resolve().parent;raw=R/'data/raw';raw.mkdir(parents=True,exist_ok=True);manifest=[]
def fetch(name,url):
    req=urllib.request.Request(url,headers={'User-Agent':'University finance research contact analyst@example.com'})
    b=urllib.request.urlopen(req,timeout=40).read();(raw/name).write_bytes(b)
    manifest.append(dict(file=name,url=url,retrieved_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),sha256=hashlib.sha256(b).hexdigest()));print(name,len(b),flush=True)
for t,cik in [('AAPL',320193),('MSFT',789019),('GOOGL',1652044)]:fetch(t+'_companyfacts.json',f'https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010}.json')
start=int(datetime.datetime(2026,9,11,tzinfo=datetime.timezone.utc).timestamp());end=int(datetime.datetime(2026,9,16,tzinfo=datetime.timezone.utc).timestamp())
for t in ['AAPL','MSFT','GOOGL']:
    fetch(t+'_daily.json',f'https://query1.finance.yahoo.com/v8/finance/chart/{t}?period1={start}&period2={end}&interval=1d')
for t in ['AAPL','SPY']:
    start=int(datetime.datetime(2021,9,1,tzinfo=datetime.timezone.utc).timestamp());end=int(datetime.datetime(2026,9,1,tzinfo=datetime.timezone.utc).timestamp())
    fetch(t+'_monthly.json',f'https://query1.finance.yahoo.com/v8/finance/chart/{t}?period1={start}&period2={end}&interval=1mo')
fetch('treasury_sep2026.html','https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value=202609')
for name,url in [
('AAPL_Q3_2026.html','https://www.sec.gov/Archives/edgar/data/320193/000032019326000020/aapl-20260627.htm'),
('Siri_2026_release.html','https://www.apple.com/newsroom/2026/09/siri-ai-a-profoundly-more-capable-and-personal-assistant-is-here/')]:
    try:fetch(name,url)
    except Exception as e:print(name,type(e).__name__,str(e),flush=True)
(R/'data/source_manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
