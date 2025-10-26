from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

  name:str
  email:EmailStr
  age:int
  weight:float
  married:bool
  allergies:List[str]
  contact_details:Dict[str, str]

  @field_validator('email')
  def email_validator(cls, value):
    valid_domains = ['example.com', 'test.com']
    domain = value.split('@')[-1]
    if domain not in valid_domains:
      raise ValueError(f'Email domain {domain} is not allowed.')
    return value
  
  @field_validator('name')
  @classmethod
  def transform_name(cls, value):
    return value.upper()

  @field_validator('age', mode='after')
  @classmethod
  def validate_age(cls, value):
    if not (0 < value <= 100):
      raise ValueError('Age must be greater than 0 and less than or equal to 100.')
    return value
  



def insert_patient_data(patient: Patient):
  print(patient.name)
  print(patient.age)
  print("Patient data inserted successfully")


def update_patient_data(patient: Patient):
  print(patient.name)
  print(patient.age)
  print(patient.weight)
  print("Patient data updated successfully")



patient_info={
  "name":"nitish",
  "email":"nitish@example.com",
  "link":"https://nitish.com",
  "age":'30',
  "weight": 40.65,
  "married": True,
  "allergies": ["pollen", "nuts"],
  "contact_details": {"email": "nitish@example.com", "phone": "1234567890"}
}

patient1=Patient(**patient_info)

update_patient_data(patient1)
