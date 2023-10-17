import uuid
from dataclasses import dataclass
from datetime import datetime
from app import db



def generate_uuid():
    return str(uuid.uuid4())


@dataclass
class Book(db.Model):
    __tablename__ = 'books'
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
    date_publish = db.Column(db.DateTime(timezone=True))