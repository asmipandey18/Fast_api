# import the fastapi class
from fastapi import FastAPI, Body, Path
import uvicorn
from pydantic import BaseModel, Field
from typing import List

# Create a fastapi instance(used by uvicorn to run the server)
app = FastAPI() 

# define a simple GET endpoint
# it means the roor (/) route for GET request

## Task 1 
@app.get("/")
def read_root():
    return{"message": "Hello Asmi pandey"}

## Task 2
## Develope a POST endpoint that accepts name and return a personalized greeting messages
@app.post("/greet")
def greet_user(name:str):
    return{"message": f"Hello,{name}"}

# ## path parameters
# @app.get("/hello/{name}")
# async def hello(name):
#     return {"name": name}

# @app.get("/hello/{name}/{age}")
# async def hello(name, age):
#     return {"name": name, "age": age}

# ## Query parameters
# @app.get("/hey")
# async def hey(name:str, age:int):
#     return {"name": name, "age": age}

# ## Path validation
# @app.get("/hello/{name}")
# async def hello(name:str=Path(..., min_length=3,max_length=10)):
#     return {"name": name}

# @app.get("/hello/{name}/{age}")
# async def hello(name:str=Path(..., min_length=3, max_length=10), age: int = Path(..., ge=1, le=100)):
#     return {"name": name, "age": age}



### Implementing pydantic model with fastapi
# class Student(BaseModel):
#     id: int
#     name: str
#     subjects: List[str] = []


# data = {
#     'id': 1,
#     'name': "Asmi pandey",
#     'subjects': ['ML','Full Stack']
# }

# s1 = Student(**data)

# print(s1)

# print(s1.model_dump())



## Basic Data validation
# from pydantic import BaseModel, ValidationError

# class BlogPost(BaseModel):
#     title: str
#     content: str

# try:
#     # Valid data
#     post_data = BlogPost(title="Introduction to Pydantic", 
#         content="Pydantic is a Python library for data validation.")
#     print(post_data)

#     # Corrected invalid data
#     invalid_post_data = BlogPost(title="123", content="42")
#     print(invalid_post_data)

# except ValidationError as e:
#     print("Validation error:", e)



## Parsing data with Pydantic
## Example: Data Parsing and Default Values
# class User(BaseModel):
#     username: str
#     email: str
#     age: int = 25  # Default value

# # Valid data
# user_data = User(username="john_doe", email="john@example.com")
# print(user_data.age)  # Output: 25 (default value)

# # Valid data with age specified
# user_data2 = User(username="jane_doe", email="jane@example.com", age=30)
# print(user_data2.age)  # Output: 30

# Invalid data
#invalid_user_data = User(username="jim_doe", email=123)
# This will raise a ValidationError for 'email' since it should be a string.



## pydantic model as request body
class Student(BaseModel):
    id: int
    name: str = Field(None, title="Nmae of the student", max_length=10)
    subjects: List[str] = []

@app.post("/student")
async def student_profile(s1: Student):
    return s1




# ## Example of FastAPI endpoint /student_profile that accepts student information as a payload.
# class StudentProfile(BaseModel):
#     name: str
#     phone: str
#     address: str
#     college_name: str
#     email: str
#     faculty: str
#     subjects: list[str]
#     marks: list[float]

# @app.post("/student_profile")
# async def student_profile(student: StudentProfile):
#     return student


# ## Task
# students = []

# # POST API: Add student details
# @app.post("/add_students")
# def add_students(student: dict = Body(...)):
#     students.append(student)
#     return {"message": "students added"}


# # GET API: Display added student details
# @app.get("/get_students")
# def get_students():
#     return students



if __name__ == "__main__":
    uvicorn.run("main:app",host = "127.0.0.1",port = 8000, reload=True)