"""Build visible output, or serve the local interactive application."""
import argparse, csv, json, sys, datetime
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
import model
def build():
    result=model.all_results(); out=model.ROOT/'visible_output'; out.mkdir(exist_ok=True)
    (out/'results.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    html=(model.ROOT/'dashboard.html').read_text(encoding='utf-8').replace('__RESULTS__',json.dumps(result).replace('</','<\\/'))
    (out/'index.html').write_text(html,encoding='utf-8')
    for case,v in result['cases'].items():
        with (out/f'{case}_statements.csv').open('w',newline='',encoding='utf-8') as f:
            w=csv.DictWriter(f,fieldnames=v['statements'][0].keys()); w.writeheader(); w.writerows(v['statements'])
    print('Visible output:',out/'index.html')
    for case,v in result['cases'].items(): print(f"{case}: ${v['valuation']['per_share']:.2f}; TV share {v['valuation']['terminal_share']:.1%}")
    print('Proposed committee action:',result['action']); return result
class Handler(SimpleHTTPRequestHandler):
    def __init__(self,*args,**kwargs): super().__init__(*args,directory=str(model.ROOT/'visible_output'),**kwargs)
    def do_POST(self):
        if self.path!='/api/scenario': self.send_error(404); return
        try:
            if int(self.headers.get('Content-Length',0))>10000: raise ValueError('Request too large')
            q=json.loads(self.rfile.read(int(self.headers['Content-Length']))); a=model.assumptions(q.get('case','base'))
            allowed={'wacc','terminal_growth','services_growth','product_margin','rd_ratio','capex_ratio'}
            for k,v in q.get('changes',{}).items():
                if k not in allowed: raise ValueError('Unsupported driver')
                a[k]=[float(v)]*5 if k=='services_growth' else float(v)
            rows=model.project(a); result=dict(assumptions=a,statements=rows,valuation=model.value(rows,a)); self.send_response(200)
        except (ValueError,KeyError,TypeError) as e:
            result=dict(error=str(e)); self.send_response(400)
        payload=json.dumps(result).encode(); self.send_header('Content-Type','application/json'); self.send_header('Content-Length',str(len(payload))); self.end_headers(); self.wfile.write(payload)
def main():
    parser=argparse.ArgumentParser(); parser.add_argument('--serve',action='store_true'); parser.add_argument('--port',type=int,default=8765); args=parser.parse_args(); build()
    if args.serve:
        print(f'Open http://127.0.0.1:{args.port} - Ctrl+C to stop',flush=True)
        ThreadingHTTPServer(('127.0.0.1',args.port),Handler).serve_forever()
if __name__=='__main__': main()
