from pydantic import BaseModel

class StudentBase(BaseModel):
    id:int
    name:str
    age:int
    class Config:
        orm_mode = True
    
class StudentCreate(BaseModel):
    name:str
    age:int
    class Config:
        orm_mode = True

class StudentRead(BaseModel):
    id:int
    name:str
    age:int
    class Config:
        orm_mode = True
    
class StudentUpdate(BaseModel):
    id:int
    name: str | None = None
    age: int | None = None
    class Config:
        orm_mode = True

    