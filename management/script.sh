#!/bin/bash

# Define your Personal Access Token and Project ID from Asana
TOKEN="1/1205490882856885:e85f31b796d373533c7717127b01798c"
PROJECT_ID="1205491108290307"

# Function to retrieve the GID of a section based on its name
get_section_gid() {
    SECTION_NAME=$1
    curl -s -H "Authorization: Bearer $TOKEN" \
    "https://app.asana.com/api/1.0/projects/$PROJECT_ID/sections" | jq -r ".data[] | select(.name == \"$SECTION_NAME\") | .gid"
}

# Fetch GIDs for Thomas, Tom, and Kevin sections
THOMAS_GID=$(get_section_gid "Thomas")
TOM_GID=$(get_section_gid "Tom")
KEVIN_GID=$(get_section_gid "Kevin")

# Function to create a task in Asana
create_task() {
    TASK_NAME="$1"
    TASK_NOTES="$2"
    TASK_START="$3"
    TASK_DUE="$4"
    SECTION_NAME="$5"

    case $SECTION_NAME in
        Thomas)
            SECTION_GID=$THOMAS_GID
            ;;
        Tom)
            SECTION_GID=$TOM_GID
            ;;
        Kevin)
            SECTION_GID=$KEVIN_GID
            ;;
        *)
            echo "Invalid section name provided"
            exit 1
    esac

    JSON_PAYLOAD=$(printf '{"data": {"name": "%s", "notes": "%s", "projects": ["%s"], "start_on": "%s", "due_on": "%s", "memberships": [{"project": "%s", "section": "%s"}]}}' "$TASK_NAME" "$TASK_NOTES" "$PROJECT_ID" "$TASK_START" "$TASK_DUE" "$PROJECT_ID" "$SECTION_GID")

    curl -s -H "Authorization: Bearer $TOKEN" \
         -H "Content-Type: application/json" \
         -X POST https://app.asana.com/api/1.0/tasks \
         -d "$JSON_PAYLOAD"
    echo $JSON_PAYLOAD
}

# Tâches pour Thomas (Backend Developer)
create_task "Initialisation du Projet Git" "Mise en place du repo Git avec une stratégie de branching. Références: [Git Branching Model](https://nvie.com/posts/a-successful-git-branching-model/)" "2024-01-02" "2024-01-02" "Thomas"
create_task "Installation de Node et Express" "Mise en place de Node.js et Express. Références: [Express.js](https://expressjs.com/fr/starter/installing.html)" "2024-01-03" "2024-01-04" "Thomas"
create_task "Design de la Base de Données MongoDB" "Conception du schéma de la DB. Références: [MongoDB Data Modeling](https://docs.mongodb.com/manual/core/data-modeling-introduction/)" "2024-01-07" "2024-01-10" "Thomas"
create_task "API CRUD pour MongoDB" "Création des routes CRUD pour les entités principales. Références: [MongoDB Node.js Driver](https://mongodb.github.io/node-mongodb-native/)" "2024-01-13" "2024-01-16" "Thomas"
create_task "Sécurisation de l'API" "Mise en place d'une authentification et d'une sécurisation des données. Références: [Passport.js](http://www.passportjs.org/)" "2024-01-17" "2024-01-18" "Thomas"
create_task "Optimisation de l'API" "Optimisation des requêtes et de la logique métier pour une meilleure performance." "2024-01-21" "2024-01-23" "Thomas"

# Tâches pour Tom (Frontend Developer)
create_task "Installation de React" "Mise en place du projet React. Références: [Create React App](https://fr.reactjs.org/docs/create-a-new-react-app.html)" "2024-01-03" "2024-01-04" "Tom"
create_task "Wireframing et Design des Composants" "Création des maquettes et design des principaux composants. Références: [React Components](https://fr.reactjs.org/docs/components-and-props.html)" "2024-01-07" "2024-01-10" "Tom"
create_task "Intégration API avec Axios" "Connexion du frontend avec le backend. Références: [Axios](https://axios-http.com/docs/intro)" "2024-01-13" "2024-01-14" "Tom"
create_task "Routage avec React-Router" "Mise en place du routage. Références: [React Router](https://reactrouter.com/)" "2024-01-15" "2024-01-16" "Tom"
create_task "Authentification et Session" "Gestion des sessions utilisateur et authentification. Références: [React Authentication](https://www.smashingmagazine.com/2020/01/authentication-react-apps/)" "2024-01-17" "2024-01-18" "Tom"
create_task "Optimisation des Performances Frontend" "Utilisation d'outils comme React Profiler pour optimiser les rendus." "2024-01-21" "2024-01-23" "Tom"

# Tâches pour Kevin (DevOps et Testeur)
create_task "Stratégie de Test" "Définition des méthodologies de test pour assurer la qualité. Références: [Software Testing Strategies](https://www.guru99.com/software-testing-strategies.html)" "2024-01-03" "2024-01-03" "Kevin"
create_task "Tests Unitaires Backend avec Jest" "Écriture de tests pour les routes CRUD. Références: [Jest](https://jestjs.io/)" "2024-01-17" "2024-01-19" "Kevin"
create_task "Tests Frontend avec React Testing Library" "Écriture de tests pour les composants React. Références: [React Testing Library](https://testing-library.com/)" "2024-01-20" "2024-01-22" "Kevin"
create_task "Mise en Place de la CI/CD" "Automatisation de l'intégration et du déploiement. Références: [Jenkins CI/CD](https://jenkins.io/doc/)" "2024-01-23" "2024-01-25" "Kevin"
create_task "Déploiement sur le Serveur" "Mise en production sur le serveur. Références: [DigitalOcean Deployment](https://www.digitalocean.com/community/tutorials)" "2024-01-28" "2024-01-30" "Kevin"
create_task "Maintenance et Monitoring" "Mise en place d'outils pour monitorer la performance et la stabilité du système." "2024-01-31" "2024-02-02" "Kevin"

