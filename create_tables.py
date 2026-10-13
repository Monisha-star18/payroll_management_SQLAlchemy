from database.connection import engine
from models import Base, EmployeePayDeatils


def create_tables():
    Base.metadata.create_all(bind=engine)
    print("Table availability check")


if __name__ == "__main__":
    create_tables()