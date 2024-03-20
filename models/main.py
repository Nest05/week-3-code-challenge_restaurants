from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from class_models import Base, Customer, Restaurant, Review

class ReviewManagementSystem:

    def __init__(self, db_name):
        self.engine = create_engine(f'sqlite:///{db_name}')
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
    
    def get_customer_reviews(self, customer_id):
        customer = self.session.query(Customer).get(customer_id)
        if customer:
            return customer.customer_reviews()
        else:
            return "Customer not found"
        
    def get_customer_restaurants(self, customer_id):
        customer = self.session.query(Customer).get(customer_id)
        if customer:
            return customer.restaurants()
        else:
            return "Customer not found"
        
    def get_customer_full_name(self, customer_id):
        customer = self.session.query(Customer).get(customer_id)
        if customer:
            return customer.full_name()
        else:
            return "Customer not found"
        
    def get_customer_favorite_restaurant(self, customer_id):
        customer = self.session.query(Customer).get(customer_id)
        if customer:
            return customer.favorite_restaurant()
        else:
            return "Customer not found"

if __name__ == '__main__':
    restaurant_review_management = ReviewManagementSystem("restaurant_review_manager.db")

    # customer_reviews = restaurant_review_management.get_customer_reviews(1)
    # print(customer_reviews)