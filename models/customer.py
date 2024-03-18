from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base(1)


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, unique=True, nullable=False)
    
    from review import Review
    from restaurant import Restaurant
    
    reviews = relationship('Review', backref='customer')
    restaurants = relationship('Restaurant', secondary = 'review.reviews' )

    def customer_reviews(self):
        return self.reviews

    def customer_restaurants(self):
        return self.restaurants

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def favorite_restaurant(self):
        return max(self.restaurants, key=lambda restaurant: restaurant.star_rating)

    def add_review(self, restaurant, rating):
        from review import Review
        review = Review(restaurant_name=restaurant.name, rating=rating)
        self.reviews.append(review)

    def delete_reviews(self, restaurant):
        self.reviews = [review for review in self.reviews if review.restaurant_name != restaurant.name]
           
