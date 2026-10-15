from fastapi import APIRouter , Depends
from sqlalchemy.ext.asyncio import AsyncSession

from services.employee_salary_service import employee_salary_service
from database import get_session

from schemas import EmployeeSalaryResponse , CreateEmployee

router = APIRouter(prefix="/api/employee_salary")

#get all the employee salary deatiles 
@router.get('/', response_model=list[EmployeeSalaryResponse])
async def get_all_employee_salary_details(db:AsyncSession = Depends(get_session)):
    return await employee_salary_service.get_all_employee(db)

@router.post('/createEmployeeSalary')
async def create_employee_salary(employee_salary_deatils :CreateEmployee,db:AsyncSession = Depends(get_session)):
    return await employee_salary_service.create_employee(employee_salary_deatils,db)