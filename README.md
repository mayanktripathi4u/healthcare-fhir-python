# Healthcare FHIR with python
I am new to FHIR (Fast Healthcare Interoperability Resources), and here I am exploring what FHIR is, and how I can use Python to interact with FHIR resources.

So FHIR is actually a standard by HL7 (Health Level 7).

Will be using FHIR R4 Version and [official document for R4](https://hl7.org/fhir/R4/documentation.html).

FHIR has several versions, with the most mature ones being **R4** (Release 4) and **R5** (Release 5). R4 is widely adopted and considered a stable standard. R5 is newer, with more resources and is still under development. Older versions like STU3 and DSTU2 are also in use, but are less commonly used in new implementations. 

There is also a FHIR CI-Build refers to the continuous integration build process for the FHIR (Fast Healthcare Interoperability Resources) specification, which is a standard for exchanging healthcare information. It's essentially an automated system that builds and tests the latest version of FHIR as changes are made to the specification. 
FHIR **R6** is in Draft mode as of today (July 2025).
<img width="1159" height="382" alt="image" src="https://github.com/user-attachments/assets/98d67dee-298f-4fc6-bae5-3d839e8de4a2" />

When working with Python, I will start with library `fhir.resources`.

Follow along with me in this journey.

## Create Virtual Env.
Will create a Virtual Env specific for our FHIR related work, this is just so that I don't install dependencies globally, and like mess with my other projects using Python Interpreter.


```bash
python -m venv .fhir-venv

source .fhir-venv/bin/activate
```

Try to use same version as `3.13.2` of Python, so that there is no issues, when using the same code.

```bash
python --version
```

Install the Python Library for FHIR
```sh
pip install fhir.resources
```

## Start with Sample Patient
To create a Patient record, there are various ways I could do like in `.txt`, `.csv`, `.xls` or in any of the Relational / SQL Database or No-SQL Database. However, here the aim is to create a FHIR standard Patient resource with Python, which would have same or similar information as what we have in other existing formats.

Now the simplest answer is actually, I can just create a JSON by visiting the FHIR documentation and referencing the JSON sample for a Patient. Writing the JSON data in Python is easy and I literally just have to do `resourceType: Patient` and then take a look at the field (like name, address, DOB, gender, email, phone etc) from existing source and manually create by understanding the spec, and follow the documentation. 

Example below:
`create_patient_manually.py`
```python
patient = {
    "resourceType: "Patient",
    "name": [
        {
            "use": "official",
            "family": "Tripathi",
            "given": [
                "Mayank"
            ]
        }
    ],
    "gender": "male"
}

print(patient) # Python Object

import json
print(json.dump(patient)) # JSON Object

```

This is quite an easy way to get started. However its hard to keep it up to make sure we are writing a valid JSON and the resource created manually not always goign to conform to the FHIR spec.

So its good to have something where we can sort of get that confidence that we always going to create a FHIR resource. This is where Python package like `fhir.resources` comes in. There would be more, which I will be learning slowly and adding here soon.

We already installed the package earlier, lets actually use it, and create the same resource if we did it using this package.

Refer [create_patient_using_package.py](./create_patient_using_package.py), where we make <font color="#ff0000">use of the package and Patient Object</font>, and observe the output, which indicates that now the Patient Resource we created is conform with FHIR spec, and the field which we did not passed were included too with value as None. If there is any mandatory value it will ask. This is actually quite significant because now we have a validation built in. 

Try yourself, by adding an extra field which is not FHIR standard (does not exists in FHIR Spec), something like `"test": "dummy data"`. It will error out with reason extra inputs are not permitted. 
```sh
 Extra inputs are not permitted [type=extra_forbidden, input_value='dummy data', input_type=str]
 ```

We have strong validation going here, and this library can help us ensure that our resources are always valid.

There is an alternate way to create this Patient Resource using the <font color="#ff0000">primitives</font> that we have with the package. Refer [Create Patient Using Primitives](./create_patient_using_primitives.py).

# Play around the FHIR Resource Library
Refer [Jupyter NB](./playing_with_fhir_resource_package.ipynb)

# Post the Patient FHIR Resource to real FHIR Server
Excited to extend the journey, and learn to post the patient resource we created to a real FHIR server.

Will have to first import `requests` library (Make sure to install it if not already.), which will help us with the HTTP connection and the HTTP request. 
[For full code refer](./playing_with_fhir_resource_package.ipynb)
