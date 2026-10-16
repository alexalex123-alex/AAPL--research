# AAPL - September 14, 2026 valuation refresh

**Student recommendation: INITIATE.** Alex Schwanke confirmed this judgment after an AI-closed partner review with Jess Tran. This folder preserves a material valuation disagreement instead of changing the output to agree with the student. Core DCF approximately **$73-$254/share**, versus **$333.08** historical close. A high operating case with an extended growth fade gives **$286-$350**; that requires a much longer economic runway. The upper figure is not a confidence bound or proof of a safe purchase price.

## Start the application

Windows: double-click `Start-AAPL.cmd`, then open http://127.0.0.1:8766. Keep the terminal open; Ctrl+C stops it.

Python 3.10+ standard library, no packages or credentials needed:

```
python -m unittest discover -s . -p "test_*.py" -v
python run.py
python run.py --serve --port 8766
```

Open `visible_output/index.html` directly for all included frozen output and offline discount/growth exploration. Operating-driver recalculation requires the server. Do not record an earlier2025 application tab while speaking about this refresh.

## Recording and written evidence

- `docs/Video-Scripts.txt`: three narration drafts incorporating actual partner answers, the explicit initiate stance and the changed valuation date. They are not transcripts of recordings that already happened.
- `docs/recording-screen-plan.md`: exact screens/functions to show in each video.
- `docs/Decision-Memo.pdf`: two-page committee memo with conditional ranges, risks and the remaining judgment gap.
- `docs/Research-Evolution.pdf`: source/date correction and research evolution. No successful Edition A receipt has been supplied; no pre-AI baseline is fabricated.
- `docs/Partner-Review-Record.pdf`: supplied Alex/Jess review, reciprocal NVIDIA question/check, labeled analytical completion and missing details.
- `docs/Validation-and-AI-Use.pdf` and matching Markdown: working technical/AI record, not a final submitted freeze.
- `docs/README-REMAINING.md`: actual receipts, human locked record, recordings/transcripts, access checks and unresolved decision support.

## Architecture and evidence

`model.py`: latest-public TTM reconstruction inputs; five linked operating periods; FCFF/WACC/Gordon terminal with explicit reinvestment; enterprise-equity bridge; causal cases, WACC/g grid, reverse DCF, stresses, driver sensitivities and a terminal growth-duration challenge. `run.py` and `dashboard.html` produce the included report/application. The source/date filter is enforced in `rebuild_inputs.py`. `data/fact_ledger.json`, `manual_ledger.json` and `source_manifest.json` preserve definitions, filing dates and transformations. `docs/sources-and-normalization.md` explains source conflicts, tariff/mix reserve and current calibrations. The challenge CSV includes every independent driver.

Apple base: TTM ended June27,2026, calculated as FY2025 +9m2026 -9m2025. June balance-sheet proxies are used for five annual decision periods ending September14,2027-2031. This does not claim to know unreported fiscal2026 annual results or a September daily balance roll-forward. The timing/basis simplification is explicit. The older2025 full analysis remains in the existing research repository; it is not bundled here. The original changed-input engine and project-only provenance are retained at this package root.

`fetch_sources.py` is an optional network refresh and must not be run blindly on a frozen submission. `rebuild_inputs.py` rebuilds selected inputs from saved snapshots. Both preserve availability filters. The Siri release was verified via web reading; direct archival download returned403, so no fake local copy is supplied. Same-day release timing before close remains a condition. Raw financial snapshots may contain later filings, but the selected ledger excludes them.

## Validation and human-only work

Thirteen financial/model test groups and four evidence-tool checks pass. The technical changed-input demonstration is `python technical_changed_input.py`; it does not satisfy the student's human-authored AI-off exercise. The exercise remains outstanding even though Alex confirms the partner exchange itself was AI closed.

Inside the versioned repository copy, `locked_test.py prepare`, `run` and `review` support the student's independent prediction, pre-run commit, protected hashes, preserved outputs and personal diagnosis. Use it with AI closed and your own Git identity. Do not substitute a synthetic test fixture or the technical expectation for your own prediction. The helper's automatic model rule is separate from Alex's initiate judgment.

## Material limits

Tariff-refund amount is not independently quantified; normalized Products margin38% is a judgment reserve. Narrow WC freezes other current balances, which may omit genuine operating investment. PP&E/non-PP&E D&A allocation and replacement are estimates. A newly separate20,342m intangible line is explicitly aggregated with other noncurrent assets after the base check failed; a different generic SEC tag is not silently substituted. Cash reserve30bn, marginal debt cost6%, ERP4.5%, forecast paths and terminal ROIC are assumptions. Beta is recalculated from59 complete monthly adjusted-return observations; it is not claimed to be Alex's exact earlier Yahoo beta. Shares and cash/debt are latest published proxies. Alphabet gains and the aggregate-class price proxy weaken the sparse peer comparison. No acquisition/control premium or future buyback windfall is included.

Prepared with disclosed Codex assistance. No securities transaction, Brightspace submission, hosted recording or confirmed GitHub publication has been performed by the application.

## October16 completion of items1-3

See docs/Initiation-Defense.pdf for explicit current-price acceptance and the proposed5% high-case valuation hurdle; docs/Edition-A-Current-Draft.pdf for an on-time AI-disclosed checkpoint candidate under student-reported permission; docs/Human-Locked-Exercise.pdf for the personal AI-off workflow. These do not claim a checkpoint receipt or a completed human exercise.
