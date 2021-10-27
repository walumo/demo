from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import sessionmaker
import os
from datetime import datetime
from sqlalchemy.orm.session import Session


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

engine = create_engine('sqlite:///database.db')
Session = sessionmaker(bind=engine)
