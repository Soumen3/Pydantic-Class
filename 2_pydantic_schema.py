from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
  name:Annotated[str, Field(max_length=50, min_length=1, description="The name of the patient", examples=['Nitish', 'Akash'])]  # Name with max length 50 and min length 1
  email:EmailStr
  link:Optional[AnyUrl] = None            # Optional field for personal website
  age:Annotated[int, Field(gt=0)]         # Age must be greater than 0
  weight:Annotated[float, Field(gt=0, strict=True)]    # Weight must be greater than 0
  married:Annotated[bool, Field(default=False)]  # Default value set to False
  allergies:Annotated[Optional[List[str]], Field(default=None, max_length=5)]    # Optional field for allergies
  contact_details:Dict[str, str]


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
  "age":30,
  "weight": 40.65,
  "married": True,
  "allergies": ["pollen", "nuts"],
  "contact_details": {"email": "nitish@example.com", "phone": "1234567890"}
}

patient1=Patient(**patient_info)

update_patient_data(patient1)
