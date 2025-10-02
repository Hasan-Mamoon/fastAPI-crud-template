from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.database.session import get_session
from app.schemas.student import StudentCreate, StudentRead, StudentUpdate, StudentDelete
from app.core.crud import student as crud_student

router = APIRouter(prefix="/students", tags=["students"])

@router.get("/students", response_model=list[StudentRead])
def read_students(session: Session = Depends(get_session)):
    return crud_student.get_all_students(session)

@router.post("/add-students", response_model=StudentRead)
def create_student(new_student: StudentCreate, session: Session = Depends(get_session)):
    return crud_student.create_student(session, new_student)

@router.patch("/edit-student", response_model=StudentRead)
def edit_student(student_data: StudentUpdate, session: Session = Depends(get_session)):
    updated_student = crud_student.update_student(session, student_data)
    if not updated_student:
        raise HTTPException(status_code=404, detail="Student not found")
    return updated_student

@router.delete("/delete-student", response_model=StudentRead)
def delete_student(student_data: StudentDelete, session: Session = Depends(get_session)):
    deleted_student = crud_student.delete_student(session, student_data)
    if not deleted_student:
        raise HTTPException(status_code=404, detail="Student not found")
    return deleted_student
