# Apple DCF and Reverse DCF

All valuation figures are in **USD millions** unless marked otherwise. Per-share
figures are in USD per share. This model uses Apple FY2025 financial data and a
target share price of **$326.00**. It is an academic valuation exercise, not
investment research or financial advice.

## Model inputs

| Input | Value |
| --- | ---: |
| Starting FCFF (FY2025) | $95,622.0000 |
| FCFF growth, Years 1-5 | 0.57% annually |
| WACC | 8.91% |
| Terminal growth | 2.00% |
| Cash and investments | $132,420.0000 |
| Debt | $98,657.0000 |
| Diluted shares | 15,004.697 million |

Starting FCFF is calculated as operating income after tax plus D&A less capital
expenditures and the increase in operating net working capital:

`$133.050B × (1 − 15.6%) + $11.698B − $12.715B − $15.655B = $95.622B`

Source: [Apple FY2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm).

## Base-case DCF output

| DCF line item | Value |
| --- | ---: |
| FCFF Year 1 | $96,167.0454 |
| FCFF Year 2 | $96,715.1976 |
| FCFF Year 3 | $97,266.4742 |
| FCFF Year 4 | $97,820.8931 |
| FCFF Year 5 | $98,378.4722 |
| PV of explicit FCFF | $378,863.3325 |
| Terminal value, Year 5 | $1,452,185.8411 |
| PV of terminal value | $947,727.3368 |
| Enterprise value | $1,326,590.6693 |
| Equity value | $1,360,353.6693 |
| Value per share (USD) | $90.6619 |
| PV of TV / enterprise value | 71.44% |

## Reverse DCF: value implied by a $326.00 share price

The reverse DCF holds WACC, terminal growth, net cash, and diluted shares
constant. It solves for one constant annual FCFF growth rate over Years 1-5
that makes the model's per-share value equal $326.00.

| Reverse-DCF line item | Value |
| --- | ---: |
| Target share price | $326.00 |
| Implied equity value | $4,891,531.2220 |
| Implied enterprise value | $4,857,768.2220 |
| Implied annual FCFF growth, Years 1-5 | **33.70%** |
| FCFF Year 1 | $127,847.1454 |
| FCFF Year 2 | $170,932.3438 |
| FCFF Year 3 | $228,537.4935 |
| FCFF Year 4 | $305,555.8987 |
| FCFF Year 5 | $408,529.9345 |
| FCFF Year 6 (terminal cash flow) | $416,700.5332 |
| PV of explicit FCFF | $922,202.0534 |
| Terminal value, Year 5 | $6,030,398.4543 |
| PV of terminal value | $3,935,566.1686 |
| PV of TV / enterprise value | 81.02% |

### Operating performance implied by the reverse DCF

FY2025 FCFF margin was 22.98% ($95.622B FCFF / $416.161B revenue), and
operating margin was 31.97%. If both margins remain unchanged, the required
33.70% FCFF growth is also the required revenue and operating-income growth.

| Metric | FY2025 actual | Year 5 implied target |
| --- | ---: | ---: |
| Revenue | $416.161B | $1.778T |
| Operating income | $133.050B | $568.435B |
| FCFF | $95.622B | $408.530B |
| FCFF margin | 22.98% | 22.98% |
| Operating margin | 31.97% | 31.97% |

The reverse case requires Year-5 FCFF that is **4.15x** the base-case Year-5
FCFF of $98.378B.

If revenue grew more slowly, a higher FCFF margin would be required to meet the
same $408.530B Year-5 FCFF target. The operating-margin column holds the FY2025
tax rate and D&A, capex, and working-capital ratios constant.

| Revenue CAGR | Year-5 revenue | Required Year-5 FCFF margin | Implied operating margin |
| ---: | ---: | ---: | ---: |
| 10% | $670.2B | 60.95% | 76.97% |
| 15% | $837.0B | 48.81% | 62.57% |
| 20% | $1.036T | 39.45% | 51.49% |
| 25% | $1.270T | 32.17% | 42.86% |
| 33.70% | $1.778T | 22.98% | 31.97% |

## Implied growth-rate interpretation

The $326 target price cannot determine both the explicit FCFF growth rate and
the terminal growth rate at the same time; one must be an assumption.

| Scenario | Explicit FCFF growth, Years 1-5 | Terminal growth |
| --- | ---: | ---: |
| Reverse DCF used above | **33.70%** | 2.00% assumed |
| Keep the base-case FCFF growth | 0.57% assumed | **7.37% implied** |

The 7.37% alternative is close to the 8.91% WACC. A perpetuity growth rate
that close to WACC creates an extremely large terminal value and is generally
not a credible long-run assumption for a mature company.

## Reproducing the analysis

Run the accompanying script with Python 3:

```bash
python dcf.py
```

The script has no third-party dependencies. Change the input constants at the
top of `dcf.py` to test a different share price, WACC, terminal growth rate,
capital structure, or FCFF forecast.
