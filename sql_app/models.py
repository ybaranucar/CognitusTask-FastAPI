from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

    
class Data(Base):
    __tablename__ = "app_data"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    text = Column(String, index=True)
    label = Column(String, index=True)