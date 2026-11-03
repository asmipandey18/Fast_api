from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.database import (
    add_student,
    delete_student,
    retrieve_student,
    retrieve_students,
    update_student
)

from app.server.models.student import (
    ErrorResponseModel,
    ResponseModel,
    StudentSchema,
    UpdateStudentModel
)

router = APIRouter()

# api to create a new student
@router.post("/", response_description="Student data added into the database")
async def add_student_data(student: StudentSchema = Body(...)):
    student = jsonable_encoder(student)
    new_student = await add_student(student)
    return ResponseModel(new_student, "Student added successfully")


# api to fetch all students
@router.get("/", response_description="Student retrieved")
async def get_students():
    students = await retrieve_students()
    if students:
        return ResponseModel(students, "Students data retrieved successfully")
    return ResponseModel(students, "Empty list returned")

# api to fetch student by id
@router.get("/{id}", response_description="Student data retrieved")
async def get_student_data(id: str):
    student = await retrieve_student(id)
    if student:
        return ResponseModel(student, "Student data is fetched sucessfully")
    return ErrorResponseModel("An error occured", 400, "Student doesn't exist")


# # api to update student details
# @router.put("/{id}", response_description="Student data is Updated sucessfully")
# async def update_student_data(id: str, req:UpdateStudentModel = Body(...)):
#     req = {}


# api to delete student by id 
@router.delete("/{id}", response_description="Student data deleted from the database")
async def delete_student_data(id: str):
    deleted_student = await delete_student(id)
    if deleted_student:
        return ResponseModel(
            "Student with ID: {} deleted". format(id), "Student deleted successfully"
        )
    return ErrorResponseModel(
        "An error occured", 404, "Student with id {0} doesn't exist".format(id)
    )

