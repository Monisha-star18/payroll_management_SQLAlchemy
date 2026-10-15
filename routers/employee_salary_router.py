from fastapi import APIRouter 

from services.employee_salary_service import employee_salary_service

router = APIRouter(prefix="/api/employee_salary")

#get all the employee salary deatiles 
@router.get('/')
def get_all_employee_salary_details():
    return employee_salary_service.get_all_employee()
