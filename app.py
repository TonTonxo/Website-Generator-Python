from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from utils import generate_user_template  # Import the function
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///links.db'
db = SQLAlchemy(app)

class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    url = db.Column(db.String(200))
    name = db.Column(db.String(50))  # User's name
    bio = db.Column(db.String(200))  # User's bio or description

# Create the database tables within the application context
with app.app_context():
    db.create_all()

# Route to display links and add a new link
@app.route('/')
def index():
    links = Link.query.all()
    return render_template('index.html', links=links)

@app.route('/add_link', methods=['POST'])
def add_link():
    title = request.form['title']
    url = request.form['url']
    name = request.form['name']
    bio = request.form['bio']

    new_link = Link(title=title, url=url, name=name, bio=bio)
    db.session.add(new_link)
    db.session.commit()

    # Generate HTML template for the user
    generate_user_template(new_link)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5001)
    
migrate = Migrate(app, db)