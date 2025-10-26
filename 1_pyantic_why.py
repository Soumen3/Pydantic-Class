from pydantic import BaseModel


class Patient(BaseModel):
  name: str
  age: int
  weight: float


def insert_patient_data(patient: Patient):
  print(patient.name)
  print(patient.age)
  print("Patient data inserted successfully")


def update_patient_data(patient: Patient):
  print(patient.name)
  print(patient.age)
  print("Patient data updated successfully")



patient_info={
  "name":"nitish",
  "age":30,
  "weight": 40.65
}


patient1=Patient(**patient_info)
insert_patient_data(patient1)