# from back.resume.models import app

from datetime import datetime

from flask.views import View, MethodView
# from back.resume.models import Book, generate_uuid, app, Author, Category, Item, Course
from flask import jsonify, request, abort

# from back.resume.models import db
import uuid
from dataclasses import dataclass
from datetime import datetime
from typing import List, Dict, Any

import psycopg2
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, JSON, Column, UUID, String, DateTime, \
    Integer
from back.resume import routes

app = Flask(__name__)
pg_user = "postgres"
pg_pwd = "qawsed"
pg_port = "5432"
app.config[
    "SQLALCHEMY_DATABASE_URI"] = f"postgresql://{pg_user}:{pg_pwd}@localhost:{pg_port}/my-crm-basic"
db = SQLAlchemy(app)
conn = psycopg2.connect(database='my-crm-basic', user='postgres',password='qawsed')






if __name__ == "__main__":
    app.run(debug=True)
