from fastapi import FastAPI,Depends, HTTPException
from sqlmodel import select
from .database.session import Session,get_session
from .schemas.student import StudentCreate,StudentRead,StudentUpdate
from .models.student import student

app = FastAPI()


@app.get("/students", response_model=list[StudentRead])
def read_users(session:Session= Depends(get_session)):
    students = session.exec(select(student)).all()
    return students

@app.post("/add-students", response_model=StudentRead)
def create_student(newStudent: StudentCreate, session: Session = Depends(get_session)):
    session.add(newStudent)
    session.commit()
    session.refresh(newStudent)
    return newStudent

@app.patch("/edit-student",response_model=StudentRead)
def edit_student(studentData: StudentUpdate, session: Session = Depends(get_session)):
    res = session.exec(select(student).where(student.id == studentData.id))
    db_student = res.first()

    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")

    update_data = studentData.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_student, key, value)

    session.add(db_student)
    session.commit()
    session.refresh(db_student)

    return db_student

@app.delete("/delete-student",response_model=StudentRead)
def delete_student(student_id:int,session:Session=Depends(get_session)):
  toDelete = session.get(student,student_id)
  if not toDelete:
        raise HTTPException(status_code=404, detail="Student not found")
  session.delete(toDelete)
  session.commit()
  return toDelete
