# Lab 13 — Portfolio Mandate Defense

## The common question

Which portfolios does the Meridian Foundation's mandate permit, and what must the CIO answer before anyone optimizes?

A passes all five implemented checks. B fails the reserve, liquidity, and issuer checks. C fails the reserve check. Passing these checks establishes only compliance with the rules measurable from the supplied holdings and weights; it does not establish full mandate compliance or suitability. The CIO must specify the pilot's optimization objective before portfolios can be ranked.

## S1–S10: statement types and reasons

Some statements contain more than one element; the table identifies their main role and explains any distinction.

| Statement | Type | Reason |
|---|---|---|
| S1: Seven-year horizon; annual rebalancing | Hard constraint | The horizon and rebalancing schedule govern implementation, although a single snapshot of weights cannot verify either. |
| S2: CPI + 4% annually, net of costs, over rolling five-year periods | Objective | This is the return goal and evaluation period; it is not a guaranteed outcome or a fully specified optimization function. |
| S3: $0.75 million quarterly; twelve months of payouts in cash or daily-liquid government securities | Hard constraint | Four payments require $3 million, or 3% of the $100 million reserve, in eligible holdings. |
| S4: 60% global equities / 40% U.S. investment-grade bonds benchmark | Preference / evaluation reference | It defines a comparator; it does not explicitly require those portfolio weights or impose a tracking-error limit. |
| S5: Long-only; no borrowing, short sales, or derivatives | Hard constraint | These are explicit prohibitions. Nonnegative weights and the approved holdings support part of the check; separate financing or derivative exposures require additional information. |
| S6: No single issuer above 8% | Hard constraint | Aggregate each company's securities, applying the stated exemptions for cash, Treasury, and diversified funds. |
| S7: Annual turnover at most 25% without committee approval | Hard constraint with approval exception | Turnover is limited unless approved; current weights alone do not reveal trades or annual turnover. |
| S8: At least 90% redeemable within five business days | Hard constraint | Sum weights whose stated redemption time is at most five business days and compare the result with 90%. |
| S9: No calendar-year loss greater than 10%; no measure or breach rule | Unverifiable promise | As stated, it provides neither a usable risk test nor a breach procedure; risky holdings cannot make an unconditional loss guarantee. The checker must request clarification. |
| S10: No sector, ESG, tax, or home-bias preference; pilot objective unspecified | Missing | No extra preferences should be invented, and the pilot lacks the criterion needed to choose among feasible portfolios. |

## Checker and verification

`mandate.py` uses only the Python standard library. Editable holdings, candidate weights, monetary inputs, thresholds, and issuer exemptions appear at the top. All reported measurements and verdicts are computed from those inputs. Percent weights use percentage points: 2 means 2%.

Run from the folder containing the file:

```powershell
python mandate.py
```

The local Windows `python` launcher was unavailable during verification, so the checker was run successfully using the bundled Python executable. No third-party packages are needed.

Reserve minimum = 4 × $0.75 million ÷ $100 million × 100 = **3.0%**.

| Check | A | B | C | D |
|---|---|---|---|---|
| Weights sum to 100 | 100.0 pass | 100.0 pass | 100.0 pass | 100.0 pass |
| Lowest weight is nonnegative | 0.0 pass | 0.0 pass | 0.0 pass | 0.0 pass |
| Reserve at least 3.0% | 14.0 pass | 1.0 FAIL | 2.0 FAIL | 100.0 pass |
| Redeemable within five business days at least 90% | 100.0 pass | 85.0 FAIL | 100.0 pass | 100.0 pass |
| Largest single company at most 8% | 0.0 pass | 9.0 FAIL | 8.0 pass | 0.0 pass |
| Calendar-year loss | Requires CIO clarification | Requires CIO clarification | Requires CIO clarification | Requires CIO clarification |
| Verdict | Passes every checkable rule | Fails 3 rules | Fails 1 rule | Passes every checkable rule |

A's reserve is 2% cash + 2% Treasury bills + 10% Treasury notes = 14%. The supplied eligibility table includes the Treasury note: daily liquidity qualifies it for this check even though its market value can fluctuate.

B's private real estate allocation is 15%, leaving 85% redeemable within five days. Its Acme bonds and stock add to 5% + 4% = 9%, exceeding the issuer limit. C's Acme exposure equals the 8% ceiling and therefore passes.

### Negative-weight probe

For A, changing cash from 2 to -2 and global equity from 60 to 64 produces total weight 100.0, lowest weight -2.0, eligible reserve 10.0, liquid share 100.0, and largest company 0.0. Only long-only fails. These results were verified using a copy of A's weights; the saved candidate A retains its original values.

### Code comprehension quiz

Question: Why must the checker add Acme's bond and stock weights before applying the 8% issuer limit?

Answer: The limit applies to total exposure to one company, not to each security separately. Testing the bond and stock independently would incorrectly pass B, because 5% and 4% are each below 8%, even though their combined 9% breaches S6.

The aggregation line `company_weights[issuer] = company_weights.get(issuer, 0) + weight` retrieves the company's accumulated weight, uses zero if this is its first holding, and adds the current security's weight.

## The attack: candidate D

| Holding | D weight (%) |
|---|---:|
| Cash | 100 |
| Treasury bills | 0 |
| Treasury 10-year note | 0 |
| Global equity index fund | 0 |
| Investment-grade bond fund | 0 |
| Private real estate fund | 0 |
| Acme Corp bonds | 0 |
| Acme Corp stock | 0 |

D is included in `mandate.py` and was run successfully: all five implemented checks pass. It exposes S2, because the checker has no return assumptions, inflation assumptions, or cost model with which to assess the CPI + 4% goal; no optimization was performed.

### Two-sentence judgment

The objection holds as a suitability concern: a 100% cash portfolio can pass every implemented check while offering no demonstrated basis for achieving CPI + 4% net over rolling five-year periods. S2 supports the CIO's rejection, although the supplied data do not prove that D must miss the target.

### Skeptical colleague role

I would cite S2 against D and ask for evidence that cash can support the real-return objective. I would also challenge any claim that passing the program resolves S9, since the program deliberately leaves that statement untested. S4 alone does not prohibit D: a benchmark is not automatically an allocation constraint.

## One question for the CIO

**What should the pilot optimize: the estimated probability of meeting the CPI + 4% net rolling five-year goal, or the reduction of downside risk while treating that return figure as an aspiration?**

If the CIO selects target attainment, I would compare feasible allocations using a documented model of net real returns and target-shortfall probability, potentially supporting more growth exposure. If the CIO prioritizes downside protection, I would use a defined downside measure and would consider more defensive allocations even when their modeled probability of meeting the return target is lower. Neither answer supplies a numerical allocation without assumptions, and S9 still needs a measurable definition and breach procedure before final implementation.

## Investment policy statement: learn on your own

An investment policy statement (IPS) records a client's purpose, return goals, risk requirements, implementation limits, and governance arrangements. It translates client instructions into a framework for selecting, monitoring, and reviewing portfolios.

Objectives define what success means. Constraints limit the feasible choices. A benchmark provides a comparison, while governance rules specify who may approve exceptions, how the portfolio is monitored, and what happens after a breach. An IPS should distinguish an aspiration from an enforceable rule and identify missing definitions before implementation.

| IPS component | Meridian statements |
|---|---|
| Horizon and implementation schedule | S1 |
| Return objective and evaluation period | S2 |
| Spending needs and eligible liquidity reserve | S3 |
| Performance benchmark | S4 |
| Permitted exposures and financing restrictions | S5 |
| Company concentration limit and exemptions | S6 |
| Trading limit and exception authority | S7 |
| Portfolio liquidity requirement | S8 |
| Unresolved loss tolerance and breach governance | S9 |
| Absent additional preferences and missing pilot optimization criterion | S10 |

The checker is one monitoring tool within an IPS process. The snapshot inputs cannot establish adherence to annual rebalancing, historical turnover, net real-return achievement, or an undefined loss rule. The record also lacks a separate account of financing and off-table exposures. Those limitations should be resolved through the appropriate data and policy definitions rather than silently reported as passes.

## Reflection

A portfolio can pass every checkable rule and still be wrong for the client because the program checks only a subset of the mandate. Candidate D makes the distinction concrete: concentration and liquidity compliance do not show that a portfolio can finance distributions while pursuing the real-return goal. A passing verdict must be read within the checker's scope.

The classification I would be least certain about is S4. The benchmark sounds prescriptive because it names exact weights, but the statement does not require the portfolio to hold those weights. I therefore classify it as an evaluation reference within the permitted preference category; a binding allocation or tracking limit would need explicit language.

## Project 2: draft client mandate

This is a proposed fictional client for Project 2, not additional information about Meridian. The assumptions below require client agreement before use.

**Client:** Northbridge Community Scholarship Fund, with a $10 million reserve supporting annual scholarship grants over a ten-year horizon.

**Objective:** Pursue CPI + 3% annualized, net of all investment costs, over rolling five-year periods while supporting planned scholarship distributions. This is a target rather than a guarantee.

**Hard constraints:**

- Pay $75,000 at the end of each quarter and maintain at least twelve months of planned distributions in cash or daily-liquid U.S. Treasury securities. At the initial reserve value this is $300,000, or 3%; recompute the percentage using the current portfolio value.
- Use long-only, fully funded holdings with weights totaling 100%; no borrowing, short sales, or derivatives.
- Keep at least 90% of portfolio value redeemable within five business days.
- Limit each company's combined securities to 5% of portfolio value; exempt cash, U.S. Treasury securities, and diversified funds.
- Review annually and rebalance at the annual review, subject to spending and reserve maintenance needs.
- Limit annual one-way turnover to 20% without written investment-committee approval. Measure turnover as the lesser of annual purchases or annual sales, excluding trades solely to accommodate external contributions and distributions, divided by average month-end portfolio value during the year.

**One client question:** Should the pilot maximize the modeled probability of meeting the real-return target, or prioritize reducing downside risk even if the target becomes less likely?

**Answer that changes the design:** Choosing target attainment would favor comparing feasible portfolios by modeled net real-return shortfall probability; choosing downside protection would shift the selection criterion toward a client-approved downside-risk measure and could support a more defensive allocation. The risk measure and assumptions must be agreed before optimization.

## Checkout

- Checker matches the supplied A–C values and verdicts: verified.
- Negative-weight probe fails only long-only: verified; original A preserved.
- S1–S10 sorted with reasons: included.
- D added, run, and judged against a named statement: included and verified.
- One CIO question and design consequence: included.
- IPS explanation, mapping, reflection, and draft Project 2 mandate: included.
- Attendance and completion of the separate IPS reading: student to confirm.
- GitHub delivery: upload `lab13.md` and `mandate.py`, then paste their GitHub file links into the Lab 13 quiz before it closes. This workspace has no Git repository or configured remote, so no GitHub upload has been performed.

Prepared with AI assistance under the updated classroom permission described by the student. Review the reflection and proposed Project 2 client so they accurately represent your understanding and chosen project.
