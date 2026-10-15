from fastapi import HTTPException,Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

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

    async def post_employee(employee_details,db):
        try:
            await db.add(employee_details)
            await db.commit()

            return{"message":f"Employee with ID {employee_details["employee_id"]} is added" , 
                   "Salary_deatiles":employee_details}
                   
        except Exception as er :
            raise HTTPException ( status_code=500, detail=str(er))

        
