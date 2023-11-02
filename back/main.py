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

    def __iter__(self):
        for each in list(self.__dict__.values())[1:][::-1]:
            yield each

    def name_value(self):
        for each in list(self.__dict__.keys())[1:]:
            yield each

@app.route('/v1/api/')
def health():
    all_name_and_pictures = Test.query.all()
    names = ['id', 'name']
    return render_template('data.html', objects=all_name_and_pictures, name='Test22', names=names)


if __name__ == '__main__':
    app.run(debug=True)
