from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.orm import relationship
from src.db.config import Base

class Users(Base):
    """ Users Entity """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    password = Column(String, nullable=False)
    birthdate = Column(Date, nullable=True) 
    #After insertion of birthdate on register page, modify the 'nullable=True' to 'nullable=False'

    def __rep__(self):
        return f"Usr [name={self.name}]"
    