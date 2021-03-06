from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

Base = declarative_base()

class job(Base):
    __tablename__ =  'jobs'

    id = Column(Integer, primary_key=True)
    job_title = Column(String(100))
    payment_type = Column(String(100))
    start_date = Column(String(20))
    telephone = Column(String(20))
    street = Column(String(255))
    zipcode = Column(Integer)
    city = Column(String(50))
    description = Column(String(5000))

    def __repr__(self):
        return f"<Job ('{self.job_title}', '{self.payment_type}', '{self.start_date}', '{self.start_time}', '{self.telephone}', '{self.street}', '{self.zipcode}', '{self.city}', '{self.description}')>"

DATABASE_URL = os.environ['DATABASE_URL']
engine = create_engine(DATABASE_URL, pool_size=10)
Session = sessionmaker(bind=engine )
