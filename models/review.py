from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, UniqueConstraint

from sqlalchemy.orm import sessionmaker, relationship, declarative_base

Base = declarative_base()

class Review(Base):
    __tablename__ = 'reviews'

    restaurant_name = Column(String, ForeignKey('restaurants.name'), primary_key=True, nullable=False)
    customer_first_name = Column(String, nullable=False)
    customer_last_name = Column(String, ForeignKey('customers.last_name'), primary_key=True, nullable=False)
    star_rating = Column(Integer, nullable=False)

    __table_args__ = (
        UniqueConstraint('restaurant_name', 'customer_last_name', 'star_rating', name='_restaurant_customer_uc'),
    )