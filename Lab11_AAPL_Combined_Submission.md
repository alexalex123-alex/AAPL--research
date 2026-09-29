# Lab 11 — Apple Services Growth and Stability: Combined Submission

This single file contains the written checkout, both complete Python source files, and the captured results and accounting checks. Upload this Markdown file to GitHub and use its file link for the checkout.

**Outstanding requirements:** The independent locked prediction and actual Lab 11 partner notes remain incomplete. Cost of equity is a valuation driver, while the worksheet asks for two operating drivers; that mismatch still needs to be resolved. Combining the files does not complete those requirements.

To run the embedded code, save each Python block under the filename shown above it in the same folder, then run:

```bash
python apple_services_sensitivity.py --services-low 5 --services-base 10 --services-high 15
```

---

## Written checkout and analysis

## Lab 11 — Apple Services growth and perceived stability

**Current version: replaces the iPhone-margin test.** The operating driver is Services revenue growth, with its higher gross margin flowing through the revenue mix. The other requested driver is perceived stability, represented by cost of equity. No iPhone-specific margin is assumed or varied.

### Completion status

The requested scenario analysis, signed differences, spans, visible statements, checks, reproducible code and explanatory notes are complete. Three course requirements remain distinct: **cost of equity is not the required second operating driver; no independent pre-run student prediction was supplied; and actual Lab 11 partner notes were not supplied.** No claim is made that these requirements have been completed.

### D — driver question

How much do faster growth in Apple's high-margin Services business and changes in investors' required return affect forecast profit, FCFE and value per share, over the selected ranges?

### Article: what informs the model?

The [September 28, 2026 opinion article by Gian Estrada](https://finance.yahoo.com/markets/stocks/articles/opinion-apple-gangster-move-boost-155254919.html) argues that a larger Services mix supports profitability and that more predictable customer relationships can support valuation. It also cautions that an iPhone lease arranged through Klarna does not necessarily change how Apple recognizes its own revenue. These are separate operating and valuation ideas; the model tests them separately rather than assuming a financing plan automatically becomes Services revenue or automatically earns a valuation premium.

The article's quoted margins and market multiples are not adopted as forecast facts. Category revenue and gross profit are anchored in Apple's 10-K; the growth ranges and required returns below are judgments selected by the user. This is a test of the article's economic mechanism, not an endorsement or a reproduction of its market-multiple valuation.

### R — reported anchors and labeled assumptions

All financial amounts are USD millions unless indicated. [Apple FY2025 10-K, income statement p. 29 and MD&A pp. 23–24](https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm).

| Value | Label | Reason |
|---|---|---|
| FY2025 Services revenue **109,158**, gross profit **82,314** | History | Reported category amounts establish the starting Services business. |
| FY2025 Products revenue **307,003**, gross profit **112,887** | History | Reported category amounts establish the remaining product business; Products includes all hardware categories, not just iPhone. |
| Services gross margin **82,314 / 109,158 = approximately 75.41%**, held constant | Judgment | Hold the reported starting profitability constant so the test isolates growth rather than an additional margin improvement. |
| Products gross margin **112,887 / 307,003 = approximately 36.77%**, held constant | Judgment | Keep product profitability fixed so only Services growth changes in the operating tests. |
| Services annual revenue growth: **5% / 10% base / 15%** in FY2026–FY2030 | Judgment, user-selected | A slower-growth, central and stronger-growth comparison. The article does not supply this forecast range; it is not management guidance or a confidence interval. |
| Products annual revenue growth: **5% in every year**, unchanged across scenarios | Judgment | Retain the original model's 5% growth assumption for Products; all variation in the operating comparison comes from Services. |
| Cost of equity: **8% / 10% base / 12%** | Judgment, user-selected | Compare lower required return with a lasting perceived-stability shock that raises required return. This is a sensitivity range, not an estimated CAPM result. |
| Consolidated revenue and gross margin: **calculated from the two categories** | Judgment about model structure | Do not hold consolidated margin fixed when a higher-margin business changes its share of sales. |
| Inventory: **Products cost of sales × (5,718 / 194,116)** | Judgment using history | Inventory follows product costs; Services growth alone should not create physical product inventory. The calibrated inventory-days ratio is 5,718 / 194,116 × 365. |
| Other working-capital accounts: original FY2025 ratios to **total revenue** | Judgment | Preserve the remaining Lab 10 account rules for comparability. This aggregate treatment may overstate working-capital financing benefits from Services and needs refinement before a stronger economic conclusion. |
| SG&A / gross profit **14.1%**; R&D / revenue **8.3%**; tax **16%** | Judgment, retained | Preserve the saved expense and tax assumptions; linked dollar expenses and taxes recalculate with category growth. |
| Capex **12,715**; PP&E depreciation ratio **8,000 / 49,834**; other D&A **3,698** | Judgment / historical calibration, retained | Preserve the original reinvestment and D&A schedule rather than mix a capital-spending shock into the growth test. Maintaining fixed capex at higher Services growth is a limitation to investigate. |
| Net other expense **321**; term-debt repayment **10,932**; dividends **15,421**; target buybacks **90,711**; cash floor **25,000** | Judgment, retained | Preserve the original nonoperating, financing and liquidity assumptions. Buybacks adjust downward if required by the cash floor. |
| Terminal growth **2.5%**; share denominator **14,773.260 million** | Judgment / history, retained | Keep valuation comparisons on the same long-run growth and FY2025 share count. Services does not grow at 10% or 15% forever: the normalized total-company terminal cash flow grows at 2.5%. |

All remaining opening balances and account treatments are inherited from Lab 10: securities, deferred-tax assets, tax payable, commercial paper and other long-term liabilities stay flat; other non-tax long-term assets decline with the other-D&A residual; no separate stock-compensation addback is taken. No forward company guidance is claimed for these policies.

The Services range is ±5 **percentage points** around 10%, not ±5% relative. The cost-of-equity range is ±2 percentage points around 10%. Services growth is applied annually through FY2030; the cost of equity applies to the discount factors and terminal capitalization.

### Important: a revised base, not an unexplained change to Lab 10

The saved Lab 10 model used 5% total revenue growth and 46.9% fixed gross margin, producing **$112.54** per share. This extension separates Products and Services, uses exact reported category margins, and assigns **10% Services growth versus 5% Products growth** in the new base. Its base is therefore **$125.52**, not $112.54.

The 5%-Services scenario, where both businesses grow at 5%, gives **$112.56**, close to the old result. The small remaining difference comes from exact reported margins instead of the rounded 46.9% and the inventory calibration to product costs. Do not compare one scenario's change against the old base: all differences below use the new segmented base. The original Lab 10 file is unchanged.

### I / V — one-input-at-a-time sensitivity table

Outputs are FY2030 operating profit and **FCFE**, in USD millions; value is USD per share. Each run starts with a fresh copy of the same new base. Category margins are fixed in every run.

| Scenario | Services growth | Cost of equity | Operating profit | FCFE | Value/share |
|---|---:|---:|---:|---:|---:|
| Base | 10% | 10% | 190,523.8 | 153,571.7 | $125.52 |
| More stable: cost of equity 8% | 10% | 8% | 190,523.8 | 153,571.7 | $173.08 |
| Stability shock: cost of equity 12% | 10% | 12% | 190,523.8 | 153,571.7 | $98.07 |
| Services growth 5% | 5% | 10% | 169,919.4 | 135,259.0 | $112.56 |
| Services growth 15% | 15% | 10% | 215,235.1 | 175,689.9 | $141.00 |

#### Revenue mix explains the operating effect

| Services annual growth | FY2030 Services revenue, $m | Services share of total revenue | Consolidated gross margin |
|---|---:|---:|---:|
| 5% | 139,316.3 | 26.23% | 46.91% |
| 10% | 175,800.1 | 30.97% | 48.74% |
| 15% | 219,555.7 | 35.91% | 50.65% |

The high margin itself is not the varied driver. Services' **growth rate** changes, increasing or decreasing its mix share while each category's margin stays fixed. That is the mechanism requested from the article.

#### Signed changes from the new base

| Scenario | Operating-profit change, $m | FCFE change, $m | Value/share change |
|---|---:|---:|---:|
| More stable: cost of equity 8% | +0.0 | +0.0 | $+47.56 |
| Stability shock: cost of equity 12% | +0.0 | +0.0 | $-27.45 |
| Services growth 5% | -20,604.4 | -18,312.7 | $-12.97 |
| Services growth 15% | +24,711.3 | +22,118.2 | $+15.48 |

Example using displayed results: **175,689.9 − 153,571.7 = +22,118.2 million** of final-year FCFE in the 15% Services case. The code uses full precision before rounding. This is a worked check to reproduce personally, not a claim of a completed student or partner check.

#### Visible accounting and restored-base checks

| Scenario | FY2026 gap | FY2027 gap | FY2028 gap | FY2029 gap | FY2030 gap | Lowest cash, $m |
|---|---:|---:|---:|---:|---:|---:|
| Base | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 40,136.9 |
| More stable: cost of equity 8% | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 40,136.9 |
| Stability shock: cost of equity 12% | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 40,136.9 |
| Services growth 5% | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 36,960.9 |
| Services growth 15% | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 43,312.9 |

All 25 forecast-year checks pass; cash exceeds the 25,000 floor and FCFE stays positive. No revolver or buyback reduction is needed in these runs. The script checks that only the chosen independent input changes, verifies the Services earnings bridge, confirms product inventory is unchanged across Services-only runs, and reruns the new base at the end. The full restored-base statements and value match exactly. Accounting tolerance is 0.000001 million.

If a future run fails accounting, it is flagged invalid and not used for a complete ranking. Negative explicit cash flows retain their signs; nonpositive terminal cash flow or an invalid discount-rate/growth relationship makes valuation unavailable rather than forcing a terminal value.

### E — which driver matters over these ranges?

| Driver | Operating-profit span, $m | FCFE span, $m | Value/share span |
|---|---:|---:|---:|
| Stability | 0.0 | 0.0 | $75.01 |
| Services growth | 45,315.7 | 40,430.9 | $28.44 |

**Over these ranges, Services growth drives operating profit and cash flow, while the stability/required-return test produces the larger per-share valuation span.** The required-return span is approximately 75.01 per share versus 28.44 for Services growth. This is conditional on the chosen range widths and the model, not an inherent ranking or a probability statement.

#### Trace the links

1. Services revenue compounds from 109,158 at the selected rate. Products revenue grows at a fixed 5% from 307,003.
2. Each category's revenue is multiplied by its own fixed gross margin. Faster Services growth both increases total revenue and increases the weight of the more profitable category.
3. SG&A rises with gross profit and R&D rises with total revenue. The incremental Services operating-profit formula is `change in Services revenue × [Services margin × (1 − SG&A/GP) − R&D/revenue]`. The script independently verifies this link.
4. Taxes, net income and total-revenue-linked working-capital accounts recalculate. Product inventory is unchanged because Products costs are unchanged. Under the inherited negative working-capital structure, faster growth also produces extra working-capital financing; that is a model assumption to scrutinize, not a discovered Services-specific fact.
5. FCFE rises, then explicit cash flows and the normalized terminal cash flow are discounted. The separate stability cases change only cost of equity; identical statements produce different present values.

Do not simultaneously lower the discount rate in the faster-Services case: that would combine two independent changes. Neither a revenue multiple nor an automatic recurring-revenue premium is added on top of the FCFE valuation. A real stability shock might also damage sales or margins, but this test isolates required return.

### Learn-on-your-own answers and reflection prompts

**One-at-a-time sensitivity:** Change one independent driver while resetting all others to base and recalculating dependent revenue, margins, expenses, cash flows and balance-sheet accounts.

**Why ranges matter:** Spans reflect both the economic relationships and the size of the selected shocks. Testing wider Services growth or narrower cost of equity could change the ranking.

**Why these are not probabilities:** The three inputs are selected scenarios with no likelihood weights. The table does not prove the endpoints are likely or that the market must adopt the model's value.

**Research priority:** Validate the persistence of Services growth, its mix and gross-margin economics, and the reinvestment and working-capital needs associated with scaling it. Separately support the required-return range rather than equating recurring revenue with guaranteed stability. Historical source anchors are traceable; future growth and risk remain judgments.

**Reflection to write personally:** Which result surprised you—the effect of Services mix on consolidated margin, or the size of the discount-rate effect despite unchanged operating results? Use the numbers above and your own reaction; no personal reaction is invented here.

### Locked prediction and partner evidence — not supplied

The user selected 5%/10%/15% Services growth before these runs. That selection is not itself the course's Locked Changed-Input Record: no student-authored prediction made with AI closed, timestamp, rough expected output change or pre-run partner unit check was provided. No timestamp is backdated.

| Required record | Status |
|---|---|
| Pre-run timestamp / Git commit, old → new input and units | Not supplied |
| Expected direction, rough size and reason | Not supplied |
| Partner's pre-run unit and one-input check | Not confirmed |
| Actual result | Available in the tables |
| Prediction error and explanation | Cannot evaluate without the genuine prior prediction |
| Student's change or no-change conclusion / research priority | To be written personally |
| Actual partner question, response and check on their model | Not supplied for Lab 11 |

These Services outputs have now been observed. To satisfy the locked-record requirement, choose a fresh untested input change, close AI and write the prediction before running it. The earlier Lab 10 growth discussion is not reused as a Lab 11 Services review.

Suggested review questions, not an invented exchange: “Does Services need additional capex or different working-capital ratios to sustain this growth?” and “What supports 8%–12% cost of equity?” Have the reviewer recompute the 15%-Services FCFE difference and check that required return stayed at 10%.

### Fit to the lab and submission

Lab 11 asks for **two operating drivers already in the model**. This extension introduces one operating driver (Services growth) and retains the user's requested valuation driver (cost of equity). It provides the requested analysis, but to meet the literal operating-driver requirement, select and test a second operating driver or obtain instructor acceptance of the substitution. No instructor acceptance is claimed.

The bundle includes the segmented engine, sensitivity runner, full scenario statements as JSON, visible output with new-base statements, and this report. No slide deck is required by the supplied Lab 11 worksheet. No GitHub upload is claimed.

```bash
python apple_services_sensitivity.py --services-low 5 --services-base 10 --services-high 15
```

Keep the runner beside `apple_services_proforma.py`. The new base resets and restores within this analysis; the original Lab 10 files remain separate and unchanged. The old September 24 market quote is not used as a current quote in this report.

---

## Sensitivity analysis — apple_services_sensitivity.py

````python
"""Run Services growth and cost-of-equity sensitivities.
python apple_services_sensitivity.py --services-low 5 --services-base 10 --services-high 15
Rates on command line are percentages. Keep beside apple_services_proforma.py.
"""
import argparse
import copy
import json
from pathlib import Path
import apple_services_proforma as model


def run_case(name,inputs):
    a=copy.deepcopy(inputs)
    result=dict(name=name,inputs=a,status='valid')
    try:
        rows=model.project(a)
        model.assert_balanced(rows,a)
    except ValueError as e:
        result.update(status='invalid',reason=str(e),per_share=None)
        return result
    last=rows[-1]
    result.update(rows=rows,operating_income=last['operating_income'],fcfe=last['fcfe'],
        services_revenue=last['services_revenue'],services_share=last['services_share'],
        gross_margin=last['gross_margin'],per_share=None)
    try:
        result['valuation']=model.valuation(rows,a)
        result['per_share']=result['valuation']['per_share']
    except ValueError as e:
        result['valuation_reason']=str(e)
    result['checks']=[dict(year=r['year'],gap=model.gap(r),cash=r['cash'],
        cash_floor=a['cash_floor'],cash_ok=r['cash']>=a['cash_floor']-1e-6) for r in rows]
    return result


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for arg in ('services-low','services-base','services-high'):
        p.add_argument('--'+arg,type=float,required=True)
    args=p.parse_args()
    if not -100<args.services_low<args.services_base<args.services_high:
        p.error('Services rates must be ordered lower < base < higher, all above -100%')
    original=copy.deepcopy(model.A)
    base_inputs=dict(model.A,services_growth=args.services_base/100)
    cases=[run_case('Base',base_inputs),
        run_case('More stable: cost of equity 8%',dict(base_inputs,ke=.08)),
        run_case('Stability shock: cost of equity 12%',dict(base_inputs,ke=.12)),
        run_case(f'Services growth {args.services_low:g}%',dict(base_inputs,services_growth=args.services_low/100)),
        run_case(f'Services growth {args.services_high:g}%',dict(base_inputs,services_growth=args.services_high/100))]
    base=cases[0]
    if base['status']!='valid' or base['per_share'] is None:
        raise ValueError('Base cannot support this valuation comparison')
    for i,c in enumerate(cases):
        changed=[k for k,v in c['inputs'].items() if v!=base_inputs[k]]
        expected=[] if i==0 else ['ke'] if i in (1,2) else ['services_growth']
        if changed!=expected:raise AssertionError('More than one independent input changed')
        if c['status']=='valid':
            for k in ('operating_income','fcfe','per_share'):
                c['delta_'+k]=c[k]-base[k] if c[k] is not None else None
    for c in cases[1:3]:
        if c['rows']!=base['rows']:raise AssertionError('Discount-only shock changed statements')
    for c in cases[3:]:
        if c['status']!='valid':continue
        ds=c['services_revenue']-base['services_revenue']
        expected=ds*(base_inputs['services_margin']*(1-base_inputs['sga_gp'])-base_inputs['rd_sales'])
        if abs(c['delta_operating_income']-expected)>1e-6:raise AssertionError('Services EBIT bridge failed')
        if abs(c['rows'][-1]['inventory']-base['rows'][-1]['inventory'])>1e-6:
            raise AssertionError('Services-only shock changed Products inventory')
    restored=run_case('Restored base',base_inputs)
    if model.A!=original or restored['rows']!=base['rows'] or restored['per_share']!=base['per_share']:
        raise AssertionError('Base not restored exactly')
    spans={}
    for name,group in [('Stability',[cases[1],base,cases[2]]),('Services growth',[cases[3],base,cases[4]])]:
        spans[name]={}
        for key in ('operating_income','fcfe','per_share'):
            vals=[c.get(key) for c in group if c['status']=='valid' and c.get(key) is not None]
            spans[name][key]=max(vals)-min(vals) if len(vals)==3 else None
    path=Path(__file__).resolve().parent
    result=dict(cases=cases,spans=spans,restored_base=restored,checks_passed=True)
    (path/'Lab11_services_results.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print('SERVICES GROWTH AND STABILITY -- NEW SEGMENTED BASE')
    print('USD millions except value per share; FY2030 operating outputs; FCFE definition.')
    for c in cases:
        print('\n'+c['name'])
        print(f"Independent rates: Services {c['inputs']['services_growth']:.2%}; Products {c['inputs']['product_growth']:.2%}; cost of equity {c['inputs']['ke']:.2%}")
        if c['status']!='valid':
            print('INVALID:',c['reason']);continue
        value='UNAVAILABLE' if c['per_share'] is None else f"${c['per_share']:.2f}"
        print(f"FY2030 Services revenue {c['services_revenue']:,.1f}; Services mix {c['services_share']:.2%}; consolidated gross margin {c['gross_margin']:.2%}")
        print(f"Operating profit {c['operating_income']:,.1f}; FCFE {c['fcfe']:,.1f}; value/share {value}")
        print('Signed differences:',{k:c.get('delta_'+k) for k in ('operating_income','fcfe','per_share')})
        for r in c['checks']:
            g=0. if abs(r['gap'])<1e-6 else r['gap']
            print(f"FY{r['year']}: gap {g:.1f}; cash {r['cash']:,.1f}; cash floor passed {r['cash_ok']}")
    print('\nSPANS:',spans)
    print('PASS exact restored-base match; one input changed per run; independent Services EBIT bridge; product inventory unchanged in Services-only runs.')
    for title,keys in [('NEW BASE INCOME STATEMENT',('products_revenue','services_revenue','revenue','gross_profit','sga','rd','operating_income','net_other','tax','net_income')),
        ('NEW BASE BALANCE SHEET',model.ASSETS+('assets',)+model.LIABILITIES+('liabilities','equity','liabilities_equity')),
        ('NEW BASE CASH FLOWS',('net_income','depreciation','other_amort','change_inventory','change_other_wc','cfo','cfi','repayment','fcfe','dividends','buybacks','cff','cash'))]:
        model.table(title,base['rows'],[(model.label(k),k) for k in keys])


if __name__=='__main__':main()
````

---

## Company model — apple_services_proforma.py

````python
"""Apple Services/Products extension of the Lab 10 model; standard library only.
FY2025 category revenue and gross profit are from Apple FY2025 10-K pp. 23-24.
The original apple_proforma.py is unchanged. This file has a NEW segmented base.
Services/product margins are held constant; consolidated margin is calculated.
Inventory is linked to Products cost of sales; other WC keeps the original total-sales ratios.
"""
import math

A = dict(product_growth=.05, services_growth=.10,
         product_margin=112887/307003, services_margin=82314/109158, sga_gp=.141, rd_sales=.083,
         dep_ratio=8000/49834, other_amort=3698., capex=12715., tax=.16,
         inventory_days=5718/194116*365, net_other=-321., repayment=10932.,
         dividends=15421., buybacks=90711., cash_floor=25000.,
         ke=.10, terminal_growth=.025, shares=14773.260)
OPENING = dict(year=2025, revenue=416161., products_revenue=307003., services_revenue=109158., cash=35934., securities_current=18763.,
    receivables=39777., vendor_receivables=33180., inventory=5718., other_current_assets=14585.,
    securities_long=77723., ppe=49834., deferred_tax_assets=20777., other_long_assets=62950.,
    payables=69860., tax_payable=13016., other_current_liabilities=53371., deferred_revenue=9055.,
    commercial_paper=7979., debt_current=12350., debt_long=78328., other_long_liabilities=41549.,
    equity=73733.)
ASSETS = ('cash','securities_current','receivables','vendor_receivables','inventory',
          'other_current_assets','securities_long','ppe','deferred_tax_assets','other_long_assets')
LIABILITIES = ('payables','tax_payable','other_current_liabilities','deferred_revenue',
               'commercial_paper','debt_current','debt_long','other_long_liabilities')
WC_ASSETS = ('receivables','vendor_receivables','other_current_assets')
WC_LIABILITIES = ('payables','other_current_liabilities','deferred_revenue')


def gap(r):
    return sum(r[k] for k in ASSETS)-sum(r[k] for k in LIABILITIES)-r['equity']


def wc(r):
    return sum(r[k] for k in WC_ASSETS)-sum(r[k] for k in WC_LIABILITIES)


def assert_balanced(rows, a=A):
    for r in rows:
        name=f"FY{int(r['year'])}E"
        if not all(math.isfinite(v) for v in r.values()):
            raise ValueError(f'{name}: non-finite model value')
        g=gap(r)
        if abs(g)>1e-6:
            raise ValueError(f'{name}: assets - liabilities - equity gap {g:+,.1f}')
        if r['cash']<a['cash_floor']-1e-6:
            raise ValueError(f"{name}: cash-floor gap {r['cash']-a['cash_floor']:+,.1f}")
        for k in ASSETS+LIABILITIES:
            if r[k]<-1e-6:
                raise ValueError(f'{name}: negative {k}: {r[k]:,.1f}')
        if abs(r['cash']-r['opening_cash']-r['cfo']-r['cfi']-r['cff'])>1e-6:
            raise ValueError(f'{name}: cash-flow reconciliation failed')


def project(a=A):
    if abs(gap(OPENING))>1e-6:
        raise ValueError('Opening balance sheet does not balance')
    rows=[]
    p=OPENING.copy()
    for year in range(2026,2031):
        r=p.copy()
        r['year']=year
        r['products_revenue']=p['products_revenue']*(1+a['product_growth'])
        r['services_revenue']=p['services_revenue']*(1+a['services_growth'])
        r['revenue']=r['products_revenue']+r['services_revenue']
        r['products_gp']=r['products_revenue']*a['product_margin']
        r['services_gp']=r['services_revenue']*a['services_margin']
        r['gross_profit']=r['products_gp']+r['services_gp']
        r['products_cogs']=r['products_revenue']-r['products_gp']
        r['cogs']=r['revenue']-r['gross_profit']
        r['services_share']=r['services_revenue']/r['revenue']
        r['gross_margin']=r['gross_profit']/r['revenue']
        r['sga']=r['gross_profit']*a['sga_gp']
        r['rd']=r['revenue']*a['rd_sales']
        # Reported margins/expense ratios ALREADY include D&A. No second deduction.
        r['operating_income']=r['gross_profit']-r['sga']-r['rd']
        r['net_other']=a['net_other']
        r['pretax']=r['operating_income']+r['net_other']
        r['tax']=max(0.,r['pretax'])*a['tax']
        r['net_income']=r['pretax']-r['tax']
        r['depreciation']=p['ppe']*a['dep_ratio']
        r['other_amort']=a['other_amort']
        r['da']=r['depreciation']+r['other_amort']
        r['capex']=a['capex']
        r['ppe']=p['ppe']+r['capex']-r['depreciation']
        # Explicit simplifying allocation of non-PP&E amortization, not a reported schedule.
        r['other_long_assets']=p['other_long_assets']-r['other_amort']
        for key in WC_ASSETS+WC_LIABILITIES:
            r[key]=OPENING[key]/OPENING['revenue']*r['revenue']
        r['inventory']=r['products_cogs']*a['inventory_days']/365
        r['change_inventory']=r['inventory']-p['inventory']
        r['change_other_wc']=wc(r)-wc(p)
        r['cfo']=r['net_income']+r['da']-r['change_inventory']-r['change_other_wc']
        r['cfi']=-r['capex']
        opening_debt=p['debt_current']+p['debt_long']
        r['repayment']=min(a['repayment'],opening_debt)
        closing_debt=opening_debt-r['repayment']
        r['debt_current']=min(a['repayment'],closing_debt)
        r['debt_long']=closing_debt-r['debt_current']
        r['fcfe']=r['cfo']-r['capex']-r['repayment']
        r['dividends']=a['dividends']
        r['opening_cash']=p['cash']
        available=p['cash']+r['fcfe']-r['dividends']
        r['buybacks']=min(a['buybacks'],max(0.,available-a['cash_floor']))
        r['buyback_reduction']=a['buybacks']-r['buybacks']
        r['cff']=-r['repayment']-r['dividends']-r['buybacks']
        r['cash']=p['cash']+r['cfo']+r['cfi']+r['cff']
        r['equity']=p['equity']+r['net_income']-r['dividends']-r['buybacks']
        r['assets']=sum(r[k] for k in ASSETS)
        r['liabilities']=sum(r[k] for k in LIABILITIES)
        r['liabilities_equity']=r['liabilities']+r['equity']
        rows.append(r)
        p=r
    return rows


def valuation(rows,a=A):
    assert_balanced(rows,a)
    k,g=a['ke'],a['terminal_growth']
    if not k>g or k<=-1 or a['shares']<=0:
        raise ValueError('Require ke > terminal growth, ke > -1, positive shares')
    # Week 6: retain negative explicit cash flows, never floor them at zero.
    pv=sum(r['fcfe']/(1+k)**t for t,r in enumerate(rows,1))
    # At terminal: refinance maturities (net repayment 0) and replenish amortized assets.
    normal=rows[-1]['fcfe']+rows[-1]['repayment']-rows[-1]['other_amort']
    if rows[-1]['fcfe']<=0 or normal<=0:
        raise ValueError('Terminal value unresolved: nonpositive FCFE cannot support positive growing perpetuity')
    terminal=normal*(1+g)/(k-g)
    pvt=terminal/(1+k)**5
    return dict(pv_explicit=pv,normalized_fcfe=normal,terminal=terminal,pv_terminal=pvt,
                equity=pv+pvt,per_share=(pv+pvt)/a['shares'],terminal_share=pvt/(pv+pvt))


def table(title,rows,lines):
    print('\n'+title+' (USD millions)')
    print(f"{'Line':<42}"+''.join(f"{'FY'+str(r['year'])+'E':>14}" for r in rows))
    for label,key in lines:
        print(f'{label:<42}'+''.join(f'{r[key]:>14,.1f}' for r in rows))


def label(key):
    return {'cogs':'Cost of sales','sga':'SG&A','rd':'Research and development',
            'ppe':'PP&E, net','cfo':'Operating cash flow','cfi':'Investing cash flow',
            'cff':'Financing cash flow','fcfe':'FCFE before dividends / buybacks',
            'change_inventory':'Inventory increase (subtract)',
            'change_other_wc':'Other WC increase / (release)',
            'other_amort':'Other D&A addback','assets':'Total assets',
            'liabilities':'Total liabilities','liabilities_equity':'Total liabilities + equity',
            'other_current_liabilities':'Other current liabilities, excluding tax',
            'other_long_assets':'Other long-term assets, excluding DTA',
            'tax':'Income tax expense','net_other':'Net other income / (expense)',
            'equity':"Shareholders' equity"}.get(key,key.replace('_',' ').title())
````

---

## Visible results and accounting checks

````text
SERVICES GROWTH AND STABILITY -- NEW SEGMENTED BASE
USD millions except value per share; FY2030 operating outputs; FCFE definition.

Base
Independent rates: Services 10.00%; Products 5.00%; cost of equity 10.00%
FY2030 Services revenue 175,800.1; Services mix 30.97%; consolidated gross margin 48.74%
Operating profit 190,523.8; FCFE 153,571.7; value/share $125.52
Signed differences: {'operating_income': 0.0, 'fcfe': 0.0, 'per_share': 0.0}
FY2026: gap 0.0; cash 40,136.9; cash floor passed True
FY2027: gap 0.0; cash 54,131.2; cash floor passed True
FY2028: gap 0.0; cash 78,537.7; cash floor passed True
FY2029: gap 0.0; cash 114,063.2; cash floor passed True
FY2030: gap 0.0; cash 161,502.8; cash floor passed True

More stable: cost of equity 8%
Independent rates: Services 10.00%; Products 5.00%; cost of equity 8.00%
FY2030 Services revenue 175,800.1; Services mix 30.97%; consolidated gross margin 48.74%
Operating profit 190,523.8; FCFE 153,571.7; value/share $173.08
Signed differences: {'operating_income': 0.0, 'fcfe': 0.0, 'per_share': 47.56288674689361}
FY2026: gap 0.0; cash 40,136.9; cash floor passed True
FY2027: gap 0.0; cash 54,131.2; cash floor passed True
FY2028: gap 0.0; cash 78,537.7; cash floor passed True
FY2029: gap 0.0; cash 114,063.2; cash floor passed True
FY2030: gap 0.0; cash 161,502.8; cash floor passed True

Stability shock: cost of equity 12%
Independent rates: Services 10.00%; Products 5.00%; cost of equity 12.00%
FY2030 Services revenue 175,800.1; Services mix 30.97%; consolidated gross margin 48.74%
Operating profit 190,523.8; FCFE 153,571.7; value/share $98.07
Signed differences: {'operating_income': 0.0, 'fcfe': 0.0, 'per_share': -27.448485105170562}
FY2026: gap 0.0; cash 40,136.9; cash floor passed True
FY2027: gap 0.0; cash 54,131.2; cash floor passed True
FY2028: gap 0.0; cash 78,537.7; cash floor passed True
FY2029: gap 0.0; cash 114,063.2; cash floor passed True
FY2030: gap 0.0; cash 161,502.8; cash floor passed True

Services growth 5%
Independent rates: Services 5.00%; Products 5.00%; cost of equity 10.00%
FY2030 Services revenue 139,316.3; Services mix 26.23%; consolidated gross margin 46.91%
Operating profit 169,919.4; FCFE 135,259.0; value/share $112.56
Signed differences: {'operating_income': -20604.385034366278, 'fcfe': -18312.712710188585, 'per_share': -12.965209216893314}
FY2026: gap 0.0; cash 36,960.9; cash floor passed True
FY2027: gap 0.0; cash 44,713.5; cash floor passed True
FY2028: gap 0.0; cash 59,368.9; cash floor passed True
FY2029: gap 0.0; cash 81,138.4; cash floor passed True
FY2030: gap 0.0; cash 110,265.4; cash floor passed True

Services growth 15%
Independent rates: Services 15.00%; Products 5.00%; cost of equity 10.00%
FY2030 Services revenue 219,555.7; Services mix 35.91%; consolidated gross margin 50.65%
Operating profit 215,235.1; FCFE 175,689.9; value/share $141.00
Signed differences: {'operating_income': 24711.271886291215, 'fcfe': 22118.179102221475, 'per_share': 15.476827494329171}
FY2026: gap 0.0; cash 43,312.9; cash floor passed True
FY2027: gap 0.0; cash 63,866.4; cash floor passed True
FY2028: gap 0.0; cash 99,013.5; cash floor passed True
FY2029: gap 0.0; cash 150,407.8; cash floor passed True
FY2030: gap 0.0; cash 219,965.7; cash floor passed True

SPANS: {'Stability': {'operating_income': 0.0, 'fcfe': 0.0, 'per_share': 75.01137185206417}, 'Services growth': {'operating_income': 45315.65692065749, 'fcfe': 40430.89181241006, 'per_share': 28.442036711222485}}
PASS exact restored-base match; one input changed per run; independent Services EBIT bridge; product inventory unchanged in Services-only runs.

NEW BASE INCOME STATEMENT (USD millions)
Line                                             FY2026E       FY2027E       FY2028E       FY2029E       FY2030E
Products Revenue                               322,353.2     338,470.8     355,394.3     373,164.1     391,822.3
Services Revenue                               120,073.8     132,081.2     145,289.3     159,818.2     175,800.1
Revenue                                        442,427.0     470,552.0     500,683.6     532,982.3     567,622.3
Gross Profit                                   209,076.8     224,057.9     240,240.7     257,730.8     276,643.1
SG&A                                            29,479.8      31,592.2      33,873.9      36,340.0      39,006.7
Research and development                        36,721.4      39,055.8      41,556.7      44,237.5      47,112.7
Operating Income                               142,875.5     153,409.9     164,810.1     177,153.2     190,523.8
Net other income / (expense)                      -321.0        -321.0        -321.0        -321.0        -321.0
Income tax expense                              22,808.7      24,494.2      26,318.2      28,293.2      30,432.4
Net Income                                     119,745.8     128,594.7     138,170.8     148,539.1     159,770.3

NEW BASE BALANCE SHEET (USD millions)
Line                                             FY2026E       FY2027E       FY2028E       FY2029E       FY2030E
Cash                                            40,136.9      54,131.2      78,537.7     114,063.2     161,502.8
Securities Current                              18,763.0      18,763.0      18,763.0      18,763.0      18,763.0
Receivables                                     42,287.5      44,975.7      47,855.7      50,942.9      54,253.8
Vendor Receivables                              35,274.2      37,516.5      39,918.9      42,494.0      45,255.8
Inventory                                        6,003.9       6,304.1       6,619.3       6,950.3       7,297.8
Other Current Assets                            15,505.5      16,491.2      17,547.2      18,679.2      19,893.2
Securities Long                                 77,723.0      77,723.0      77,723.0      77,723.0      77,723.0
PP&E, net                                       54,549.0      58,507.1      61,829.8      64,619.1      66,960.6
Deferred Tax Assets                             20,777.0      20,777.0      20,777.0      20,777.0      20,777.0
Other long-term assets, excluding DTA           59,252.0      55,554.0      51,856.0      48,158.0      44,460.0
Total assets                                   370,272.0     390,742.8     421,427.6     463,169.5     516,887.0
Payables                                        74,269.2      78,990.5      84,048.6      89,470.5      95,285.5
Tax Payable                                     13,016.0      13,016.0      13,016.0      13,016.0      13,016.0
Other current liabilities, excluding tax        56,739.5      60,346.4      64,210.7      68,352.9      72,795.3
Deferred Revenue                                 9,626.5      10,238.5      10,894.1      11,596.8      12,350.6
Commercial Paper                                 7,979.0       7,979.0       7,979.0       7,979.0       7,979.0
Debt Current                                    10,932.0      10,932.0      10,932.0      10,932.0      10,932.0
Debt Long                                       68,814.0      57,882.0      46,950.0      36,018.0      25,086.0
Other Long Liabilities                          41,549.0      41,549.0      41,549.0      41,549.0      41,549.0
Total liabilities                              282,925.2     280,933.4     279,579.4     278,914.2     278,993.3
Shareholders' equity                            87,346.8     109,809.4     141,848.2     184,255.3     237,893.6
Total liabilities + equity                     370,272.0     390,742.8     421,427.6     463,169.5     516,887.0

NEW BASE CASH FLOWS (USD millions)
Line                                             FY2026E       FY2027E       FY2028E       FY2029E       FY2030E
Net Income                                     119,745.8     128,594.7     138,170.8     148,539.1     159,770.3
Depreciation                                     8,000.0       8,756.9       9,392.3       9,925.7      10,373.5
Other D&A addback                                3,698.0       3,698.0       3,698.0       3,698.0       3,698.0
Inventory increase (subtract)                      285.9         300.2         315.2         331.0         347.5
Other WC increase / (release)                   -2,824.0      -3,023.9      -3,239.6      -3,472.6      -3,724.4
Operating cash flow                            133,981.9     143,773.3     154,185.6     165,304.4     177,218.7
Investing cash flow                            -12,715.0     -12,715.0     -12,715.0     -12,715.0     -12,715.0
Repayment                                       10,932.0      10,932.0      10,932.0      10,932.0      10,932.0
FCFE before dividends / buybacks               110,334.9     120,126.3     130,538.6     141,657.4     153,571.7
Dividends                                       15,421.0      15,421.0      15,421.0      15,421.0      15,421.0
Buybacks                                        90,711.0      90,711.0      90,711.0      90,711.0      90,711.0
Financing cash flow                           -117,064.0    -117,064.0    -117,064.0    -117,064.0    -117,064.0
Cash                                            40,136.9      54,131.2      78,537.7     114,063.2     161,502.8
````
