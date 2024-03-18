from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base(1)

class Review(Base):
    __tablename__ = 'reviews'

    from customer import Customer
    from restaurant import Restaurant
    
    restaurant_name = Column(String, ForeignKey(Restaurant.name), primary_key=True, nullable=False)
    customer_first_name = Column(String, nullable=False)
    customer_last_name = Column(String, ForeignKey(Customer.last_name), primary_key=True, nullable=False)
    star_rating = Column(Integer, nullable=False)


    restaurant = relationship('restaurant.Restaurant')
    customer = relationship('customer.Customer')
    __table_args__ = (
        UniqueConstraint('restaurant_name', 'customer_last_name', 'star_rating', name='_restaurant_customer_uc'),
    )

    def customer(self):
        return self.customer

    def restaurant(self):
        return self.restaurant

    def full_review(self):
        return f"Revies for {self.restaurant_name} by {self.customer_first_name} {self.customer_last_name}: {self.star_rating} stars "

    