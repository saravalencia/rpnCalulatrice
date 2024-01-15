from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Calculation(Base):
    __tablename__ = 'calculations'
    id = Column(Integer, primary_key=True, index=True)
    expression = Column(String, index=True)
    result = Column(String, index=True)