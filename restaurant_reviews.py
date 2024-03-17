from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, UniqueConstraint

from sqlalchemy.orm import sessionmaker, relationship, declarative_base

Base = declarative_base()


class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, unique=True, nullable=False)
    price = Column(Integer, nullable=False)

    customers = relationship('Customer', secondary="reviews")

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, unique=True, nullable=False)

class Review(Base):
    __tablename__ = 'reviews'

    restaurant_id = Column(Integer, ForeignKey('restaurants.id'), primary_key=True, nullable=False)
    customer_id = Column(Integer, ForeignKey('customers.id'), primary_key=True, nullable=False)
    star_rating = Column(Integer, nullable=False)

    __table_args__ = (
        UniqueConstraint('restaurant_id', 'customer_id', 'star_rating', name='_restaurant_customer_uc'),
    )

class ReviewManagementSystem:

    def __init__(self, db_name):
        self.engine = create_engine(f'sqlite:///{db_name}')
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def add_restaurant(self, name, price):

        if not name or not price:
            print("Error: fields cannot be empty")
        
        restaurant = Restaurant(name=name, price=price)

        try:
            self.session.add(restaurant)
            self.session.commit()
            print("Restaurant Added successfully")
        except Exception as e:
            self.session.rollback()
            print(f'Error: {e}')

    def add_customer(self, first_name, last_name):
        
        if not first_name or not last_name:
            print("Error: fields cannot be empty")
        
        customer = Customer(first_name=first_name, last_name=last_name)

        try:
            self.session.add(customer)
            self.session.commit()
            print("Customer Added Successfully")
        except Exception as e:
            self.session.rollback()
            print(f'Error: {e}')

    def associate_review(self, restaurant_id, customer_id, star_rating):
        # if not restaurant_id or not customer_id or not star_rating:
        #     print("Error: fields cannot be empty")

        review = Review(restaurant_id=restaurant_id, customer_id=customer_id, star_rating=star_rating)

        try:
            self.session.add(review)
            self.session.commit()
            print("Review Successfully added")
        except Exception as e:
            self.session.rollback()
            print(f'Error: {e}')

    def all_reviews_for_restaurant(self, restaurant_id):
        reviews = self.session.query(Review).filter_by(restaurant_id=restaurant_id).all()

        if reviews:
            return reviews
        else:
            print("No reviews found for the restaurant")
            return []

if __name__ == '__main__':
    restaurant_review_management = ReviewManagementSystem("restaurant_review_manager.db")

    # restaurant_review_management.add_restaurant('Jajamelo', 500)
    # restaurant_review_management.add_restaurant('Mama Rocks', 1000)
    # restaurant_review_management.add_restaurant('Urban Burger', 1200)

    # restaurant_review_management.add_customer('Nestor', 'Masinde')
    # restaurant_review_management.add_customer('John', 'Kimani')
    # restaurant_review_management.add_customer('Levis', 'Ngige')
    # restaurant_review_management.add_customer('Naomi', 'Lagat')
    # restaurant_review_management.add_customer('John', 'Ouma')
    # restaurant_review_management.add_customer('Monica', 'Mwangi')

    # restaurant_review_management.associate_review(1, 2, 3)
    # restaurant_review_management.associate_review(1, 1, 2)
    # restaurant_review_management.associate_review(1, 3, 4)
    # restaurant_review_management.associate_review(1, 4, 3)
    # restaurant_review_management.associate_review(1, 5, 1)
    # restaurant_review_management.associate_review(2, 1, 4)
    # restaurant_review_management.associate_review(2, 2, 3)
    # restaurant_review_management.associate_review(2, 3, 5)
    # restaurant_review_management.associate_review(2, 4, 4)
    # restaurant_review_management.associate_review(2, 5, 5)
    # restaurant_review_management.associate_review(3, 4, 4)
    # restaurant_review_management.associate_review(3, 3, 4)
    # restaurant_review_management.associate_review(3, 2, 5)
    # restaurant_review_management.associate_review(3, 1, 4)
    # restaurant_review_management.associate_review(3, 5, 5)

    
    reviews = restaurant_review_management.all_reviews_for_restaurant(1)
    for review in reviews:
        print(review.star_rating)