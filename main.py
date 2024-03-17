# main.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.restaurant import Restaurant
from models.customer import Customer
from models.review import Review

engine = create_engine('sqlite:///restaurant_review_manager.db')
Session = sessionmaker(bind=engine)
session = Session()

# Rest of your code goes here