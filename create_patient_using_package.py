import json
from fhir.resources.patient import Patient

patient_obj = {
    "resourceType": "Patient",
    # "test": "dummy data",
    "name": [
        {
            'use': 'official',
            'family': 'Tripathi',
            "given": [
                "Mayank"
            ]
        }
    ],
    'gender': "male"
}

patient = Patient(**patient_obj)

print(f"\nPatient Resource with FHIR Spec: \n{patient}") # FHIR Spec.

print("\n--------------\n")
print(f"Patient data in JSON Format: \n{patient.json()}") # JSON Object