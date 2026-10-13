import os 
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import ( create_async_engine ,
                                    async_sessionmaker)
from fastapi import HTTPException

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL :
    raise HTTPException ( status_code= 500 , 
                        detail='The database connection failed as not Database URL')

#create a new engine 
engine = create_async_engine ( DATABASE_URL , 
                        pool_size= 5,
                        pool_timeout=30,
                        pool_recycle=1800,
                        pool_pre_ping= True,
                        echo= False 
                    )

#creating a session factory 
SessionLocal = async_sessionmaker( bind=engine ,
                            autoflush=True,
                            expire_on_commit=True
                        )
