from fastapi import HTTPException

from repositories.employee_salary_repo import EmployeeSalaryRepo
from services.payroll_services import PayrollService

class EmployeeSalaryService:

    def __init__(self):
        self.payroll_services=PayrollService()
        self.employee_repository=EmployeeSalaryRepo()
        

    def get_all_employee(self):
        return self.employee_repository.fetch_all_employee_salary()
         

#instance of the Employee Salary Service
employee_salary_service = EmployeeSalaryService()