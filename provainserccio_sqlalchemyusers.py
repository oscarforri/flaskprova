#https://alexanderae.com/sqlalchemy-orm-para-python-1.html

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_declarative import User, Base

engine = create_engine('sqlite:///sqlalchemy_users.db', echo=True)
DBSession = sessionmaker(bind=engine)
session = DBSession()

##Insertamos usuarios
#user_1 = User('oscar35','Oscar Forradellas','oscar35@gmail.com','1234')
#session.add(user_1)
#session.commit()

#Realizamos consulta
print "---------------/n/n Realitzem consulta"
user = session.query(User).all()
print user
