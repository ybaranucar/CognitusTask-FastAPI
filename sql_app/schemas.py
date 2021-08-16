from pydantic import BaseModel


class DataBase(BaseModel):
    text: str 
    label: str

class DataCreate(DataBase):
    pass 

class Data(DataBase):
    id: int 
    
    class Config:
        orm_mode = True
        
    