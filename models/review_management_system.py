from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from restaurant import Restaurant
from customer import Customer
from review import Review

Base = declarative_base()

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

    def associate_review(self, restaurant_name,customer_first_name, customer_last_name, star_rating):
        # if not restaurant_id or not customer_id or not star_rating:
        #     print("Error: fields cannot be empty")

        review = Review(restaurant_name=restaurant_name, customer_first_name=customer_first_name ,customer_last_name=customer_last_name, star_rating=star_rating)

        try:
            self.session.add(review)
            self.session.commit()
            print("Review Successfully added")
        except Exception as e:
            self.session.rollback()
            print(f'Error: {e}')

if __name__ == '__main__':
    restaurant_review_management = ReviewManagementSystem("restaurant_review_manager.db")

    restaurant_review_management.add_restaurant('Jajamelo', 500)
    restaurant_review_management.add_restaurant('Mama Rocks', 1000)
    restaurant_review_management.add_restaurant('Urban Burger', 1200)

    restaurant_review_management.add_customer('Nestor', 'Masinde')
    restaurant_review_management.add_customer('John', 'Kimani')
    restaurant_review_management.add_customer('Levis', 'Ngige')
    restaurant_review_management.add_customer('Naomi', 'Lagat')
    restaurant_review_management.add_customer('John', 'Ouma')
    restaurant_review_management.add_customer('Monica', 'Mwangi')

    restaurant_review_management.associate_review('Jajamelo', 'John',  'Kimani', 3)
    restaurant_review_management.associate_review('Jajamelo', 'Nestor', 'Masinde', 2)
    restaurant_review_management.associate_review('Jajamelo', 'Levis', 'Ngige', 4)
    restaurant_review_management.associate_review('Jajamelo', 'Naomi', 'Lagat', 3)
    restaurant_review_management.associate_review('Jajamelo', 'Monica', 'Mwangi', 1)
    restaurant_review_management.associate_review('Mama Rocks', 'Nestor', 'Masinde', 4)
    restaurant_review_management.associate_review('Mama Rocks', 'John', 'Kimani', 3)
    restaurant_review_management.associate_review('Mama Rocks', 'Levis', 'Ngige', 5)
    restaurant_review_management.associate_review('Mama Rocks', 'Naomi', 'Lagat', 4)
    restaurant_review_management.associate_review('Mama Rocks', 'Monica', 'Mwangi', 5)
    restaurant_review_management.associate_review('Urban Burger', 'Naomi', 'Lagat', 4)
    restaurant_review_management.associate_review('Urban Burger', 'Levis', 'Ngige', 4)
    restaurant_review_management.associate_review('Urban Burger', 'John', 'Kimani', 5)
    restaurant_review_management.associate_review('Urban Burger', 'Nestor', 'Masinde', 4)
    restaurant_review_management.associate_review('Urban Burger', 'Monica', 'Mwangi', 5)