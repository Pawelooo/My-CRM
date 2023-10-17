from back.resume.models import app

import psycopg2
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, JSON, Column, UUID, String, DateTime, \
    Integer
from back.resume import routes








if __name__ == "__main__":
    app.run(debug=True)
