from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from models import db

app = Flask(__name__)
Bootstrap(app)

app.config.from_object('config')

db.init_app(app)
db.create_all(app=app)

@app.route("/")
def index():
    return render_template('index.html') 


if __name__ == "__main__":
    app.run(debug=True)
