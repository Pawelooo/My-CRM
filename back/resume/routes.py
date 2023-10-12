from app import app
from app.models import Book
from flask import render_template, jsonify



@app.route('/', methods=['GET'])
def read_all_authors():
    books = Book.query.all()
    return jsonify(books)
