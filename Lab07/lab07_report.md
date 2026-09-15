# Lab 07 — Comparable-Company Policy and Implied Range

## Purpose and basis

This exercise applies P/E comparison to **Asbury Automotive (ABG)** using the instructor's frozen inputs. All figures are USD per share. December 31, 2024 prices are paired with subsequently reported FY2024 **total GAAP diluted EPS**. This is a retrospective training comparison: the earnings were not necessarily public at the price date. It is not a trade recommendation available on December 31, 2024.

AI assisted with the explanation, code and verification. The calculations were executed, not just copied from the answer table. This document does not claim that a pre-AI partner conversation took place. Peer decisions below are supported analytical recommendations for individual review.

## 1. Reopen the saved DCF

The saved Apple DCF was rerun successfully using `dcf.py`. It reproduces **$90.6619 per diluted share**, or **$90.66**. The saved work contains a point estimate, not a scenario range.

Its main assumptions are starting FCFF of $95,622 million, 0.57% annual growth over five years, 8.91% WACC and 2% terminal growth. It adds $132,420 million of cash/investments, subtracts $98,657 million of debt and divides by 15,004.697 million diluted shares. Higher cash flows or lower discount rates generally increase DCF value. Here, 71.44% of enterprise value comes from discounted terminal value, making the terminal assumptions consequential.

**Question to investigate:** Why might investors pay a different price for one dollar of reported earnings at two apparently similar companies?

The Apple model is prior-work context only; its inputs are not used in the Asbury calculation.

## 2. What P/E measures

**Price per share** is the market price of one share. **Diluted earnings per share** allocates earnings to the weighted-average diluted share count, including the effects of potentially dilutive securities under the applicable accounting rules. **P/E = price per share / annual EPS.** A 10x P/E means investors pay about $10 for each $1 of annual reported earnings. It is not a guaranteed ten-year payback: earnings can change, and earnings are not necessarily distributed as cash.

P/E makes different-sized companies easier to compare because both the price and earnings are measured per share. A peer's multiple can be multiplied by the target's EPS to produce an implied target share price. This provides a market-based reference alongside a DCF, which values forecast cash flows directly.

Comparability requires attention to business model, growth, risk, geography, financing and earnings definitions. A negative or zero denominator does not support a meaningful earnings multiple for this exercise. Unusual profits can make a stock look artificially cheap; temporarily weak earnings can make its P/E look high. Adjusted earnings should not be mixed with total GAAP diluted EPS.

**A lower P/E does not automatically mean a better investment.** It can reflect slower expected growth, greater risk or unsustainable earnings. The useful question is whether the difference in price paid for earnings is justified by the underlying economics.

## 3. Case peer policy and decisions

The relevant match is **franchised vehicle retail plus service/parts and related customer revenue**. These businesses share exposure to vehicle demand, inventory, manufacturer relationships and after-sales activity. Merely being in the automotive industry would also include manufacturers or suppliers whose costs, capital requirements and risks differ substantially.

| Candidate | Decision | Business explanation and qualification |
|---|---|---|
| AutoNation (AN) | **Use** | Its U.S. franchised retail operations sell new and used vehicles and generate parts/service and finance/insurance revenue. This matches the case's core dealership economics. Its standalone used-vehicle stores and captive finance operations mean its earnings mix is not identical; use does not imply perfect comparability. |
| Group 1 Automotive (GPI) | **Qualify** | Its vehicle retail, maintenance, parts and financing-related activities fit the operating model. Its U.S. and U.K. footprint introduces a different geographic mix. Currency exposure, local demand and regulation can affect the appropriate multiple, so its reference deserves qualification. |

Sources opened by the assistant: [AutoNation FY2024 10-K](https://www.sec.gov/Archives/edgar/data/350698/000035069825000029/an-20241231.htm), Part I, Item 1, Business; and [Group 1 FY2024 10-K](https://www.sec.gov/Archives/edgar/data/1031203/000103120325000013/gpi-20241231.htm), Part I, Item 1, Business → General.

Both peers are admitted. These decisions are based on business fit, not on which valuation looks preferable. The attachment labels GPI a qualified candidate. The separate instructor file `teach-comps-worked-example.md` was not supplied or found locally; these primary-source checks supplement the attachment and do not claim to reproduce that missing reading.

## 4. Frozen inputs and implementation

| Company / role | December 31, 2024 close | FY2024 total GAAP diluted EPS |
|---|---:|---:|
| Asbury Automotive (ABG), target | $243.03 | $21.50 |
| AutoNation (AN), peer | $169.84 | $16.92 |
| Group 1 Automotive (GPI), qualified peer | $421.48 | $36.81 |

**Numeric source:** The instructor's Lab 07 attachment, frozen case-input table. The calculator fetches no data and installs no packages.

For each peer:

```text
Peer P/E = peer price / peer diluted EPS
Target implied price = peer P/E × target diluted EPS
```

The calculator takes the minimum, median and maximum admitted peer multiples. With two peers, the median is the arithmetic midpoint of their multiples. It never adds cash or subtracts debt: P/E already relates equity price to equity earnings.

`lab07_comps.py` is standalone and uses the standard library. Edit `TARGET` and `PEERS` at the top. Tickers are normalized, duplicates are removed with the first occurrence retained, and the target is excluded. Invalid inputs are labeled not meaningful. One valid peer gives a reference, and zero valid peers give no estimate. An invalid target price prevents an observed P/E or price comparison, but valid target EPS can still support a peer-implied price.

Calculations retain 50-digit Decimal precision without intermediate display rounding. Only printed multiples and prices are rounded to six decimals and cents, respectively.

### Run command

The script was tested with Python 3. With Python on PATH, run from this file's directory:

```bash
python lab07_comps.py
```

## 5. Checked results

| Check | Instructor answer | Executed result | Match |
|---|---:|---:|---|
| AutoNation P/E | 10.037825x | 10.037825x | Yes |
| Group 1 P/E | 11.450149x | 11.450149x | Yes |
| Peer median P/E | 10.743987x | 10.743987x | Yes |
| Asbury implied range | $215.81–$246.18 | $215.81–$246.18 | Yes |
| Asbury at peer median | $231.00 | $231.00 | Yes |
| Remove GPI: AN reference | $215.81 | $215.81 | Yes |
| Change from full-peer estimate | −$15.18 | −$15.18 | Yes |

### Worked arithmetic check

```text
AN P/E = 169.84 / 16.92 = 10.0378250591...
AN-implied ABG price = (169.84 / 16.92) × 21.50
                     = 215.8132387707... → $215.81

GPI P/E = 421.48 / 36.81 = 11.4501494159...
GPI-implied ABG price = (421.48 / 36.81) × 21.50
                      = 246.1782124423... → $246.18

Median-implied ABG price = (215.8132387707... + 246.1782124423...) / 2
                         = 230.9957256065... → $231.00
```

This is a worked check supplied for the student to understand and reproduce; it is not represented as an unaided student calculation.

## 6. Change the peer set

**Prediction:** Removing GPI should lower the estimate because GPI has the higher P/E. AN would become the only reference, so the result would no longer be a range.

**Executed result:** Removing GPI leaves **$215.81**, with an unrounded change of approximately **−$15.1824868358**, displayed as **−$15.18**. Subtracting the already rounded displayed values, $215.81 − $231.00, gives −$15.19. That one-cent difference is why the script computes changes before rounding.

For completeness, removing AN leaves GPI's **$246.18** reference, a **+$15.18** change from the full-peer median. Removing the sole remaining peer leaves no estimate.

A single peer cannot reveal dispersion across peers. Calling its result a range would imply evidence that is no longer present. The sensitivity demonstrates the importance of selection; it does not justify excluding GPI because its price is higher. The original use/qualify decisions stay in place.

## 7. Reflection

The case estimates what Asbury's own earnings would be worth if investors paid the selected peers' multiples. AutoNation provides a core dealership comparison; Group 1 adds a qualified comparison with geographic differences. The $243.03 observed Asbury price is inside the two-peer span and above the $231.00 median reference, but that does not prove fair value or overvaluation.

The peer companies themselves could be mispriced. Different growth, risk and earnings quality could justify different multiples. The training comparison also uses earnings published after the price date. The range is therefore a conditional comparison, not a confidence interval, and the median is a reference rather than an independently proven intrinsic value.

The transferable lesson for the next lab is to choose peers based on economics, align price dates and earnings definitions, validate arithmetic and test how much the conclusion depends on one peer. A peer result complements a DCF; it does not replace the need to defend cash-flow assumptions.

## 8. Reproducibility and checkout

- `lab07_report.md`: explanation, peer policy, checks and reflection.
- `lab07_comps.py`: standalone editable calculator.
- `lab07_output.txt`: captured successful calculator output.
- `test_lab07_comps.py`: four passing tests covering instructor results, duplicates/target exclusion, one/no peers, and invalid inputs.

To run the tests from the same directory: `python -m unittest test_lab07_comps.py`.

The assignment requests **GitHub links to the files**:

- [Report](https://github.com/alexalex123-alex/AAPL--research/blob/main/Lab07/lab07_report.md)
- [Calculator](https://github.com/alexalex123-alex/AAPL--research/blob/main/Lab07/lab07_comps.py)
- [Captured output](https://github.com/alexalex123-alex/AAPL--research/blob/main/Lab07/lab07_output.txt)
- [Tests](https://github.com/alexalex123-alex/AAPL--research/blob/main/Lab07/test_lab07_comps.py)

Read the report and make the peer judgments your own before individual checkout. No classroom conversation or missing worked-case reading is claimed as completed.
