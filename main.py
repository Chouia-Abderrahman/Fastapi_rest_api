from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Annotated, Optional
import models
from database import engine, session_local
from sqlalchemy.orm import Session
from datetime import datetime
from database import Base


app = FastAPI()

# Database Configuration
DATABASE_URL = "postgresql://odoo:odoo@localhost/fastapi"

# Class model for the data
class Employee(BaseModel):
    lastName: str
    firstName: str
    department: str
    dateCreated: Optional[datetime]
    checkIns: Optional[datetime]
    checkOuts: Optional[datetime]
    timeDifference: Optional[float]
    comments: Optional[str]

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/employee/")
async def create_employee(new_employee : Employee, db : db_dependency):
    db_employee = models.Employee(lastName = new_employee.lastName,
                                  firstName = new_employee.firstName,
                                  department = new_employee.department,
                                  )
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)