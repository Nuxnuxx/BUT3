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

    RESPONSE=$(curl -s -H "Authorization: Bearer $TOKEN" \
                   -H "Content-Type: application/json" \
                   -X POST https://app.asana.com/api/1.0/tasks \
                   -d "$JSON_PAYLOAD")

    echo "$RESPONSE" | jq -r '.data.gid'
}

# Function to add a dependency between two tasks
add_dependency() {
    DEPENDENT_TASK_GID="$1"
    DEPENDED_ON_TASK_GID="$2"

    curl -s -H "Authorization: Bearer $TOKEN" \
         -H "Content-Type: application/json" \
         -X POST https://app.asana.com/api/1.0/tasks/$DEPENDENT_TASK_GID/addDependencies \
         -d "{\"data\": {\"dependencies\": [\"$DEPENDED_ON_TASK_GID\"]}}"
}

ENV_SETUP_GID=$(create_task "Configuration de l'Environnement" "Thomas: Installer Node.js, initialiser npm pour le développement backend, et configurer ESLint pour le linting de code.\nTo-Do: Installer Node.js, npm init, Installer ESLint\nExigences: Node.js v14+\nDocumentation: https://nodejs.org/en/docs/" "2024-01-02" "2024-01-05" "Thomas")

WIREFRAME_GID=$(create_task "Maquettage" "Tom: Concevoir des maquettes initiales avec Figma pour les pages principales de l'application, y compris le login, l'inscription et le tableau de bord.\nTo-Do: Utiliser Figma pour créer des maquettes\nExigences: Figma\nDocumentation: https://help.figma.com/hc/fr/articles/360039839513" "2024-01-08" "2024-01-12" "Tom")

DRAFT_TEST_GID=$(create_task "Ébauche de la Stratégie de Test" "Kevin: Ébaucher une stratégie de test complète. Mettre en évidence les scénarios de test, les cas limites et configurer Jest pour les tests.\nTo-Do: Écrire la stratégie de test, Installer Jest\nExigences: Connaissance en Jest\nDocumentation: https://jestjs.io/docs/getting-started" "2024-01-15" "2024-01-19" "Kevin")
add_dependency "$DRAFT_TEST_GID" "$WIREFRAME_GID"

MONGO_SETUP_GID=$(create_task "Configuration de MongoDB" "Thomas: Installer MongoDB, configurer les bases de données initiales et écrire des définitions de schéma pour les collections.\nTo-Do: Installer MongoDB, écrire des schémas\nExigences: MongoDB\nDocumentation: https://docs.mongodb.com/manual/installation/" "2024-01-22" "2024-01-26" "Thomas")
add_dependency "$MONGO_SETUP_GID" "$ENV_SETUP_GID"

FRONTEND_INIT_GID=$(create_task "Initialisation du Frontend" "Tom: Initialiser le projet React en utilisant create-react-app et configurer le routage avec React Router.\nTo-Do: Utiliser create-react-app, configurer React Router\nExigences: React.js\nDocumentation: https://reactjs.org/docs/create-a-new-react-app.html#create-react-app" "2024-01-29" "2024-02-02" "Tom")
add_dependency "$FRONTEND_INIT_GID" "$WIREFRAME_GID"

API_DESIGN_GID=$(create_task "Conception de l'API" "Thomas: Concevoir et documenter les points de terminaison de l'API RESTful en utilisant Swagger.\nTo-Do: Utiliser Swagger pour la documentation de l'API\nExigences: Swagger\nDocumentation: https://swagger.io/docs/" "2024-02-05" "2024-02-09" "Thomas")
add_dependency "$API_DESIGN_GID" "$MONGO_SETUP_GID"

UNIT_TEST_GID=$(create_task "Configuration des Tests Unitaires" "Kevin: Configurer les tests unitaires avec Jest et écrire les tests unitaires initiaux pour les fonctions utilitaires.\nTo-Do: Écrire des tests unitaires\nExigences: Jest\nDocumentation: https://jestjs.io/docs/getting-started" "2024-02-12" "2024-02-16" "Kevin")
add_dependency "$UNIT_TEST_GID" "$DRAFT_TEST_GID"

API_IMPL_GID=$(create_task "Implémentation de l'API" "Thomas: Commencer à implémenter les points de terminaison de l'API et à les intégrer avec MongoDB.\nTo-Do: Implémenter des points de terminaison\nExigences: Node.js, MongoDB\nDocumentation: https://expressjs.com/en/guide/routing.html" "2024-02-19" "2024-02-23" "Thomas")
add_dependency "$API_IMPL_GID" "$API_DESIGN_GID"

FRONTEND_DEV_GID=$(create_task "Développement du Frontend" "Tom: Commencer le développement des composants et des pages frontend en fonction des maquettes.\nTo-Do: Développer des composants React\nExigences: React.js\nDocumentation: https://reactjs.org/docs/components-and-props.html" "2024-02-26" "2024-03-02" "Tom")
add_dependency "$FRONTEND_DEV_GID" "$FRONTEND_INIT_GID"

INTEG_TEST_GID=$(create_task "Tests d'Intégration" "Kevin: Mettre en œuvre des tests d'intégration pour s'assurer que l'API et la base de données fonctionnent correctement ensemble.\nTo-Do: Écrire des tests d'intégration\nExigences: Postman, Jest\nDocumentation: https://www.postman.com/api-documentation-tool/" "2024-03-05" "2024-03-09" "Kevin")
add_dependency "$INTEG_TEST_GID" "$UNIT_TEST_GID"
add_dependency "$INTEG_TEST_GID" "$API_IMPL_GID"

AUTH_IMPL_GID=$(create_task "Implémentation de l'Authentification" "Thomas: Implémenter l'authentification basée sur JWT sur le backend.\nTo-Do: Implémenter JWT\nExigences: JWT\nDocumentation: https://jwt.io/introduction/" "2024-03-12" "2024-03-16" "Thomas")
add_dependency "$AUTH_IMPL_GID" "$API_IMPL_GID"

FRONTEND_AUTH_GID=$(create_task "Authentification Frontend" "Tom: Implémenter la logique et l'interface utilisateur d'authentification frontend.\nTo-Do: Implémenter le flux d'authentification frontend\nExigences: React.js\nDocumentation: https://reactjs.org/docs/hooks-intro.html" "2024-03-20" "2024-03-24" "Tom")
add_dependency "$FRONTEND_AUTH_GID" "$AUTH_IMPL_GID"

TEST_FIX_GID=$(create_task "Corrections de Tests" "Kevin: Résoudre les tests échoués et mettre à jour les cas de tests au besoin.\nTo-Do: Corriger les tests échoués\nExigences: Jest\nDocumentation: https://jestjs.io/docs/troubleshooting" "2024-03-27" "2024-03-31" "Kevin")
add_dependency "$TEST_FIX_GID" "$INTEG_TEST_GID"

FRONTEND_TEST_GID=$(create_task "Tests Frontend" "Kevin: Commencer la création de tests frontend en utilisant Jest et React Testing Library.\nTo-Do: Écrire des tests frontend\nExigences: Jest, React Testing Library\nDocumentation: https://testing-library.com/docs/" "2024-04-03" "2024-04-07" "Kevin")
add_dependency "$FRONTEND_TEST_GID" "$FRONTEND_AUTH_GID"

DATABASE_OPT_GID=$(create_task "Optimisation de la Base de Données" "Thomas: Optimiser les collections, les requêtes et les index MongoDB.\nTo-Do: Optimiser MongoDB\nExigences: MongoDB\nDocumentation: https://docs.mongodb.com/manual/optimization/" "2024-04-10" "2024-04-14" "Thomas")
add_dependency "$DATABASE_OPT_GID" "$AUTH_IMPL_GID"

FRONTEND_POLISH_GID=$(create_task "Polissage du Frontend" "Tom: Affiner l'UI, effectuer des tests d'utilisabilité et mettre en œuvre des modifications de feedback.\nTo-Do: Peaufiner l'UI\nExigences: React.js, CSS\nDocumentation: https://reactjs.org/docs/optimizing-performance.html" "2024-04-17" "2024-04-21" "Tom")
add_dependency "$FRONTEND_POLISH_GID" "$FRONTEND_TEST_GID"

API_DOC_GID=$(create_task "Documentation de l'API" "Thomas: Documenter l'API à l'aide d'outils comme Swagger.\nTo-Do: Documenter l'API\nExigences: Swagger\nDocumentation: https://swagger.io/docs/" "2024-04-24" "2024-04-28" "Thomas")
add_dependency "$API_DOC_GID" "$DATABASE_OPT_GID"

STAGING_DEPLOY_GID=$(create_task "Déploiement en Environnement de Staging" "Kevin: Déployer l'application dans un environnement de préproduction et effectuer des tests.\nTo-Do: Déploiement et tests en staging\nExigences: Docker, Kubernetes\nDocumentation: https://kubernetes.io/docs/tutorials/" "2024-05-01" "2024-05-05" "Kevin")
add_dependency "$STAGING_DEPLOY_GID" "$API_DOC_GID"
add_dependency "$STAGING_DEPLOY_GID" "$FRONTEND_POLISH_GID"

PROD_DEPLOY_GID=$(create_task "Déploiement en Production" "Thomas: Gérer le déploiement dans l'environnement de production.\nTo-Do: Déploiement en production\nExigences: AWS, Docker\nDocumentation: https://aws.amazon.com/getting-started/hands-on/deploy-docker-containers/" "2024-05-08" "2024-05-12" "Thomas")
add_dependency "$PROD_DEPLOY_GID" "$STAGING_DEPLOY_GID"

MONITORING_SETUP_GID=$(create_task "Configuration de la Surveillance" "Kevin: Mettre en place la surveillance et la journalisation pour l'environnement de production.\nTo-Do: Configurer Grafana et Prometheus\nExigences: Grafana, Prometheus\nDocumentation: https://grafana.com/docs/grafana/latest/getting-started/" "2024-05-15" "2024-05-19" "Kevin")
add_dependency "$MONITORING_SETUP_GID" "$PROD_DEPLOY_GID"

FINAL_REPORT_GID=$(create_task "Rapport Final du Projet" "Tom: Générer des rapports finaux sur l'achèvement du projet, les performances et les suggestions futures.\nTo-Do: Rédiger le rapport final\nExigences: LaTeX, Microsoft Word\nDocumentation: https://www.latex-project.org/" "2024-03-19" "2024-03-23" "Tom")
