# import json # Not required.
from fhir.resources.patient import Patient
from fhir.resources.humanname import HumanName

patient = Patient() 
patient.name = [ HumanName(given = ["Mayank"], family = "Tripathi")]

print("FHIR Patient Resource created using Primitives \n")
print(patient.model_dump_json(indent = 2))

print(f"Adding Gender and Email \n")

patient.gender = "male"

from fhir.resources.contactpoint import ContactPoint

patient.telecom = [
    ContactPoint(system="email", value = "mayank_learn@fhir.com")
]

print(patient.model_dump_json(indent = 2))
