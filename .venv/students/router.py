from fastapi import APIRouter, HTTPException
from .schema import Student, StudentCreateSchema, StudentUpdateSchema
from .storage import get_students_storage


router = APIRouter()

@router.get("/")
async def get_students():
    return get_students_storage()

@router.post("/")
async def create_student(student: StudentCreateSchema):
    students_storage = get_students_storage()
    id = len(students_storage) + 1
    new_student = Student(id=id, **student.dict())
    students_storage[id] = new_student
    return new_student

@router.get("/{student_id}")
async def get_student(student_id: int):
    students_storage = get_students_storage()
    if student_id not in students_storage:
        raise HTTPException(status_code=404, detail="Student not found")
    return students_storage[student_id]

@router.put("/{student_id}")
async def update_student(student_id: int, student_update: StudentUpdateSchema):
    students_storage = get_students_storage()
    if student_id not in students_storage:
        raise HTTPException(status_code=404, detail="Student not found")
    students_storage[student_id].first_name = student_update.first_name
    students_storage[student_id].last_name = student_update.last_name
    return students_storage[student_id]
