import copy,hashlib,json,unittest
import model as m
class RefreshedTests(unittest.TestCase):
    def test_training_answer(self):
        cf=100;path=[]
        for g in [.08,.06,.05,.04,.03]:cf*=1+g;path.append(cf)
        r=m.dcf_path(path,.1,.03,50,300,50)
        expected=[108,114.48,120.204,125.0122,128.7625,448.4408,1894.6486,1176.4277,1624.8685,1374.8685,27.4974,.7240]
        actual=path+[r[k] for k in ['pv_explicit','terminal_value','pv_terminal','ev','equity','per_share','terminal_share']]
        for x,y in zip(actual,expected):self.assertAlmostEqual(x,y,delta=.0001)
    def test_source_cutoff_and_hashes(self):
        self.assertEqual(m.DATA['cutoff'],'2026-09-14')
        for row in json.loads((m.ROOT/'data/fact_ledger.json').read_text()):self.assertLessEqual(row['filed'],m.DATA['cutoff'])
        for row in json.loads((m.ROOT/'data/source_manifest.json').read_text()):self.assertEqual(hashlib.sha256((m.ROOT/'data/raw'/row['file']).read_bytes()).hexdigest(),row['sha256'])
    def test_historical_independent_filing(self):
        h=m.H['2026'];self.assertEqual(h['assets'],383266);self.assertEqual(h['intangible_assets_disclosed'],20342)
        self.assertEqual(h['other_long_assets'],77557+20342)
        self.assertEqual(h['revenue'],416161+364357-313695)
        self.assertEqual(h['ebit'],133050+122432-100623)
        self.assertEqual(m.M['price'],333.08);m.base_reconciliation()
    def test_normalization(self):
        n=m.base_reconciliation();self.assertLess(n['normalized_ebit'],n['reported_ebit'])
        self.assertEqual(n['normalized_product_margin'],.38)
        self.assertNotIn('other_current_liabilities',m.WC_L)
    def test_articulation_all_cases(self):
        for case in ['low','base','high']:
            a=m.assumptions(case);rows=m.project(a);self.assertEqual(len(rows),5)
            self.assertEqual([r['year'] for r in rows],list(range(2027,2032)))
            for r in rows:m.check_row(r,a)
        self.assertEqual(len(m.whatifs()),4)
    def test_fail_loudly(self):
        a=m.assumptions();r=m.project(a)[0];r['cash']+=1000
        with self.assertRaises(ValueError):m.check_row(r,a)
        r=m.project(a)[0];r['fcff']-=1000
        with self.assertRaises(ValueError):m.check_row(r,a)
    def test_boundaries_and_negative_explicit(self):
        for k,g,sh in [(.03,.03,50),(.02,.03,50),(.1,.03,0),(.1,float('nan'),50)]:
            with self.assertRaises(ValueError):m.dcf_path([100]*5,k,g,50,300,sh)
        self.assertLess(m.dcf_path([-100,100,100,100,100],.1,.03,50,300,50)['ev'],m.dcf_path([0,100,100,100,100],.1,.03,50,300,50)['ev'])
    def test_monotonicity(self):
        a=m.assumptions();rows=m.project(a)
        vs=[m.value(rows,dict(a,wacc=k))['per_share'] for k in [.08,.09,.10,.11,.12]]
        self.assertTrue(all(x>y for x,y in zip(vs,vs[1:])))
        vs=[m.value(rows,dict(a,terminal_growth=g))['per_share'] for g in [.015,.02,.025,.03,.035]]
        self.assertTrue(all(x<y for x,y in zip(vs,vs[1:])))
    def test_bridge(self):
        a=m.assumptions();v=m.value(m.project(a),a)
        self.assertEqual(v['nonoperating_assets'],39544+22855+84118-30000)
        self.assertEqual(v['debt'],1997+11007+71340)
        self.assertAlmostEqual(v['equity'],v['ev']+v['nonoperating_assets']-v['debt'])
    def test_peers_and_reverse(self):
        for p in m.comps():
            self.assertEqual(p['price_date'],'2026-09-14')
            self.assertAlmostEqual(p['ev'],p['market_cap']+p['debt']-p['cash_and_securities'])
            self.assertAlmostEqual(p['pe'],p['market_cap']/p['ni'])
        a=m.assumptions();self.assertAlmostEqual(m.reverse_dcf(m.project(a),a)['per_share'],333.08)
    def test_operating_direction_before_run_expectation(self):
        # AI-assisted expectation written before execution: faster iPhone growth
        # raises EBIT and economic FCFF at fixed margins/cost/reinvestment ratios.
        a=m.assumptions();b=copy.deepcopy(a);b['iphone_growth']=[g+.02 for g in a['iphone_growth']]
        old,new=m.project(a),m.project(b)
        self.assertGreater(new[-1]['ebit'],old[-1]['ebit']);self.assertGreater(new[-1]['fcff'],old[-1]['fcff'])
        self.assertGreater(m.value(new,b)['per_share'],m.value(old,a)['per_share'])
    def test_judgment_and_output_are_separate(self):
        r=m.all_results();self.assertTrue(r['action'].startswith('Initiate'))
        self.assertTrue(r['model_action'].startswith('Watch'))
        self.assertLess(r['cases']['high']['valuation']['per_share'],r['market']['price'])
    def test_growth_duration_terminal_reconciliation(self):
        cases=m.scenarios();rows=m.duration_challenge(cases)
        for case in ['base','high']:
            r=[x for x in rows if x['case']==case]
            self.assertAlmostEqual(r[0]['per_share'],cases[case]['valuation']['per_share'])
            self.assertTrue(all(x['per_share']<y['per_share'] for x,y in zip(r,r[1:])))
            for x in r:
                for flow in x['terminal_cash_flow_path']:
                    self.assertLess(flow['growth'],x['terminal_roic'])
                    self.assertAlmostEqual(flow['fcff'],flow['nopat']*(1-flow['growth']/x['terminal_roic']))
if __name__=='__main__':unittest.main(verbosity=2)
