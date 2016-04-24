from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    fullname = Column(String)
    email = Column(String)
    password = Column(String)

    def __init__(self, username, fullname, email, password):
        self.username = username
        self.fullname = fullname
        self.email = email
        self.password = password

    def __repr__(self):
        return "<User(username='%s', fullname='%s', email='%s' password='%s')>" % (
                        self.username, self.fullname, self.email, self.password)

engine = create_engine('sqlite:///sqlalchemy_users.db')
Base.metadata.create_all(engine)
