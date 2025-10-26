from pydantic import BaseModel, EmailStr, AnyUrl, Field, model_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name:str
    email:EmailStr
    age:int
    weight:float
    married:bool
    allergies:List[str]
    contact_details:Dict[str, str]


    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Emergency contact is required for patients over 60 years old.')
        return model




def show_patient_data(patient: Patient):
    print(f"Name: {patient.name}")
    print(f"Email: {patient.email}")
    print(f"Age: {patient.age}")
    print(f"Weight: {patient.weight}")
    print(f"Married: {patient.married}")
    print(f"Allergies: {patient.allergies}")
    print(f"Contact Details: {patient.contact_details}")


patient_info={
    "name":"nitish",
    "email":"nitish@example.com",
    "link":"https://nitish.com",
    "age":'70',
    "weight": 40.65,
    "married": True,
    "allergies": ["pollen", "nuts"],
    "contact_details": {"email": "nitish@example.com", "phone": "1234567890"}
}

patient1=Patient(**patient_info)

show_patient_data(patient1)
