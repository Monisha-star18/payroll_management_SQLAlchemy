from decimal import Decimal
from pydantic import BaseModel,ConfigDict,Field

BASIC_SALARY = dict(ge=5_000,lt=1_000_000)

class Base(BaseModel):
    pass


class EmployeeSalaryResponse(Base):

    model_config = ConfigDict(from_attributes=True)

    employee_id: int
    basic_salary: Decimal
    da: Decimal
    pf: Decimal
    gross_salary: Decimal


class CreateEmployee(Base):
    model_config = ConfigDict(extra='forbid')

    employee_id :int = Field(ge=1)
    basic_salary : Decimal = Field(**BASIC_SALARY)
