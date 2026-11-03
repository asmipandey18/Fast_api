from fastapi import APIRouter, Body

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
