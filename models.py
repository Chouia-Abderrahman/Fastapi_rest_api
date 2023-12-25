from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Float
from database import Base

class Employee(Base):
    __tablename__ = 'Employee'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    lastName = Column(String)
    firstName = Column(String)
    dateCreated = Column(DateTime)
    department = Column(String)
    checkIns = Column(DateTime)
    checkOuts = Column(DateTime)
    timeDifference = Column(Float)
    comments = Column(String)