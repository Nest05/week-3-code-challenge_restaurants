from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, unique=True, nullable=False)

    def reviews():
        pass

    def restaurants():
        pass

    def full_name():
        pass

    def favorite_retsaurant():
        pass

    def add_review(restaurant, rating):
        pass

    def delete_reviews(restaurant):
        pass    
