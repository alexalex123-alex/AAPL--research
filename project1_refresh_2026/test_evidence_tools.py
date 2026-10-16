"""Synthetic utility checks; never a student's locked prediction or real review."""
import contextlib,io,json,tempfile,unittest
from pathlib import Path
from unittest.mock import patch
import locked_test
class EvidenceToolTests(unittest.TestCase):
    def test_prepare_records_without_execution(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'synthetic-precommit.json'
            answers=['YES','wacc','0.10','fraction','SYNTHETIC direction fixture','SYNTHETIC size fixture','SYNTHETIC decision fixture','AUTOMATED FIXTURE - NOT A HUMAN']
            with patch.object(locked_test,'P',path),patch('builtins.input',side_effect=answers),patch.object(locked_test.model,'project',side_effect=AssertionError('No execution before precommit')),contextlib.redirect_stdout(io.StringIO()):
                locked_test.prepare()
            record=json.loads(path.read_text()); self.assertIn('protected_file_hashes',record); self.assertIn('expected_rough_size',record)
    def test_existing_prediction_cannot_be_overwritten(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'synthetic.json';path.write_text('fixture')
            with patch.object(locked_test,'P',path),self.assertRaises(SystemExit):locked_test.prepare()
            self.assertEqual(path.read_text(),'fixture')
    def test_nonfinite_change_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'synthetic.json'
            answers=['YES','wacc','nan','fraction','SYNTHETIC','SYNTHETIC','SYNTHETIC','AUTOMATED FIXTURE']
            with patch.object(locked_test,'P',path),patch('builtins.input',side_effect=answers),self.assertRaises(SystemExit):locked_test.prepare()
            self.assertFalse(path.exists())
    def test_provenance_hashes_cover_model_inputs_and_helper(self):
        hashes=locked_test.hashes()
        self.assertEqual(set(hashes),{'model.py','data/inputs.json','locked_test.py'})
        self.assertTrue(all(len(v)==64 for v in hashes.values()))
if __name__=='__main__':unittest.main(verbosity=2)
