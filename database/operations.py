from sqlalchemy.sql.expression import null
from database import job, Session
from sqlalchemy import or_

def __get_session():
    return Session()

def insert(title, payment, date, telephone, address, zipcode, city, description):
    new_row=job(job_title=title, payment_type=payment, start_date=date, telephone=telephone, street=address, zipcode=zipcode, city=city, description=description)

    db = __get_session()
    db.add(new_row)
    db.commit()
    id = new_row.id
    db.close()
    return id

def search(keyword):
    return __get_session().query(job).filter(or_(
        job.job_title.ilike(f'%{keyword}%'), 
        job.start_date.ilike(f'%{keyword}%')))

def get():
    return __get_session().query(job).order_by(job.start_date)

def next():
    return __get_session().query(job).order_by(job.start_date).first()


def delete(id):
    db = __get_session()
    db.query(job).filter(job.id==id).delete()
    db.commit()
    db.close()
