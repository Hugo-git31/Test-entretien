# Application de gestion de données géographiques (Rest Countries)
Vidéo de présentation : https://docs.google.com/videos/d/1jYXhtYuBfZCUoCrQ0-ryyjaMKSnNBPBSDJUekDKCsbY/edit?usp=sharing
Ce projet est une application Django permettant d'importer, de consulter et d'analyser les données des pays du monde via l'API Rest Countries.

## Fonctionnalités principales

- Importation des données via une commande de gestion personnalisée.
- Liste des pays avec pagination, recherche par nom et filtrage par région.
- Fiche détaillée pour chaque pays.
- Page de statistiques (Top 10 population/superficie et répartition par région).
- Fonctionnement autonome sur base de données locale après importation.

## Architecture technique

L'application repose sur le framework Django. Le modèle de données est structuré autour du code CCA3 (ISO 3166-1 alpha-3) utilisé comme clé primaire pour garantir l'unicité des enregistrements et faciliter les jointures lors des mises à jour.

- Backend : Django 6.0
- Base de données : SQLite
- Ingestion : Script de gestion utilisant la bibliothèque Requests

## Installation

1. Cloner le dépôt :
   git clone git@github.com:Hugo-git31/Test-entretien.git

2. Créer un environnement virtuel et l'activer :
   python3 -m venv venv
   source venv/bin/activate

3. Installer les dépendances :
   pip install -r requirements.txt

4. Appliquer les migrations :
   python manage.py migrate

## Utilisation

### Importation des données
Pour peupler la base de données locale depuis l'API externe, exécutez la commande suivante :
python manage.py import_countries

### Lancement du serveur
Lancez le serveur de développement :
python manage.py runserver

L'interface est accessible à l'adresse suivante : http://127.0.0.1:8000/
