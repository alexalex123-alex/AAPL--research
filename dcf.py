"""Apple five-year FCFF DCF and reverse DCF (all dollars in USD millions).

Run with: python dcf.py
"""

# FY2025 starting values and base-case assumptions
STARTING_FCFF = 95_622.0
GROWTH_RATES = [0.0057] * 5
WACC = 0.0891
TERMINAL_GROWTH = 0.02
NON_OPERATING_CASH = 132_420.0
DEBT = 98_657.0
DILUTED_SHARES = 15_004.697

# Reverse-DCF target
TARGET_SHARE_PRICE = 326.00


def calculate_dcf(growth_rates, terminal_growth=TERMINAL_GROWTH):
    """Return DCF outputs for five annual FCFF growth rates."""
    if len(growth_rates) != 5:
        raise ValueError("Enter exactly five annual FCFF growth rates.")
    if terminal_growth >= WACC:
        raise ValueError("Terminal growth must be below WACC.")

    fcff = []
    previous_fcff = STARTING_FCFF
    for growth_rate in growth_rates:
        previous_fcff *= 1 + growth_rate
        fcff.append(previous_fcff)

    pv_explicit_fcff = sum(
        cash_flow / (1 + WACC) ** year
        for year, cash_flow in enumerate(fcff, start=1)
    )
    terminal_value_year_5 = fcff[-1] * (1 + terminal_growth) / (WACC - terminal_growth)
    pv_terminal_value = terminal_value_year_5 / (1 + WACC) ** 5
    enterprise_value = pv_explicit_fcff + pv_terminal_value
    equity_value = enterprise_value + NON_OPERATING_CASH - DEBT

    return {
        "fcff": fcff,
        "pv_explicit_fcff": pv_explicit_fcff,
        "terminal_value_year_5": terminal_value_year_5,
        "pv_terminal_value": pv_terminal_value,
        "enterprise_value": enterprise_value,
        "equity_value": equity_value,
        "value_per_share": equity_value / DILUTED_SHARES,
        "pv_terminal_value_share": pv_terminal_value / enterprise_value,
    }


def reverse_dcf_constant_growth(target_share_price=TARGET_SHARE_PRICE):
    """Solve for a constant five-year FCFF growth rate at the target price.

    WACC, terminal growth, net cash, and diluted shares are held at the inputs
    above. Bisection is used because the DCF value rises monotonically with FCFF
    growth over the tested range.
    """
    target_equity_value = target_share_price * DILUTED_SHARES
    target_enterprise_value = target_equity_value - NON_OPERATING_CASH + DEBT
    lower_growth, upper_growth = -0.50, 1.00

    for _ in range(100):
        midpoint = (lower_growth + upper_growth) / 2
        midpoint_value = calculate_dcf([midpoint] * 5)["enterprise_value"]
        if midpoint_value < target_enterprise_value:
            lower_growth = midpoint
        else:
            upper_growth = midpoint

    implied_growth = (lower_growth + upper_growth) / 2
    result = calculate_dcf([implied_growth] * 5)
    result["target_share_price"] = target_share_price
    result["target_equity_value"] = target_equity_value
    result["implied_fcff_growth"] = implied_growth
    return result


def implied_terminal_growth_at_base_case(target_share_price=TARGET_SHARE_PRICE):
    """Solve terminal growth if the original 0.57% FCFF growth is retained."""
    base_without_terminal = calculate_dcf(GROWTH_RATES, terminal_growth=0.0)
    target_enterprise_value = (
        target_share_price * DILUTED_SHARES - NON_OPERATING_CASH + DEBT
    )
    required_pv_terminal_value = (
        target_enterprise_value - base_without_terminal["pv_explicit_fcff"]
    )
    required_terminal_value = required_pv_terminal_value * (1 + WACC) ** 5
    year_5_fcff = base_without_terminal["fcff"][-1]
    return (required_terminal_value * WACC - year_5_fcff) / (
        required_terminal_value + year_5_fcff
    )


def print_base_dcf(result):
    """Print the standard 12-line DCF output."""
    for year, cash_flow in enumerate(result["fcff"], start=1):
        print(f"FCFF Year {year}: {cash_flow:,.4f}")
    print(f"PV of explicit FCFF: {result['pv_explicit_fcff']:,.4f}")
    print(f"Terminal value, Year 5: {result['terminal_value_year_5']:,.4f}")
    print(f"PV of terminal value: {result['pv_terminal_value']:,.4f}")
    print(f"Enterprise value: {result['enterprise_value']:,.4f}")
    print(f"Equity value: {result['equity_value']:,.4f}")
    print(f"Value per share: {result['value_per_share']:,.4f}")
    print(f"PV of TV / enterprise value: {result['pv_terminal_value_share']:.4%}")


def print_reverse_dcf(result):
    """Print reverse-DCF outputs at the target share price."""
    print(f"Target share price: ${result['target_share_price']:,.2f}")
    print(f"Target equity value: {result['target_equity_value']:,.4f}")
    print(f"Target enterprise value: {result['enterprise_value']:,.4f}")
    print(f"Implied annual FCFF growth: {result['implied_fcff_growth']:.4%}")
    for year, cash_flow in enumerate(result["fcff"], start=1):
        print(f"Reverse DCF FCFF Year {year}: {cash_flow:,.4f}")
    print(f"PV of explicit FCFF: {result['pv_explicit_fcff']:,.4f}")
    print(f"Terminal value, Year 5: {result['terminal_value_year_5']:,.4f}")
    print(f"PV of terminal value: {result['pv_terminal_value']:,.4f}")
    print(f"PV of TV / enterprise value: {result['pv_terminal_value_share']:.4%}")


def main():
    base_case = calculate_dcf(GROWTH_RATES)
    reverse_case = reverse_dcf_constant_growth()

    print("BASE-CASE DCF")
    print_base_dcf(base_case)
    print("\nREVERSE DCF")
    print_reverse_dcf(reverse_case)
    print(
        "Implied terminal growth if base 0.57% FCFF growth is retained: "
        f"{implied_terminal_growth_at_base_case():.4%}"
    )


if __name__ == "__main__":
    main()
