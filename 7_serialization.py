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
    gender:str = "male"
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
    # "gender":"male",
    "age":30,
    "address": address1
}

patient1=Patient(**patient_info)

# show_patient_data(patient1)

temp=patient1.model_dump()
print(temp)
print(type(temp),end="\n\n")

temp_json=patient1.model_dump_json()
print(temp_json)
print(type(temp_json),end="\n\n")

temp_from_json=Patient.model_validate_json(temp_json)
print(temp_from_json)
print(type(temp_from_json),end="\n\n")

temp_exclude=patient1.model_dump(exclude={'address'})
print(temp_exclude)
print(type(temp_exclude),end="\n\n")

temp_exclude2=patient1.model_dump(exclude={'address': {'street', 'city'}})
print(temp_exclude2)
print(type(temp_exclude2),end="\n\n")

temp_exclude3=patient1.model_dump(exclude_unset=True)
print(temp_exclude3)
print(type(temp_exclude3),end="\n\n")

temp_include=patient1.model_dump(include={'name', 'age'})
print(temp_include)
print(type(temp_include),end="\n\n")

temp_include2=patient1.model_dump(include={'address': {'city', 'country'}})
print(temp_include2)
print(type(temp_include2),end="\n\n")