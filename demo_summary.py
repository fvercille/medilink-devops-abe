import json
from medilink_contract import build_summary

# Sample input data described in the lab guide
patient = {"patient_id": "P-101", "name": "Jane Doe"}
appointments = [{"id": "A-1", "date": "2026-10-15"}]

# Calls the integration contract and prints formatted JSON
summary = build_summary(patient, appointments)
print(json.dumps(summary, indent=2))