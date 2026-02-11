Voici le contenu du fichier README.md rédigé de manière sobre et professionnelle, sans emojis, pour faciliter l'évaluation par votre professeur.

Projet Authentification Star Wars
Ce projet consiste en une application Web d'authentification sécurisée développée avec Python et le framework Flask. Il met en oeuvre une base de données relationnelle pour la gestion des utilisateurs.

Caractéristiques Techniques
Gestion de la Base de Données : Utilisation de SQLite via l'ORM SQLAlchemy pour garantir l'intégrité des données et prévenir les injections SQL.

Sécurité des Identifiants : Les mots de passe ne sont jamais stockés en clair. Le système utilise un hachage cryptographique via werkzeug.security pour protéger les données utilisateurs.

Interface Utilisateur : Design thématique Star Wars utilisant des styles CSS modernes et le moteur de template Jinja2 pour l'affichage dynamique des messages de retour.

Guide d'Installation
1. Prérequis
Python 3 doit être installé sur la machine.

2. Installation des dépendances
Ouvrez un terminal dans le répertoire du projet et exécutez la commande suivante :

Bash
pip install flask flask-sqlalchemy
3. Lancement de l'application
Exécutez le script principal :

Bash
python app.py
Le serveur sera accessible à l'adresse locale suivante : http://127.0.0.1:5000

Structure du Projet
app.py : Contient la configuration du serveur, la définition du modèle de données et la logique de traitement des formulaires.

templates/index.html : Structure HTML du formulaire de connexion et d'inscription.

static/style.css : Feuilles de style pour le rendu visuel de l'interface.

starwars.db : Fichier de base de données SQLite généré automatiquement à la racine du projet lors du premier enregistrement.

Procédure de Test
Saisissez un identifiant et un mot de passe, puis cliquez sur le bouton de création de compte.

Vérifiez la création de la ligne correspondante dans la base de données.

Testez la connexion avec les identifiants créés pour valider le processus d'authentification.
