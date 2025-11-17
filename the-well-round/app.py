from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy 
import os

app = Flask(__name__)

#Set database for tracking 
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'wellround.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

if __name__== "__main__":
    if not os.path.exists('wellround.db'):
        with app.app_context():
            db.create_all()
    app.run(debug=True)