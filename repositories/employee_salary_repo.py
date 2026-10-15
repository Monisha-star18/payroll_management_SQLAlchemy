from fastapi import HTTPException,Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from models import EmployeePayDeatils

class EmployeeSalaryRepo:

    def __init__(self):
        pass

    #get alll employees 
    async def fetch_all_employee_salary(self,db:AsyncSession)-> list[EmployeePayDeatils]|dict:

        try:
            stmt = select(EmployeePayDeatils)
            result = (await db.scalars(stmt)).all()

            if result:
                return result

            return {"message":"The table is empty"}
        
        except SQLAlchemyError as er:
            raise HTTPException(status_code=500, detail=str(er))
        
    #create new employess
    async def post_employee(self,employee_details,db):
        try:
            employee_data = EmployeePayDeatils(**employee_details)
            db.add(employee_data)
            await db.commit()

            return{"message":f"Employee with ID {employee_details["employee_id"]} is added" , 
                   "Salary_deatiles":employee_details}
                   
        except IntegrityError:
            await db.rollback()
            raise HTTPException(status_code=500, detail="Employee ID already exists")
        
        except SQLAlchemyError as er:
            await db.rollback()
            raise HTTPException(status_code=500, detail=str(er))

    #update employee
    async def put_employee(self,employee_details,db):
        try:
            employee = await db.get(EmployeePayDeatils,employee_details["employee_id"])

            if not employee :
                return {"message":f"The id {employee_details["employee_id"]} dont exists "}

            for column , value in employee_details.items():
                if column != "employee_id":
                    setattr(employee,column,value)

            await db.commit()
            await db.refresh(employee)

            return{"message":f"Employee with ID {employee_details["employee_id"]} is updated" , 
                               "Salary_deatiles": employee_details}
        

        except SQLAlchemyError as er:
            await db.rollback()
            raise HTTPException(status_code=500, detail=str(er))

    #delete the employee 
    async def delete_employee(self,employee_id,db):
        try:
            employee = await db.get(EmployeePayDeatils,employee_id)
            
            if not employee :
                return {"message":f"The id {employee_id} dont exists "}

            await db.delete(employee)
            await db.commit()

            return{"message":f"Employee with ID {employee_id} is deleted"}

        except SQLAlchemyError as er:
            await db.rollback()
            raise HTTPException(status_code=500, detail=str(er))



            
                
        
