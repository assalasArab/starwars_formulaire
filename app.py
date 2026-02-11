from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ma_cle_secrete_intergalactique'
import os

# Détermine le chemin absolu du dossier où se trouve app.py
basedir = os.path.abspath(os.path.dirname(__file__))

# Force la base de données à se créer dans ce dossier précis
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'starwars.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    identifiant = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/auth', methods=['POST'])
def auth():
    identifiant = request.form.get('identifiant')
    password = request.form.get('password')
    action = request.form.get('action')

    if action == 'register':
        hashed_pw = generate_password_hash(password)
        new_user = User(identifiant=identifiant, password_hash=hashed_pw)
        try:
            db.session.add(new_user)
            db.session.commit()
            flash(f"Compte créé pour {identifiant} !", "success")
        except:
            flash("Erreur : Cet identifiant est déjà pris.", "error")

    elif action == 'login':
        user = User.query.filter_by(identifiant=identifiant).first()
        if user and check_password_hash(user.password_hash, password):
            flash(f"Bienvenue, {identifiant}. Que la Force soit avec vous.", "success")
        else:
            flash("Accès refusé. Identifiants invalides.", "error")

    return redirect(url_for('index')) # On revient toujours au formulaire

if __name__ == '__main__':
    app.run(debug=True)