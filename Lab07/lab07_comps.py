"""Lab 07 Asbury P/E exercise. Standard library only; no data fetching.

Editable frozen inputs are below. Prices: December 31, 2024 closes.
EPS: subsequently published FY2024 total GAAP diluted EPS.
This is a retrospective training comparison, not an as-of-date valuation.
"""
from decimal import Decimal, InvalidOperation, localcontext
from statistics import median

TARGET = {'ticker': 'ABG', 'price': '243.03', 'eps': '21.50'}
PEERS = [
    {'ticker': 'AN', 'price': '169.84', 'eps': '16.92'},
    {'ticker': 'GPI', 'price': '421.48', 'eps': '36.81'},
]

def positive(value):
    """Return a finite positive Decimal, or None for unusable input."""
    try:
        number = Decimal(str(value))
    except (InvalidOperation, ValueError):
        return None
    return number if number.is_finite() and number > 0 else None

def symbol(row):
    return str(row.get('ticker') or '').strip().upper()

def evaluate(target, peers):
    """Deduplicate by ticker (first entry wins), excluding target and bad data."""
    valid, notes, seen = [], [], set()
    for row in peers:
        ticker = symbol(row)
        if not ticker:
            notes.append('Missing peer ticker: not meaningful; excluded.')
            continue
        if ticker == symbol(target):
            notes.append(f'{ticker}: target excluded from peers.')
            continue
        if ticker in seen:
            notes.append(f'{ticker}: duplicate excluded (first entry retained).')
            continue
        seen.add(ticker)
        price, eps = positive(row.get('price')), positive(row.get('eps'))
        if price is None or eps is None:
            notes.append(f'{ticker}: P/E not meaningful (missing/nonpositive/nonfinite price or EPS).')
            continue
        valid.append((ticker, price / eps))
    return valid, notes

def run(target=TARGET, peers=PEERS):
    # Keep unrounded values for all calculations; round only formatted output.
    with localcontext() as ctx:
        ctx.prec = 50
        price, eps = positive(target.get('price')), positive(target.get('eps'))
        valid, notes = evaluate(target, peers)
        print('LAB 07 - ASBURY RETROSPECTIVE TRAINING COMPARISON')
        print('2024-12-31 closing prices / subsequently reported FY2024 GAAP diluted EPS')
        print('USD per common share. No cash/debt bridge.')
        print(f'Target: {symbol(target)}')
        if price is None or eps is None:
            print('Target observed P/E: not meaningful (invalid price or EPS).')
        else:
            print(f'Target observed P/E: {price / eps:.6f}x')
        for note in notes:
            print(note)
        for ticker, multiple in valid:
            print(f'{ticker} P/E: {multiple:.6f}x')
        if not valid:
            print('No usable peers. No implied estimate or range.')
            return
        multiples = [multiple for _, multiple in valid]
        middle = median(multiples)
        print(f'Peer median P/E: {middle:.6f}x')
        if eps is None:
            print('Target implied prices: not meaningful (invalid target EPS).')
            for ticker, _ in valid:
                print(f'Remove {ticker}: no estimate; dollar change not meaningful.')
            return
        full_value = middle * eps
        if len(valid) == 1:
            print(f'Single-peer reference estimate: ${full_value:.2f}; no range.')
        else:
            print(f'Minimum implied price: ${min(multiples) * eps:.2f}')
            print(f'Median implied price: ${full_value:.2f}')
            print(f'Maximum implied price: ${max(multiples) * eps:.2f}')
            print(f'Implied range: ${min(multiples) * eps:.2f}-${max(multiples) * eps:.2f}')
        if price is None:
            print('Comparison with target market price: not meaningful (invalid target price).')
        else:
            print(f'Median-implied minus target close: ${full_value - price:+.2f}')
        for ticker, _ in valid:
            remaining = [multiple for name, multiple in valid if name != ticker]
            if not remaining:
                print(f'Remove {ticker}: no estimate; no usable peers remain.')
                continue
            value = median(remaining) * eps
            label = 'single-peer reference; no range' if len(remaining) == 1 else 'remaining peer median'
            print(f'Remove {ticker}: ${value:.2f}; change ${value - full_value:+.2f}; {label}.')

if __name__ == '__main__':
    run()
