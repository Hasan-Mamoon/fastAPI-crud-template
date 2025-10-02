from fastapi import HTTPException
from sqlmodel import Session, select
from app.models.student import student
from app.schemas.student import StudentCreate, StudentUpdate, StudentDelete

def create_student(db: Session, student_in: StudentCreate) -> student:
    db_student = student.model_validate(student_in)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def get_all_students(db: Session) -> list[student]:
    return list(db.exec(select(student)).all())


def update_student(db: Session, student_data: StudentUpdate) -> student:
    db_student = db.exec(select(student).where(student.id == student_data.id)).first()
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    update_data = student_data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_student, key, value)
    
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


def delete_student(db: Session, studentTod: StudentDelete) -> student:
    toDelete = db.get(student,studentTod.id)
    if not toDelete:
        raise HTTPException(status_code=404, detail="Student not found")
    db.delete(toDelete)
    db.commit()
    return toDelete
