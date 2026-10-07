import unittest
from medilink_contract import build_summary


class TestMedilinkContract(unittest.TestCase):
    def test_summary_preserves_required_public_contract(self):
        patient = {"patient_id": "P-100", "name": "Alice"}
        appointments = []
        result = build_summary(patient, appointments, "active")

        self.assertIn("patient", result)
        self.assertIn("appointments", result)
        self.assertIn("clinic_status", result)
        self.assertEqual(result["clinic_status"], "ACTIVE")

    def test_invalid_patient_raises_value_error(self):
        with self.assertRaises(ValueError):
            build_summary("not-a-dict", [])


if __name__ == "__main__":
    unittest.main()