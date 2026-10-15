from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from repositories.employee_salary_repo import EmployeeSalaryRepo
from services.payroll_services import PayrollService
from models import EmployeePayDeatils

class EmployeeSalaryService:

    def __init__(self):
        self.payroll_services=PayrollService()
        self.employee_repository=EmployeeSalaryRepo()
        

    async def get_all_employee(self,db:AsyncSession)->list[EmployeePayDeatils]:
        return await self.employee_repository.fetch_all_employee_salary(db)
         

#instance of the Employee Salary Service
employee_salary_service = EmployeeSalaryService()