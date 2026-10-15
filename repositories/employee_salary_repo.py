from fastapi import HTTPException,Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from models import EmployeePayDeatils

class EmployeeSalaryRepo:

    def __init__(self):
        pass

    async def fetch_all_employee_salary(self,db:AsyncSession)-> list[EmployeePayDeatils]:

        try:
            stmt = select(EmployeePayDeatils)
            result = (await db.scalars(stmt)).all()

            if result:
                return result

            return {"message":"The table is empty"}
        
        except Exception as er :
            raise HTTPException ( status_code=500, detail=str(er))

    async def post_employee(self,employee_details,db):
        try:
            employee_data = EmployeePayDeatils(**employee_details)
            db.add(employee_data)
            await db.commit()

            return{"message":f"Employee with ID {employee_details["employee_id"]} is added" , 
                   "Salary_deatiles":employee_details}
                   
        except IntegrityError:
            await db.rollback()
            raise HTTPException(status_code=409, detail="Employee ID already exists")
        
        except SQLAlchemyError as er:
            await db.rollback()
            raise HTTPException(status_code=500, detail=str(er))

        
