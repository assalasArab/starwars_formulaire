# starwars_formulaire
Ce projet est un formulaire de connexion thématique Star Wars réalisé avec **Python** et **Flask**. Il démontre la mise en place d'une base de données sécurisée
# 🌌 Star Wars Login - TP Authentification Sécurisée

Ce projet est un formulaire de connexion thématique Star Wars réalisé avec **Python** et **Flask**. Il démontre la mise en place d'une base de données sécurisée.

## 🚀 Fonctionnalités
- **Thème Star Wars** : Interface futuriste avec effets de néon (Jedi/Sith).
- **Sécurité SQL** : Utilisation de SQLAlchemy (ORM) pour bloquer les injections SQL.
- **Cryptage des mots de passe** : Hachage sécurisé via `werkzeug.security` (PBKDF2 avec SHA256).
- **Gestion BDD** : Base de données SQLite légère (`starwars.db`).
- **Actions** : Inscription de nouveaux comptes et vérification de connexion.

## 🛠️ Installation et Lancement

1. **Cloner le projet**
   ```bash
   git clone [https://github.com/ton-pseudo/starwars-login.git](https://github.com/ton-pseudo/starwars-login.git)
   cd starwars-login
