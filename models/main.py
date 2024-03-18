from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from customer import Base as CustomerBase, Customer
from restaurant import Base as RestaurantBase, Restaurant
from review import Base as ReviewBase, Review

engine = create_engine('sqlite:///restaurant_review_manager.db')
Session = sessionmaker(bind=engine)
session = Session()

CustomerBase.metadata.create_all(engine)
RestaurantBase.metadata.create_all(engine)
ReviewBase.metadata.create_all(engine)



