from fastapi import Depends, FastAPI, HTTPException, status
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
    dateCreated: Optional[datetime] = None
    checkIns: Optional[datetime] = None
    checkOuts: Optional[datetime] = None
    timeDifference: Optional[float] = None
    comments: Optional[str] = None

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/employee/")
async def create_employee(new_employee: Employee, db: Session = Depends(get_db)):
    try:
        db_employee = models.Employee(
            lastName=new_employee.lastName,
            firstName=new_employee.firstName,
            department=new_employee.department,
        )
        db.add(db_employee)
        db.commit()
        db.refresh(db_employee)
        return db_employee
    except Exception as e:
        db.rollback()
        print(f"Error during database operation: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from e