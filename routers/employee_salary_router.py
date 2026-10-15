from fastapi import APIRouter , Depends,Path
from sqlalchemy.ext.asyncio import AsyncSession

from services.employee_salary_service import employee_salary_service
from database import get_session

from schemas import EmployeeSalaryResponse , CreateEmployee , UpdateEmployee , IncrementRequest

router = APIRouter(prefix="/api/employee_salary")

#get all the employee salary deatiles 
@router.get('/', response_model=list[EmployeeSalaryResponse]|dict)
async def get_all_employee_salary_details(db:AsyncSession = Depends(get_session)):
    return await employee_salary_service.get_all_employee(db)

#post the new employee
@router.post('/createEmployeeSalary')
async def create_employee_salary(employee_salary_deatils :CreateEmployee,
                                 db:AsyncSession = Depends(get_session)
                                ):
    return await employee_salary_service.create_employee(employee_salary_deatils,db)

#update the existing employee details 
@router.put('/updateEmployee/{employee_id}')
async def edit_employee_details(employee_deatils:UpdateEmployee,
                                employee_id:int = Path(gt=0),
                                db:AsyncSession = Depends(get_session),
                                ):
    
    return await employee_salary_service.edit_employee(employee_deatils,employee_id,db)


#delete employee details 
@router.delete('/deleteEmployee/{employee_id}')
async def remove_employee_details(employee_id:int = Path(gt=0),
                                db:AsyncSession = Depends(get_session),
                                ):
    
    return await employee_salary_service.remove_employee(employee_id,db)

#increment by percentage
@router.patch('/{employee_id}/increment', response_model=EmployeeSalaryResponse)
async def increase_employee_salary(employee_id: int, 
                                   increment_details: IncrementRequest,
                                    db: AsyncSession = Depends(get_session)):
    return await employee_salary_service.increase_salary(employee_id, increment_details, db)