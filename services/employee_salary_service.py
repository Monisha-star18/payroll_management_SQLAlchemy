from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel

from repositories.employee_salary_repo import EmployeeSalaryRepo
from services.payroll_services import PayrollService
from models import EmployeePayDeatils

class EmployeeSalaryService:

    def __init__(self):
        self.payroll_services=PayrollService()
        self.employee_repository=EmployeeSalaryRepo()
        

    async def get_all_employee(self,db:AsyncSession)->list[EmployeePayDeatils]:
        return await self.employee_repository.fetch_all_employee_salary(db)

    async def create_employee(self,employee_salary_deatils,db:AsyncSession):
        #change the object to dict
        employee_deatils = employee_salary_deatils.model_dump()

        basic_salary = employee_salary_deatils["basic_salary"]

        da = self.payroll_services(basic_salary)
        pf=self.payroll_services(basic_salary)
        gross_salary=self.payroll_services(basic_salary)

        salary_deatils = {"da":da , 
                          "pf":pf,
                          "gross_salary":gross_salary}

        employee_compailed_deatils = {**employee_deatils,**salary_deatils}

        return await self.employee_repository.post_employee(employee_compailed_deatils,db)
         

#instance of the Employee Salary Service
employee_salary_service = EmployeeSalaryService()