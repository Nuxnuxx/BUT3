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

# Thomas's tasks
create_task "Initialisation Projet Git" "Mise en place du repo Git avec une stratégie de branching adaptée. Références : [Git Branching Model](https://nvie.com/posts/a-successful-git-branching-model/)" "2024-01-02" "2024-01-03" "Thomas"
create_task "Design de la Base de Données" "Élaboration du schéma de la DB. Références: [Conception MongoDB](https://www.mongodb.com/basics)" "2024-01-04" "2024-01-06" "Thomas"
create_task "Initialisation du Backend" "Configuration de l'environnement Node.js et intégration de MongoDB." "2024-01-09" "2024-01-13" "Thomas"
create_task "API CRUD" "Développement des routes CRUD pour les principales entités." "2024-01-16" "2024-01-23" "Thomas"
create_task "Optimisation du Backend" "Revue du code, refactoring et optimisations diverses." "2024-01-24" "2024-01-30" "Thomas"
create_task "Mise en Production du Backend" "Déploiement du backend et configuration des variables d'environnement." "2024-01-31" "2024-02-05" "Thomas"

# Tom's tasks
create_task "Configuration React" "Initialisation de l'appli React avec routing via React-Router. Références : [React Routing](https://reactrouter.com/)" "2024-01-04" "2024-01-05" "Tom"
create_task "Wireframing & Design" "Création des maquettes initiales de l'application." "2024-01-06" "2024-01-10" "Tom"
create_task "Développement Components React" "Création des components nécessaires pour les principales fonctionnalités." "2024-01-11" "2024-01-17" "Tom"
create_task "Intégration API" "Connecter le frontend avec l'API développée par Thomas." "2024-01-18" "2024-01-26" "Tom"
create_task "Tests et Refinements UI" "Tests UI et apport des ajustements nécessaires." "2024-01-27" "2024-02-02" "Tom"
create_task "Mise en Production du Frontend" "Déploiement du frontend sur une plateforme d'hébergement." "2024-02-03" "2024-02-07" "Tom"

# Kevin's tasks
create_task "Stratégie de Test" "Définition des méthodologies de test et rédaction du plan de test. Références: [Plan de Test Agile](https://www.softwaretestinghelp.com/agile-test-plan-template/)" "2024-01-04" "2024-01-06" "Kevin"
create_task "Tests Unitaires Backend" "Écriture et exécution de tests pour les routes CRUD." "2024-01-09" "2024-01-14" "Kevin"
create_task "Tests d'Intégration" "Tests pour vérifier l'intégration correcte entre le frontend et le backend." "2024-01-15" "2024-01-22" "Kevin"
create_task "Tests UI/UX" "S'assurer que l'interface est intuitive et que le design est cohérent." "2024-01-23" "2024-01-29" "Kevin"
create_task "Revue des Tests et Ajustements" "Revue des tests, identification des problèmes et coordination avec Tom et Thomas pour les résoudre." "2024-01-30" "2024-02-04" "Kevin"
create_task "Préparation pour la Mise en Production" "S'assurer que tout est prêt pour le déploiement, tant pour le frontend que pour le backend." "2024-02-05" "2024-02-08" "Kevin"

# Réunions d'équipe hebdomadaires pour la coordination et le feedback
create_task "Réunion d'équipe 1" "Discussion sur les avancées de la première semaine et planification de la semaine suivante." "2024-01-06" "2024-01-06" "Équipe"
create_task "Réunion d'équipe 2" "Discussion sur les avancées de la deuxième semaine et planification de la semaine suivante." "2024-01-13" "2024-01-13" "Équipe"
create_task "Réunion d'équipe 3" "Discussion sur les avancées de la troisième semaine et planification de la semaine suivante." "2024-01-20" "2024-01-20" "Équipe"
create_task "Réunion d'équipe 4" "Discussion sur les avancées de la quatrième semaine et planification de la semaine suivante." "2024-01-27" "2024-01-27" "Équipe"
create_task "Réunion d'équipe 5" "Discussion sur les avancées de la cinquième semaine et préparation pour la mise en production." "2024-02-03" "2024-02-03" "Équipe"
