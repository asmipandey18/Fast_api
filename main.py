# import the fastapi class
from fastapi import FastAPI, Body
import uvicorn
from pydantic import BaseModel

# Create a fastapi instance

app = FastAPI() 

#define a simple GET endpoint
 
## Task 1 
@app.get("/")
def read_root():
    return{"message": "Hello Asmi pandey"}

# # Task 2
# #
@app.post("/greet")
def greet_user(name:str):
    return{"message": f"Hello,{name}"}

## Task3

students = []

# POST API: Add student details
@app.post("/add_students")
def add_students(student: dict = Body(...)):
    students.append(student)
    return {"message": "students added"}


# GET API: Display added student details
@app.get("/get_students")
def get_students():
    return students



if __name__ == "__main__":
    uvicorn.run("main:app",host = "127.0.0.1",port = 8000, reload=True)