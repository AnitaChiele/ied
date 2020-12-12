from app import db


class Book(db.Model):
    __tablename__ = 'book'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    publisher_name = db.Column(db.String())
    author_name = db.Column(db.String())
    publisher = db.Column(db.String())
    customer_review = db.Column(db.String())

    def __init__(
        self, publisher_name, author_name, publisher, customer_review
    ):
        self.publisher_name = publisher_name
        self.author_name = author_name
        self.publisher = publisher
        self.customer_review = customer_review

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'publisher_name': self.publisher_name,
            'author_name': self.author_name,
            'publisher': self.publisher,
            'customer_review': self.customer_review
        }


class Customer(db.Model):
    __tablename__ = 'customer'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    email = db.Column(db.String())
    address = db.Column(db.String())
    phone = db.Column(db.String())
    city = db.Column(db.String())
    state = db.Column(db.String())
    zip_code = db.Column(db.String())

    def __init__(
        self, name, email, address, phone, city, state, zip_code
    ):
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone
        self.city = city
        self.state = state
        self.zip_code = zip_code

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'address': self.address,
            'phone': self.phone,
            'city': self.city,
            'state': self.state,
            'zip_code': self.zip_code
        }

    def mainData(self):
        return {
            'id': self.id,
            'name': self.name
        }
