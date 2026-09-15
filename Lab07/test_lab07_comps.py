"""Run with: python -m unittest test_lab07_comps.py"""
import contextlib
import io
import unittest
from lab07_comps import TARGET, PEERS, run

def output(target=TARGET, peers=PEERS):
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        run(target, peers)
    return buffer.getvalue()

class CalculatorChecks(unittest.TestCase):
    def test_frozen_case_and_unrounded_change(self):
        result = output()
        for expected in ('10.037825x', '11.450149x', '10.743987x',
                         '$215.81-$246.18', 'Median implied price: $231.00',
                         'Remove GPI: $215.81; change $-15.18'):
            self.assertIn(expected, result)

    def test_duplicates_and_target(self):
        result = output(peers=PEERS + [{'ticker': ' an ', 'price': 1, 'eps': 1}, TARGET])
        self.assertIn('duplicate excluded', result)
        self.assertIn('target excluded', result)
        self.assertIn('Median implied price: $231.00', result)

    def test_single_and_no_peers(self):
        self.assertIn('Single-peer reference estimate: $215.81; no range', output(peers=PEERS[:1]))
        self.assertIn('Remove AN: no estimate', output(peers=PEERS[:1]))
        self.assertIn('No usable peers', output(peers=[]))

    def test_invalid_values(self):
        for value in (None, 0, -1, 'NaN', 'Infinity', 'bad'):
            for field in ('price', 'eps'):
                peer = dict(PEERS[0], **{field: value})
                self.assertIn('No usable peers', output(peers=[peer]))
        self.assertIn('Target implied prices: not meaningful', output(target=dict(TARGET, eps=0)))
        result = output(target=dict(TARGET, price=None))
        self.assertIn('Target observed P/E: not meaningful', result)
        self.assertIn('Median implied price: $231.00', result)

if __name__ == '__main__':
    unittest.main()
