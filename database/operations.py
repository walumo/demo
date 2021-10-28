from sqlalchemy.engine import create_engine
from sqlalchemy.sql.expression import null
from werkzeug.utils import redirect
from database import job, Session
from sqlalchemy import or_

def get_session():
    return Session()

def insert(title, payment, date, telephone, address, zipcode, city, description):
    new_row=job(job_title=title, payment_type=payment, start_date=date, telephone=telephone, street=address, zipcode=zipcode, city=city, description=description)

    db = get_session()
    db.add(new_row)
    db.commit()
    id = new_row.id
    db.close()
    return id

def search(keyword):
    return get_session().query(job).filter(or_(
        job.job_title.ilike(f'%{keyword}%'), 
        job.start_date.ilike(f'%{keyword}%')))

def get():
    return get_session().query(job).all()

def delete(id):
    db = get_session()
    db.query(job).filter(job.id==id).delete()
    db.commit()
    db.close()
