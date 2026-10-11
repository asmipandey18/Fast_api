# import the fastapi class
from fastapi import FastAPI, Body, Path
import uvicorn
from pydantic import BaseModel

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

@app.get("/hello/{name}/{age}")
async def hello(name:str=Path(..., min_length=3, max_length=10), age: int = Path(..., ge=1, le=100)):
    return {"name": name, "age": age}

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