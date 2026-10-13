from database.connection import engine
from models.Table_Model import Base

from models.Employee_Personal_Model import EmployeePayDeatils

def create_tables():
    Base.metadata.create_all(bind=engine)
    print("Table avaliablity check")

if __name__ == "__main__":
    create_tables()