from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, unique=True, nullable=False)
    price = Column(Integer, nullable=False)

    customers = relationship('Customer', secondary="reviews")

    def reviews():
        pass

    def customers():
        pass
    
    def fanciest():
        pass

    def all_reviews():
        pass