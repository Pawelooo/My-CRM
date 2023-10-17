
import psycopg2
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
pg_user = "postgres"
pg_pwd = "qawsed"
pg_port = "5432"
app.config[
    "SQLALCHEMY_DATABASE_URI"] = f"postgresql://{pg_user}:{pg_pwd}@localhost:{pg_port}/my-crm-basic"
db = SQLAlchemy(app)
conn = psycopg2.connect(database='my-crm-basic', user='postgres',
                        password='qawsed')


if __name__ == "__main__":
    app.run(debug=True)
