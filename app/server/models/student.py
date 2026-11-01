from pydantic import BaseModel, Field, EmailStr



class StudentSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    course_of_study: str = Field(...)
    year: int = Field(..., gt=0, le=4)
    gpa: float = Field(..., ge=0, le=4.0)

    # It validate the email string, eg asmipandey@abc.com correct, else asmi.com // error
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "fullname": "Asmi Pandey",
                    "email": "asmipandey@example.com",
                    "course_of_study": "BCA",
                    "year": 3,
                    "gpa": 3.8
                }
            ]
        }
    }

class UpdateStudentModel(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    course_of_study: str = Field(...)
    year: int = Field(..., gt=0, le=4)
    gpa: float = Field(..., ge=0, le=4.0)

    # It validate the email string, eg asmipandey@abc.com correct, else asmi.com // error
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "fullname": "Asmi Pandey",
                    "email": "asmipandey@example.com",
                    "course_of_study": "BCA",
                    "year": 3,
                    "gpa": 3.8
                }
            ]
        }
    }

def ResponseModel(data, message):
    return {
        "data": (data),
        "code": 200,
        "message": message
    }

def ErrorResponseModel(error, code, message):
    return{
        "error": error,
        "code": code,
        "message": message
    }
