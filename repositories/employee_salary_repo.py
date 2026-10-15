from fastapi import HTTPException,Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from database.connection import SessionLocal,get_session
from models import EmployeePayDeatils

class EmployeeSalaryRepo:

    def __init__(self):
        pass

    async def fetch_all_employee_salary(self,db:Session = Depends(get_session)):

        try:
            
            stmt = select(EmployeePayDeatils)
            result = (await db.scalars(stmt)).all()

            if result:
                return result

            return {"message":"The table is empty"}
        
        except Exception as er :
            raise HTTPException ( status_code=500, detail=str(er))
        
