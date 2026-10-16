"""AI-assisted technical demonstration; never the human AI-off locked record."""
import copy,datetime,hashlib,json
from pathlib import Path
import model
def run():
    a=model.assumptions();b=copy.deepcopy(a);b['iphone_growth']=[x+.02 for x in a['iphone_growth']]
    expectation='Before this technical execution: +2 percentage points to every annual iPhone growth input raises final EBIT, FCFF and value at fixed other independent inputs.'
    before_rows=model.project(a);after_rows=model.project(b)
    old,new=model.value(before_rows,a),model.value(after_rows,b)
    assert [k for k in a if a[k]!=b[k]]==['iphone_growth']
    assert new['per_share']>old['per_share'] and after_rows[-1]['ebit']>before_rows[-1]['ebit'] and after_rows[-1]['fcff']>before_rows[-1]['fcff']
    out=dict(author='Codex AI-assisted technical test',human_locked_requirement='NOT SATISFIED',run_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),valuation_date=model.DATA['cutoff'],input='iphone_growth',old=a['iphone_growth'],new=b['iphone_growth'],units='fractional annual growth, FY decision periods1-5; +0.02 means+2 percentage points',expectation=expectation,before=old,after=new,final_ebit_before=before_rows[-1]['ebit'],final_ebit_after=after_rows[-1]['ebit'],final_fcff_before=before_rows[-1]['fcff'],final_fcff_after=after_rows[-1]['fcff'],actual_direction='higher',before_model_rule_action='Watch/defer',after_model_rule_action='Watch/defer' if new['per_share']<model.M['price'] else 'Requires committee policy review',student_stated_action='Initiate; no new post-run human decision is claimed',diagnosis='Technical direction matches expectation. A higher value does not establish sufficient value versus market price, and no rule automatically overwrites the student judgment.',model_sha256=hashlib.sha256((model.ROOT/'model.py').read_bytes()).hexdigest(),inputs_sha256=hashlib.sha256((model.ROOT/'data/inputs.json').read_bytes()).hexdigest(),validation_history='The same direction was also tested in the unit suite; this is a preserved technical demonstration, not a first-ever human precommit')
    (model.ROOT/'docs/directional-test.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps({k:out[k] for k in ['author','human_locked_requirement','actual_direction','diagnosis']},indent=2));print('Before/after',old['per_share'],new['per_share'])
if __name__=='__main__':run()
