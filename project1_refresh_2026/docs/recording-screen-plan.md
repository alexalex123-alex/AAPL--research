# Recording guide - updated after Alex's growth exercise

Use only project1_refresh_2026 for the active September2026 application. Use root dcf.py solely for the labeled historical changed-input exercise. Scripts are narration drafts; final transcripts must match the actual recordings. Timing below is a rehearsal budget, not observed video timestamps. Read at a natural pace and leave time for demonstrations. Follow the course's identity/webcam rules.

## Prepare the screens

Open these in advance: Research-Evolution.pdf, Edition-A-Current-Draft.pdf, any actual Brightspace receipt once it exists, partner-review-record.md, sources-and-normalization.md, initiation defense, the code editor and a terminal. In the terminal, change into the versioned repository's project1_refresh_2026 directory. Start the app with python run.py --serve --port 8766 and open http://127.0.0.1:8766 in a browser. Keep this server terminal running; use a SECOND terminal for tests. If port8766 already serves the active app, reuse it. Confirm the browser header says September14,2026 and the reference close333.08. Avoid earlier2025 tabs while discussing current values.

## Video1 - research evolution; maximum3:00

| Rehearsal time | Show | Explain |
|---|---|---|
|0:00-0:20|Active app heading or memo|Who you are, fund/no existing holding, decision and your initiate stance |
|0:20-0:50|Research-Evolution.pdf date/evidence table|Old2025 date versus2026 Siri evidence; why all inputs were refreshed. If checkpoint receipt exists, briefly show it and exact received Edition A. Otherwise accurately identify the candidate as unsubmitted |
|0:50-1:20|partner-review-record.md, actual feedback section|Jess questioned original0.57% FCFF growth as low; your answer and reassessment. Credit actual remarks only |
|1:20-2:15|Alex-Growth-Exercise.md and precommit/run JSON|Your prediction, pre-run commit4173681, original0.57% to1% test,90.66 to92.33, magnitude miss and actual buy-unchanged diagnosis. State AI-assisted technical execution |
|2:15-2:45|sources-and-normalization.md intangible correction and evolution record|One corrected AI output, division of human/AI ownership and remaining basis limits |

Aim for2:30-2:50; the318-word narration leaves room for short screen changes. Do not claim Edition A was received or that any personal exercise was AI-off unless genuine evidence supports it.

## Video2 - code and validation; maximum5:00

| Rehearsal time | Show | Explain |
|---|---|---|
|0:00-0:40|data/fact_ledger.json and sources-and-normalization.md|Source/filing dates and definitions; TTM annual+current9m-prior9m; June opening proxies |
|0:40-1:30|model.py: project and check_row|Category drivers -> statements -> economic FCFF; balance, cash and bridge checks; explicit intangible correction |
|1:30-2:15|model.py: value/dcf_path and duration_challenge|Five-year discounting, funded terminal growth, EV-equity/share bridge, alternative duration |
|2:15-3:00|Second terminal, command below, then final summary|Run all17 tests; explain known-answer, failure and direction checks; show real result, do not read every test name |
|3:00-3:25|docs/cold-run-log.txt|Fresh-environment run and identical saved results |
|3:25-4:30|docs/alex-growth-precommit.json and alex-growth-run.json; root dcf.py if needed|Original engine only; commit-before-run evidence, old/new units, predicted versus actual size, your diagnosis and decision. Separate your judgment from AI execution |
|4:30-4:45|Validation-and-AI-Use.pdf|Technical validity versus economic uncertainty; qualified AI-off/historical-engine scope |

Run from project1_refresh_2026:

    python -m unittest discover -s . -p "test_*.py" -v

Keep the preserved changed-input files unchanged. Do not rerun or recreate the original prediction while filming to imply a different chronology. Show its existing commit and saved outputs. Record actual video timestamps after recording.

## Video3 - committee defense; maximum5:00

| Rehearsal time | Show | Explain |
|---|---|---|
|0:00-0:40|App heading and causal cases|Initiate; date/currency/horizon;333.08 close, core73-254 and extended286-350; conditional regimes |
|0:40-1:25|App cases and five linked statements|AI thesis -> category growth/margins -> investment -> FCFF; assumptions are not Apple guidance |
|1:25-2:00|App enterprise-equity bridge and reverse expectations|Cash reserve, debt and share proxy; reverse expectations if time permits |
|2:00-2:35|App WACC control and grid|Note displayed original9.7241% WACC. Enter10.7241 and click Revalue stored operations: approximately129.02. Explain higher required return reduces value. Restore9.7241 and revalue to approximately147.09. Keep terminal growth2.5% and operating assumptions fixed |
|2:35-3:15|App duration table|High five-year case254; high15-extra-year fade350.48; long persistence and high returns required |
|3:15-3:50|Initiation-Defense.pdf entry table|Your acceptance at333.08; assistant-proposed5% valuation-upside hurdle,349.73 required; limited cushion and no annual return promise |
|3:50-4:35|App peers and downside table|Why methods disagree; no averaging; combined downside about61; adoption/cash-conversion reversal evidence |
|4:35-4:55|Memo committee ask or app headline|Clear initiate judgment with model disagreement, downside and required monitoring explicit |

After recording: generate actual transcripts, correct finance terms/numbers/names, use transcript-video-1.txt through transcript-video-3.txt, measure actual durations, add observed timestamp indices and verify unlisted links/instructional access. No draft file is a completed recording transcript.
