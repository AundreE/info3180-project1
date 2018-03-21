from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "Sup3r$3cretkey"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://mjoomqxakjxlqv:41ace61573f6fed8a70249d4c084aee70e952b4b82afe5af5c1e1bf0555f9a24@ec2-54-221-212-15.compute-1.amazonaws.com:5432/da5hl5ne5q1j5v"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config['UPLOAD_FOLDER'] = './app/static/uploads'
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg', 'gif'])
allowed_extensions = app.config['ALLOWED_EXTENSIONS']
db = SQLAlchemy(app)
app.config.from_object(__name__)
from app import views
