import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.students

student_collection_elevatex = database.get_collection("student_collection_elevatex")

# we need to create a helper function for parsing the results from database query into Pthon Dict

def student_helper(student) -> dict:
    return {
        "id": str(student["_id"]),
        "fullname": student["fullname"],
        "email": student["email"],
        "course_of_study": student["course_of_study"],
        "year": student["year"],
        "GPA": student["gpa"]
    }

# Retrieve all student present in the Database
async def retrieve_students():
    students = []
    async for student in student_collection_elevatex.find():
        students.append(student_collection_elevatex(student))
    return students

# Add a new student into the database
async def add_student(student_data: dict) -> dict:
    student = await student_collection_elevatex.insert_one(student_data)
    new_student = await student_collection_elevatex.find_one({"_id": student.inserted_id})
    return student_helper(new_student)

# Retrieve a student with a matching ID
async def retrieve_student(id: str) -> dict:
    student = await student_collection_elevatex.find_one({"_id":ObjectId(id)})
    if student:
        return student_helper(student)

# Update a student with a matching id
async def update_student(id: str, data: dict):
    # Return False if an empty request body is sent

    if len(data) < 1:
        return False

    student = await student_collection_elevatex.find_one({"_id":ObjectId(id)})
    if student:
        update_student = await student_collection_elevatex.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if update_student:
            return True
        return False

# Delete a student from the database
async def delete_student(id: str):
    student = await student_collection_elevatex.find_one({"_id": ObjectId}(id))
    if student:
        await student_collection_elevatex.delete_one({"_id": ObjectId(id)})
        return  True