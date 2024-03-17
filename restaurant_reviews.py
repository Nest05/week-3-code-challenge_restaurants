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
    first_name = Column(String, unique=True, nullable=False)
    last_name = Column(String, unique=True, nullable=False)

class Review(Base):
    __tablename__ = 'reviews'

    restaurant_id = Column(Integer, ForeignKey('restaurants_id'), primary_key=True, nullable=False)
    customer_id = Column(Integer, ForeignKey('customers_id'), primary_key=True, nullable=False)
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
