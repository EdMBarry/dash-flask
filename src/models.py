from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True,
                   unique=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

class User(Base):
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(300), unique=True)


    def __repr__(self):
        return self.username


class Project(Base):
    title = db.Column(db.String(200))
    location = db.Column(db.String(200))
    funding_category = db.Column(db.String(200))
    portfolio_owner = db.Column(db.String(200))
    certainty = db.Column(db.Integer)
    expected_start = db.Column(db.Date)

