# Magalcar

Magalcar est une application web de gestion et de réservation de véhicules développée avec Django.

## Objectif

Faciliter la gestion des véhicules et des réservations grâce à une plateforme web centralisée.

## Technologies utilisées

- **Backend :** Python, Django
- **Base de données :** SQLite
- **Frontend :** HTML, CSS, JavaScript
- **Gestion des médias :** Django Media

## Structure du projet

- `backend/config/` : configuration du projet Django
- `backend/vehicules/` : application liée aux véhicules
- `backend/reservations/` : gestion des réservations
- `backend/paiements/` : fonctionnalités liées aux paiements
- `backend/website/` : fonctionnalités du site web

## Installation

1. Cloner le dépôt :

   ```bash
   git clone https://github.com/kyadkp/Magalcar.git
   ```

2. Accéder au dossier du backend :

   ```bash
   cd Magalcar/backend
   ```

3. Créer et activer un environnement virtuel.

4. Installer les dépendances :

   ```bash
   pip install -r requirements.txt
   ```

5. Configurer les variables d'environnement dans un fichier `.env`, notamment `DJANGO_SECRET_KEY`.

6. Lancer les migrations :

   ```bash
   python manage.py migrate
   ```

7. Démarrer le serveur :

   ```bash
   python manage.py runserver
   ```

## Statut

Projet en cours de développement.
