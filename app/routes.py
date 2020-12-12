from flask import request, jsonify
from flask_sqlalchemy import SQLAlchemy
from app import app
from .models import Book, Customer


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

SQLALCHEMY_DATABASE_URI = "postgresql://{username}:{password}@{hostname}/{databasename}".format(
    username="postgres",
    password="12345678",
    hostname="172.17.0.2",
    databasename="postgres",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)


@app.route('/customer/add', methods=['POST'])
def add_customer():
    try:
        data = request.get_json()

        customer = Customer(
            name=data['name'],
            email=data['email'],
            address=data['address'],
            phone=data['phone'],
            city=data['city'],
            state=data['state'],
            zip_code=data['zip_code']
        )

        db.session.add(customer)
        db.session.commit()
        return "Customer added. customer id={}".format(customer.id)

    except Exception as e:
        return(str(e))


@app.route('/customers/all/main')
def get_all_main_customer():
    try:
        books = Customer.query.all()
        return jsonify([e.mainData() for e in books])
    except Exception as e:
        return(str(e))


@app.route('/customers/all')
def get_all_customers():
    try:
        books = Customer.query.all()
        return jsonify([e.serialize() for e in books])
    except Exception as e:
        return(str(e))


@app.route('/books/all')
def get_all_books():
    try:
        books = Book.query.all()
        return jsonify([e.serialize() for e in books])
    except Exception as e:
        return(str(e))
