import os
import uuid
from dataclasses import dataclass

import psycopg2
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
pg_user = "postgres"
pg_pwd = "qawsed"
pg_port = "5432"
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{pg_user}:{pg_pwd}@localhost:{pg_port}/my-crm-basic"
# app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL",
#                                                   "postgresql://localhost:5432/my-crm-basic")  # 'postgresql://postgres:postgres@<PORT>:<PORT>/<DB_NAME>'
db = SQLAlchemy(app)

conn = psycopg2.connect(database='my-crm-basic', user='postgres', password='qawsed')
def generate_uuid():
    return str(uuid.uuid4())


@dataclass
class Test(db.Model):
    id: str
    title: str

    id = db.Column(db.String(36), primary_key=True, default=generate_uuid,
                   unique=True)
    title = db.Column(db.String(255), nullable=False)


@app.route('/v1/api/')
def health():
    all_name_and_pictures = Test.query.all()
    return render_template('index.html', objects=all_name_and_pictures)


if __name__ == '__main__':
    app.run(debug=True)
