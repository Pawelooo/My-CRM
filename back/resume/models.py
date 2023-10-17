import datetime
import uuid
from dataclasses import dataclass
from typing import Dict, List
from uuid import UUID

import psycopg2
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, func, String, Integer, JSON, DateTime

# from back.app import db

app = Flask(__name__)
pg_user = "postgres"
pg_pwd = "qawsed"
pg_port = "5432"
app.config[
    "SQLALCHEMY_DATABASE_URI"] = f"postgresql://{pg_user}:{pg_pwd}@localhost:{pg_port}/my-crm-basic"
db = SQLAlchemy(app)
conn = psycopg2.connect(database='my-crm-basic', user='postgres',password='qawsed')

def generate_uuid():
    return str(uuid.uuid4())


@dataclass
class Book(db.Model):
    id: str
    name: str
    category: str
    author: str
    link: str
    version: str
    page_count: int
    date_publish: datetime

    id = db.Column(db.String(36), primary_key=True, default=generate_uuid,
                   unique=True)
    name = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    link = db.Column(db.String(200), nullable=True)
    version = db.Column(db.String(200), nullable=True)
    page_count = db.Column(db.String(200), nullable=True)
    date_publish = db.Column(db.DateTime(timezone=True), nullable=True)

    def __getitem__(self, item):
        return getattr(self, item)


@dataclass
class Author(db.Model):
    id: str
    name: str
    surname: str
    website: str
    country: str
    topic: str

    id = db.Column(db.String(36), primary_key=True, default=generate_uuid,
                   unique=True)
    name = db.Column(db.String(200), nullable=False)
    surname = db.Column(db.String(200), nullable=False)
    website = db.Column(db.String(255), nullable=True)
    country = db.Column(db.String(200), nullable=True)
    topic = db.Column(db.String(200), nullable=True)

    def __getitem__(self, item):
        return getattr(self, item)


@dataclass
class Category(db.Model):
    id: str
    name: str

    id = db.Column(db.String(36), primary_key=True, default=generate_uuid,
                   unique=True)
    name = db.Column(db.String(200), nullable=False)

    def __getitem__(self, item):
        return getattr(self, item)


@dataclass
class Course(db.Model):
    id: str
    name: str
    category: str
    author: str
    link: str
    topic: str
    id = db.Column(db.String(36), primary_key=True, default=generate_uuid,
                   unique=True)
    name = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    link = db.Column(db.String(200), nullable=True)
    topic = db.Column(db.String(200), nullable=True)

    def __getitem__(self, item):
        return getattr(self, item)


def add_dict_to_method_args(method):
    def wrapper(self, custom_dict: Dict[str, str], *args, **kwargs):
        return method(self, custom_dict, *args, **kwargs)

    return wrapper


@dataclass
class Item(db.Model):
    id: str
    name: str
    title: str
    description: str
    deadline: datetime
    category: str
    assignee: int
    status: str
    name_file: str
    attachments: Dict[str, int]
    tag: str
    amounts: JSON
    amounts_tag: JSON

    id = Column(String(36), primary_key=True,
                default=func.uuid_generate_v4, unique=True)
    name = Column(String(200), nullable=False)
    title = Column(String(200), nullable=False)
    description = Column(String(500), nullable=False)
    deadline = Column(DateTime(timezone=True), nullable=False)
    category = Column(String(200), nullable=False)
    assignee = Column(Integer, nullable=False)
    status = Column(String(50), nullable=True, default='todo')
    name_file = Column(String(200), nullable=False)
    attachments = Column(JSON, nullable=True)
    tag = Column(String(200), nullable=True)
    amounts = Column(JSON, default={'todo': 0, "INPROGRESS": 0, 'DONE': 0},
                     nullable=True)
    amounts_tag = Column(JSON, default={'todo': 0, "INPROGRESS": 0, 'DONE': 0},
                         nullable=True)

    def __getitem__(self, item):
        return getattr(self, item)


@dataclass
class Question(db.Model):
    id: str
    name: str
    tag: str
    number_of_fails: int
    number_of_usages: int

    id = db.Column(db.String(36), primary_key=True, default=generate_uuid,
                   unique=True)
    name = db.Column(db.String(200), nullable=False)
    surname = db.Column(db.String(200), nullable=False)
    tag = db.Column(db.String(255), nullable=False)
    number_of_fails = db.Column(db.Integer, nullable=True)
    number_of_usages = db.Column(db.Integer, nullable=True)

    def __getitem__(self, item):
        return getattr(self, item)


@dataclass
class Roadmap(db.Model):
    id: str
    type_item: str
    title: str
    priority: str
    complexity: str
    goal_completion: datetime.date
    added: str
    user_id: str
    deadline: str

    id = db.Column(db.String(36), primary_key=True, default=generate_uuid,
                   unique=True, nullable=False)
    type_item = db.Column(db.String(200), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    priority = db.Column(db.String(200), nullable=False)
    complexity = db.Column(db.String(200), nullable=False)
    goal_completion = db.Column(db.DateTime(timezone=True), nullable=False)
    added = db.Column(db.DateTime(timezone=True), server_default=func.now(),
                      nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    deadline = db.Column(db.DateTime(timezone=True), nullable=True)


@dataclass
class Status(db.Model):
    id: str
    name: str

    id = db.Column(db.String(36), primary_key=True, default=generate_uuid,
                   unique=True)
    name = db.Column(db.String(200), nullable=False)


@dataclass
class SubItem(db.Model):
    id: str
    name: str
    title: str
    description: str
    id_item: List[str]
    deadline: datetime
    opened_by: datetime
    status: str
    name_file: str
    attachments: JSON
    tag: str
    amounts: JSON
    amounts_tag: JSON
    __allow_unmapped__ = True

    id = db.Column(db.String(36), primary_key=True, default=generate_uuid,
                   unique=True)
    name = db.Column(db.String(200), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    id_item = db.Column(db.ForeignKey('user.id'), nullable=False)
    deadline = db.Column(db.DateTime(timezone=True), nullable=True)
    opened_by = db.Column(db.DateTime(timezone=True), nullable=True)
    status = db.Column(db.String(50), nullable=True, default='todo')
    name_file = db.Column(db.String(200), nullable=False)
    attachments = db.Column(db.JSON, nullable=True)
    tag = db.Column(db.String(200), nullable=True)
    amounts = db.Column(db.JSON, nullable=True)
    amounts_tag = db.Column(db.JSON, nullable=True)


@dataclass
class User(db.Model):
    id: str
    name: str
    password: str
    email: str
    full_name: str

    id = db.Column(db.String(36), primary_key=True, default=generate_uuid,
                   unique=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    full_name = db.Column(db.String(100), nullable=True)


@dataclass
class Video(db.Model):
    id: str
    name: str
    category: str
    author: str
    link: str
    topic: str
    version: str
    date_publication: str
    __allow_unmapped__ = True

    id = db.Column(db.String(36), primary_key=True, default=generate_uuid,
                   unique=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    category = db.Column(db.String(100), db.ForeignKey('category.id'),
                         nullable=False)
    author = db.Column(db.String(100), db.ForeignKey('author.id'),
                       nullable=False)
    link = db.Column(db.String(250), nullable=True)
    topic = db.Column(db.String(255), nullable=True)
    version = db.Column(db.String(100), nullable=True)
    date_publication = db.Column(db.DateTime(timezone=True), nullable=True)

