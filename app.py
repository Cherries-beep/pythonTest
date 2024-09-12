from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///VikaProject.db'
db = SQLAlchemy(app)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(30), nullable = False)
    text = db.Column(db.Text, nullable = False)

@app.route('/')
@app.route('/mainPage')
def mainPage():
    return render_template('mainPage.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/create')
def create():
    return render_template('create.html')




if __name__== '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)
