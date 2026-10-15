from fastapi import HTTPException
from sqlalchemy import select

from database.connection import SessionLocal
from models import EmployeePayDeatils

class EmployeeSalaryRepo:

    def __init__(self):
        pass

    def fetch_all_employee_salary(self):

        try:
            with SessionLocal() as session:

                stmt = select(EmployeePayDeatils)
                result = session.scalars(stmt).all()

                if result:
                    return result

                return {"message":"The table is empty"}
        
        except Exception as er :
            raise HTTPException ( status_code=500, detail=str(er))
        
