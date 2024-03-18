from sqlalchemy import create_engine
from customer import Base as CustomerBase
from restaurant import Base as RestaurantBase
from review import Base as ReviewBase
from restaurant import Restaurant
from customer import Customer
from review import Review

# Import the ReviewManagementSystem class
from review_management_system import ReviewManagementSystem

def main():
    # Specify the database file name
    db_name = 'restaurant_review_manager.db'

    # Create the engine and tables
    engine = create_engine(f'sqlite:///{db_name}')
    CustomerBase.metadata.create_all(bind=engine)
    RestaurantBase.metadata.create_all(bind=engine)
    ReviewBase.metadata.create_all(bind=engine)

    # Instantiate the ReviewManagementSystem class
    rms = ReviewManagementSystem(db_name)

    # Populate the customers table if necessary
    # if rms.session.query(Customer).count() == 0:
    #     customer1 = Customer(first_name='John', last_name='Doe')
    #     customer2 = Customer(first_name='Jane', last_name='Smith')

    #     rms.session.add_all([customer1, customer2])
    #     rms.session.commit()

if __name__ == '__main__':
    main()
# Continue with the rest of your program using the rms object

# Rest of your code goes here