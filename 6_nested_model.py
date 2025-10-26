from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str
    country: str

class Patient(BaseModel):

    name:str
    gender:str
    age:int
    address: Address



address_dict={
    "street": "123 Main St",
    "city": "Springfield",
    "state": "IL",
    "zip_code": "62701",
    "country": "USA"
}

address1 = Address(**address_dict)

def show_patient_data(patient: Patient):
    print(f"Name: {patient.name}")
    print(f"Gender: {patient.gender}")
    print(f"Age: {patient.age}")
    print(f"Address: {patient.address}")

patient_info={
    "name":"nitish",
    "gender":"male",
    "age":30,
    "address": address1
}

patient1=Patient(**patient_info)

show_patient_data(patient1)
