from pydantic import BaseModel

class StudentCreateSchema(BaseModel):
    first_name: str
    last_name: str

    class ConfigDict:
        json_schema_extra = {
            "example": {
                "first_name": "Jerzetta",
                "last_name": "Kłosińska",
            }
        }

class StudentUpdateSchema(BaseModel):
    first_name: str
    last_name: str

    class ConfigDict:
        json_schema_extra = {
            "example": {
                "first_name": "Updated-Jerzetta",
                "last_name": "Updated-Kłosińska",
            }
        }

class Student(BaseModel):
    id: int
    first_name: str
    last_name: str
