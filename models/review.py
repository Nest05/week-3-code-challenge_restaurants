from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from customer import Customer
from restaurant import Restaurant

Base = declarative_base(1)

class Review(Base):
    __tablename__ = 'reviews'

    restaurant_name = Column(String, ForeignKey(Restaurant.name), primary_key=True, nullable=False)
    customer_first_name = Column(String, nullable=False)
    customer_last_name = Column(String, ForeignKey(Customer.last_name), primary_key=True, nullable=False)
    star_rating = Column(Integer, nullable=False)


    restaurant = relationship('restaurant.Restaurant')
    customer = relationship('customer.Customer')
    __table_args__ = (
        UniqueConstraint('restaurant_name', 'customer_last_name', 'star_rating', name='_restaurant_customer_uc'),
    )

    def customer():
        pass

    def restaurant():
        pass

    def full_review():
        pass

    