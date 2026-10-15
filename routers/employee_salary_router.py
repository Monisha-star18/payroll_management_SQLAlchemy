from fastapi import APIRouter , Depends
from sqlalchemy.ext.asyncio import AsyncSession

from services.employee_salary_service import employee_salary_service
from database import get_session

router = APIRouter(prefix="/api/employee_salary")

#get all the employee salary deatiles 
@router.get('/')
async def get_all_employee_salary_details(db:AsyncSession = Depends(get_session)):
    return await employee_salary_service.get_all_employee(db)
