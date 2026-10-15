import os 
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL :
    raise RuntimeError("DATABASE_URL is not set. Check your .env file.")

#create a new engine 
engine = create_engine ( DATABASE_URL , 
                        pool_size= 5,
                        pool_timeout=30,
                        pool_recycle=1800,
                        pool_pre_ping= True,
                        echo= False 
                    )

#creating a session factory 
SessionLocal = sessionmaker( bind=engine ,
                            autoflush=True,
                            expire_on_commit=True
                        )
