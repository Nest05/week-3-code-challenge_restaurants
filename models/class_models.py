from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, unique=True, nullable=False)
    price = Column(Integer, nullable=False)

    # customers = relationship("Customer", secondary="reviews")
    reviews = relationship("Review")

    def reviews(self):
        return self.reviews

    def customer_s(self):
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
    

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, unique=True, nullable=False)

    reviews = relationship("Review")

    # restaurants = relationship("Restaurant", secondary="reviews")

    def customer_reviews(self):
        reviews = []
        for review in self.reviews:
            reviews.append((review.star_rating))
        return reviews

    def customer_restaurants(self):
        restaurants = []
        for review in self.reviews:
            restaurants.append((review.restaurant_name))
        return restaurants

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def favorite_restaurant(self):
        return max(self.reviews, key=lambda review: review.star_rating).restaurant_name

    def add_review(self, restaurant, rating):
        review = Review(restaurant_name=restaurant.name, rating=rating)
        self.reviews.append(review)

    def delete_reviews(self, restaurant):
        self.reviews = [review for review in self.reviews if review.restaurant_name != restaurant.name]
           
class Review(Base):
    __tablename__ = "reviews"

    restaurant_name = Column(String, ForeignKey("restaurants.name"), primary_key=True, nullable=False)
    customer_first_name = Column(String, nullable=False)
    customer_last_name = Column(String, ForeignKey("customers.last_name"), primary_key=True, nullable=False)
    star_rating = Column(Integer, nullable=False)

    __table_args__ = (
        UniqueConstraint("restaurant_name", "customer_last_name", "star_rating", name="_restaurant_customer_uc"),
    )


    def customer(self):
        return self.customer

    def restaurant(self):
        return self.restaurant

    def full_review(self):
        return f"Revies for {self.restaurant_name} by {self.customer_first_name} {self.customer_last_name}: {self.star_rating} stars "


