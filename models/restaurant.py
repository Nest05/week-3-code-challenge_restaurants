from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base(1)

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, unique=True, nullable=False)
    price = Column(Integer, nullable=False)

    customers = relationship('customer.Customer', secondary="review.reviews")
    children = relationship("Child")

    def reviews():
        pass

    def customers():
        pass
    
    def fanciest():
        pass

    def all_reviews():
        pass