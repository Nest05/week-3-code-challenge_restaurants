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
    
    reviews = relationship('review.Review', backref='restaurant')

    def reviews(self):
        return self.reviews

    def customers(self):
        return self.customers
    
    @classmethod
    def fanciest(cls):
        priciest_restaurant = cls.query.order_by(cls.price.desc()).first()
        return priciest_restaurant

    def all_reviews(self):
        review_strings = []
        
        for review in self.reviews:
            review_string = f"Review for {self.name} by {review.customer_first_name} {review.customer_last_name}: {review.star_rating} stars"
            review_strings.append(review_string)
        
        return review_strings