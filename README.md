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


