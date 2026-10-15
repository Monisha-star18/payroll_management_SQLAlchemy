from decimal import Decimal
from pydantic import BaseModel,ConfigDict,Field

BASIC_SALARY = dict(gt=5_000,lt=1_000_000)

class Base(BaseModel):
    pass


class EmployeeSalaryResponse(Base):

    model_config = ConfigDict(from_attributes=True)

    employee_id: int
    basic_salary: float
    da: float
    pf: float
    gross_salary: float


class CreateEmployee(Base):
    model_config = ConfigDict(extra='forbid')

    employee_id :int = Field(ge=1)
    basic_salary : float = Field(**BASIC_SALARY)


class UpdateEmployee(Base):
    model_config = ConfigDict(extra='forbid')

    basic_salary : float = Field(**BASIC_SALARY)
    