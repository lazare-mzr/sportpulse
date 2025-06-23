from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
from functools import wraps
from flask import abort

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('LogIn'))
        return f(*args, **kwargs)
    return decorated_function

app = Flask(__name__, template_folder=("temp"))
app.secret_key = 'supersecretkey'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cart.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Cart {self.item_name}>'

@app.route('/home')
@login_required
def home():
    username = session.get('username')
    return render_template('index.html', username=username)

@app.route('/F1home')
@login_required
def F1home():
    return render_template('F1 Home.html')


@app.route('/F1drivers')
def F1drivers():
    return render_template('F1 Drivers.html')

@app.route('/F1races')
def F1races():
    return render_template("F1 Races.html")



@app.route('/LogIn', methods=['GET', 'POST'])
def LogIn():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['username'] = user.username
            flash("Login successful.")
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password')
            return redirect(url_for('LogIn'))

    return render_template("LogIn.html")

    return render_template("LogIn.html")

@app.route('/Registration', methods=['GET', 'POST'])
def Reg():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('LogIn'))

    return render_template("Registration.html")

@app.route('/logout')
@login_required
def logout():
    session.clear()
    flash("You have been logged out.")
    return redirect(url_for('LogIn'))



@app.route('/footballhome')
def index():
    return render_template('Football Home.html')

@app.route('/matches')
def matches():
    return render_template('matches.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/top-players')
def top_players():
    return render_template('top-players.html')

@app.route('/view-cart')
def view_cart():
    cart_items = Cart.query.all()
    total_price = sum(item.price for item in cart_items)
    return render_template('view-cart.html', cart_items=cart_items, total_price=total_price)

@app.route('/footballadd_to_cart', methods=['POST'])
def add_to_cart():
    item_name = request.form['item_name']
    price = request.form['price']
    
    new_item = Cart(item_name=item_name, price=int(price))
    db.session.add(new_item)
    db.session.commit()
    
    return redirect(url_for('shop'))

@app.route('/clear_cart', methods=['POST'])
def clear_cart():
    Cart.query.delete()
    db.session.commit()
    return redirect(url_for('view_cart'))

@app.route('/ufchome')
def ufchome():
    return render_template('ufc.html')

@app.route('/ufctopfighters')
def topfighters():
    return render_template('topfighters.html')

@app.route('/ufcevents')
def events():
    return render_template('events.html')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
