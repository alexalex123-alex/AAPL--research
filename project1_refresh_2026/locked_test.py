"""Student-only locked record utility. Use with AI closed, not through the assistant.
No expected direction or decision prediction is supplied by this script.
"""
import argparse, datetime, hashlib, json, math, subprocess
import model
P=model.ROOT/'docs/locked-precommit.json'
def git(*args):
    repo=model.ROOT.parent.resolve().as_posix()
    return subprocess.check_output(['git','-c',f'safe.directory={repo}','-C',repo,*args],text=True).strip()
def hashes():
    return {name:hashlib.sha256((model.ROOT/name).read_bytes()).hexdigest()
            for name in ('model.py','data/inputs.json','locked_test.py')}
def prepare():
    if P.exists(): raise SystemExit('Existing precommit preserved; do not overwrite.')
    confirm=input('Confirm this prediction is your own and AI is closed (type YES): ')
    if confirm!='YES': raise SystemExit('Cancelled')
    key=input('Material scalar input key: ').strip(); a=model.assumptions()
    if key not in a or isinstance(a[key],list): raise SystemExit('Choose a scalar input in model.BASE')
    new=float(input('New input value in model units: '))
    record=dict(material_input=key,old_value=a[key],new_value=new,units=input('Units: '),expected_output_direction=input('Your expected output direction and finance reasoning: '),expected_rough_size=input('Your rough expected size of effect and units: '),expected_decision_effect=input('Your expected committee decision effect and reasoning: '),human_author=input('Your name: '),ai_closed_declaration=True,precommit_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),protected_file_hashes=hashes())
    required=('units','expected_output_direction','expected_rough_size','expected_decision_effect','human_author')
    if not math.isfinite(new) or new==a[key] or any(not record[k].strip() for k in required): raise SystemExit('A finite material change and complete prediction are required')
    P.write_text(json.dumps(record,indent=2),encoding='utf-8')
    print('Prediction saved BEFORE execution. Review and git add/commit docs/locked-precommit.json yourself. Do not execute the change until committed.')
def run():
    dest=model.ROOT/'docs/locked-run.json'
    if dest.exists(): raise SystemExit('Existing locked run preserved; use review mode to add your diagnosis')
    if not P.exists(): raise SystemExit('Prepare your human prediction first')
    rel=f'{model.ROOT.name}/docs/locked-precommit.json'
    if git('status','--porcelain','--',rel): raise SystemExit('Precommit must be committed without pending edits')
    commit=git('log','-1','--format=%H','--',rel)
    if not commit: raise SystemExit('No precommit commit found')
    r=json.loads(P.read_text()); a=model.assumptions()
    if r.get('protected_file_hashes')!=hashes(): raise SystemExit('Model, inputs or helper changed after prediction: preserve the record and resolve before running')
    if git('status','--porcelain','--',f'{model.ROOT.name}/model.py',f'{model.ROOT.name}/data/inputs.json',f'{model.ROOT.name}/locked_test.py'): raise SystemExit('Commit the protected model/input/helper files before the locked run')
    if a[r['material_input']]!=r['old_value']: raise SystemExit('Old input no longer matches')
    b=dict(a); b[r['material_input']]=r['new_value']
    before=model.value(model.project(a),a); after=model.value(model.project(b),b)
    cases=model.scenarios(); stresses=model.whatifs()
    before_action=model.committee_action(cases,stresses,model.M['price'])
    cases['base']=dict(assumptions=b,statements=model.project(b),valuation=after)
    after_action=model.committee_action(cases,stresses,model.M['price'])
    out=dict(precommit=r,precommit_commit=commit,precommit_git_timestamp=git('show','-s','--format=%cI',commit),prediction_sha256=hashlib.sha256(P.read_bytes()).hexdigest(),run_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),before=before,after=after,actual_value_direction='higher' if after['per_share']>before['per_share'] else 'lower' if after['per_share']<before['per_share'] else 'unchanged',before_model_rule_action=before_action,after_model_rule_action=after_action,student_recorded_action='Initiate; Alex must personally diagnose whether this changes after the run',actual_decision_effect='changed' if before_action!=after_action else 'unchanged',human_reconciliation='PENDING: student must diagnose direction and decision effect after this AI-closed run')
    dest.write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
    print('Outputs preserved. While AI remains closed, run python locked_test.py review to record your diagnosis.')
def review():
    dest=model.ROOT/'docs/locked-run.json'
    if not dest.exists(): raise SystemExit('No preserved run exists')
    out=json.loads(dest.read_text())
    if out.get('review_completed_utc'): raise SystemExit('Review already preserved; add a dated addendum instead of overwriting')
    diagnosis=input('Your reconciliation to the prediction, failure diagnosis or reason the action did not change: ').strip()
    if not diagnosis: raise SystemExit('A substantive diagnosis is required')
    if input('Confirm this diagnosis was written with AI closed (YES): ')!='YES': raise SystemExit('Cancelled')
    out['human_reconciliation']=diagnosis; out['review_completed_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
    dest.write_text(json.dumps(out,indent=2)); print('Diagnosis appended; original prediction and execution results preserved. Commit both records.')
if __name__=='__main__':
    p=argparse.ArgumentParser(); p.add_argument('mode',choices=['prepare','run','review']); q=p.parse_args(); {'prepare':prepare,'run':run,'review':review}[q.mode]()
