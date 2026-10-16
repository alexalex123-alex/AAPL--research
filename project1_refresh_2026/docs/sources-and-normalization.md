# Sources, dates and normalization

Active valuation September 14,2026 close; USD. Retrieved/assembled in October 2026. Source hashes: data/source_manifest.json. Structured observations: data/fact_ledger.json. All chosen financial facts satisfy filed<=2026-09-14. Raw snapshots may contain later observations; the selection filter, not the whole raw file, defines the information set.

## Financial base and basis

Latest available Apple filing: June27,2026 Form 10-Q, filedJuly31,2026, https://www.sec.gov/Archives/edgar/data/320193/000032019326000020/aapl-20260627.htm . No FY2026 annual results were available by the valuation cutoff. TTM flows = FY2025 + first9months2026 - first9months2025. Same-period prior TTM is reconstructed analogously. The June balance sheet is the latest published opening proxy, not a September daily roll-forward.

Income: TTM sales466,823m, EBIT154,859m, NI128,930m. CF: CFO146,724m, CFI-21,398m, CFF-122,051m. Opening cash36,269m plus those flows equals39,544m ending cash. Reported histories remain unchanged by normalization.

The current filing's balance-sheet p.3 separately lists intangibles20,342m and other noncurrent assets77,557m. The model aggregates them to 97,899m. Initial omission of the new intangible presentation caused a20,342m balance-sheet failure; the line was explicitly added from the filing rather than plugged. The generic SEC intangible tag returned a different amount25,417m; it is not used for this balance-sheet line. This source/definition discrepancy is preserved and qualified. Assets383,266m equal liabilities275,746m plus equity107,520m.

Narrow operating WC = trade receivables + vendor receivables + inventory - AP - deferred revenue. Other current assets/liabilities are frozen in forecasts because the current quarterly filing does not supply enough tax detail for a clean recurring split. This differs from the older model's definition and avoids extrapolating a tax-payable swing. It also may omit genuine operating investment; stress the receivable/inventory assumptions. Year-over-year narrow WC increase2,529m is a balance-based modeling reference, not the reported CFS working-capital movement.

## Normalized base and investment

Reported TTM Products margin 39.13% includes effects the10-Q attributes to mix and tariff refunds, partly offset by higher costs (MD&A pp.15-16). Refund amount was not independently isolated. A normalized38% Products margin is therefore an explicit prudential judgment, not a falsely precise one-time adjustment. It reduces reported EBIT by 3,904.9m to 150,954.1m. Tax normalized to 18%; normalized NOPAT123,782.4m. The normalized FCFF reference is120,171.2m after D&A, investment, narrow WC and assumed replacement of other amortized assets. This bridge is not a restated audited cash-flow statement.

TTM D&A13,100m is allocated between PP&E and other amortization using the FY2025 approximate8,000/11,698 PP&E share. That allocation and replacement spending are judgments requiring challenge. Forecast PP&E capex4% of sales in base exceeds TTM reported capex10,041/466,823=2.15%; R&D10% exceeds the TTM9.19%, reflecting incremental AI investment/cost risk. D&A is already included in margins and is not deducted twice from EBIT. SBC is added back for CFO and credited to equity, then reversed from economic FCFF.

## Market observations and WACC

Yahoo historical unadjusted closes on September 14: AAPL333.08, MSFT505.41, GOOGL349.39. Adjusted closes are used only for return estimation. Source example: https://query1.finance.yahoo.com/v8/finance/chart/AAPL ; exact timestamp-bounded URLs and retrieved files are in the manifest. Opening cash39,544m + marketable securities22,855m+84,118m =146,517m; reserve30,000m leaves116,517m. Interest-bearing debt1,997+11,007+71,340=84,344m.

July17 published basic shares14,594.180m plus55.41625m TTM incremental dilution proxy =14,649.59625m valuation shares. The incremental proxy uses FY2025 diluted-minus-basic plus0.75 times the difference between current and prior nine-month weighted-average diluted-minus-basic shares. It is approximate, not an exact September 14 diluted count; annual and quarterly weighted averages are not shares at a point in time.

Treasury official10-year par yield4.97% on September 14: https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value=202609 . OLS beta 1.07494 uses59 monthly adjusted return observations against SPY, completed months throughAugust2026. Selected beta 1.075, ERP 4.5%, marginal debt cost6%, forecast tax 18%; market equity weights and carrying debt proxy give WACC 9.7241%. ERP and marginal debt cost are judgments, not fresh market quotes. Alex reports using Yahoo for earlier checks; exact historical fields he used are unconfirmed.

## Siri and event timing

September 14,2026 release: https://www.apple.com/newsroom/2026/09/siri-ai-a-profoundly-more-capable-and-personal-assistant-is-here/ . The date is verified from Apple's page; same-day publication time before market close is an explicit condition, not independently timestamped. Direct archival download returned403, while the web-reading tool accessed the official page. No fabricated raw snapshot is included. The announcement supports an adoption hypothesis, not observed incremental revenue, paid subscription pricing or a guaranteed upgrade cycle. June2026 introduction is context available before the cutoff; October 2026/other later evidence is excluded.

## Peer definitions

Policy transferred from the earlier preselected Microsoft/Alphabet set: profitable USD-reporting global ecosystems, qualified for business mix, regulation and capital needs. No peer chosen by preferred multiple. September 14 prices pair with latest published June2026 accounts; Microsoft uses FYendedJune2026 and Alphabet TTMJune2026. EV includes interest-bearing debt, subtracts cash/liquid marketable securities, and leaves leases operating; P/E uses aggregate equity/GAAP NI. Alphabet gains materially inflate GAAP NI and weaken P/E; aggregate classes priced at ClassA remain a proxy. No control/synergy transaction multiple is admitted.
