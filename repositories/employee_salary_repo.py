from fastapi import HTTPException

from database.connection import SessionLocal

class EmployeeSalaryRepo:

    def __init__(self):
        pass

    def fetch_all_employee_salary():

        try:
            with SessionLocal() as session:
                pass
        
        except Exception as er :
            raise HTTPException ( status_code=500,
                                detail=er)
        
