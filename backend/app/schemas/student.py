from pydantic import BaseModel

class StudentBase(BaseModel):
    id:int
    name:str
    age:int
    
class StudentCreate(BaseModel):
    name:str
    age:int

class StudentRead(BaseModel):
    id:int
    name:str
    age:int
    
class StudentUpdate(BaseModel):
    id:int
    name: str | None = None
    age: int | None = None

    