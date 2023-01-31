from flask import Flask
from handlers.routes import configure_routes
from utils.db import db
from utils.env import SQLALCHEMY_DATABASE_URI

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
db.init_app(app)

configure_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
