patient = {
    "resourceType": "Patient",
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

print(patient) # Python Object 

import json
print(json.dumps(patient)) # JSON Object 