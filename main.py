from fastapi import FastAPI,APIRouter

from routers.employee_salary_router import router as employee_salary_router

app=FastAPI(title="Employee Payroll Management")

app.include_router(employee_salary_router)

router = APIRouter()

@router.get('/')
async def welcome():
    return {"message" : "Welcom to the Employee Payroll Management"}
