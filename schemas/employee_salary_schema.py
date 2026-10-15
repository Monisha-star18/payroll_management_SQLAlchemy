from decimal import Decimal
from pydantic import BaseModel,ConfigDict,Field

class Base(BaseModel):
    pass

class EmployeeSalaryResponse(Base):

    model_config = ConfigDict(from_attributes=True)

    employee_id: int
    basic_salary: Decimal
    da: Decimal
    pf: Decimal
    gross_salary: Decimal
