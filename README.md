# Projet Authentification Star Wars

Ce projet consiste en une application Web d'authentification sécurisée développée avec Python et le framework Flask. Il met en oeuvre une base de données relationnelle pour la gestion des utilisateurs.

## Caractéristiques Techniques
* **Gestion de la Base de Données** : Utilisation de SQLite via l'ORM SQLAlchemy pour garantir l'intégrité des données et prévenir les injections SQL.
* **Sécurité des Identifiants** : Les mots de passe ne sont jamais stockés en clair. Le système utilise un hachage cryptographique pour protéger les données utilisateurs.
* **Interface Utilisateur** : Design thématique Star Wars utilisant des styles CSS modernes et le moteur de template Jinja2 pour l'affichage dynamique des messages de retour.

## Guide d'Installation

### 1. Prérequis
Python 3 doit être installé sur la machine.

### 2. Installation des dépendances

Ouvrez un terminal dans le répertoire du projet et exécutez la commande suivante :
```bash
pip install flask flask-sqlalchemy
```
### 3. Lancement de l'application
Exécutez le script principal :
```bash
python app.py
```
## Le serveur sera accessible à l'adresse locale suivante : http://127.0.0.1:5000
