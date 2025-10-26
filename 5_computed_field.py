from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

class Patient(BaseModel):

    name:str
    email:EmailStr
    age:int
    weight:float # in kg
    height:float # in meters
    married:bool
    allergies:List[str]
    contact_details:Dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float:
        """Calculate Body Mass Index (BMI)"""
        return round(self.weight / (self.height ** 2), 2)





def show_patient_data(patient: Patient):
    print(f"Name: {patient.name}")
    print(f"Email: {patient.email}")
    print(f"Age: {patient.age}")
    print(f"Weight: {patient.weight}")
    print(f"Height: {patient.height}")
    print(f"BMI: {patient.bmi}")
    print(f"Married: {patient.married}")
    print(f"Allergies: {patient.allergies}")
    print(f"Contact Details: {patient.contact_details}")


patient_info={
    "name":"nitish",
    "email":"nitish@example.com",
    "link":"https://nitish.com",
    "age":'70',
    "weight": 60.65,
    "height": 1.75,
    "married": True,
    "allergies": ["pollen", "nuts"],
    "contact_details": {"email": "nitish@example.com", "phone": "1234567890"}
}

patient1=Patient(**patient_info)

show_patient_data(patient1)
