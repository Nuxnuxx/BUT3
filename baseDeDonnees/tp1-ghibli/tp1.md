# Exercice 1

1. C
2. B
3. C
4. B
5. B
6. ACID
7. Vrai
8. Non redondantes, non nulles, Atomiques
9. Insert update et delete et pas les autres qui modifie la base
10. Horizontale

# Exercice 2

1. Une base de données est une collection organisée de données structurées de manière à permettre un accès, une gestion et une mise à jour efficaces. Elle stocke des informations qui peuvent être récupérées, manipulées et gérées selon des besoins spécifiques.

2. Organisation des données : Les bases de données permettent de structurer les données de manière logique.
Accès rapide : Elles offrent des moyens efficaces pour récupérer et manipuler les données rapidement.
Sécurité des données : Les systèmes de gestion de bases de données offrent des mécanismes de sécurité pour protéger les données sensibles.
Intégrité des données : Ils garantissent la cohérence et la précision des données.
Évolutivité : Les bases de données peuvent être mises à l'échelle pour s'adapter à de grandes quantités de données.

3. Les requêtes SQL, ou Structured Query Language, sont utilisées pour interagir avec les bases de données. Elles servent à effectuer diverses opérations telles que l'insertion, la modification, la suppression et la récupération de données stockées dans une base de données relationnelle. Les requêtes SQL permettent aux utilisateurs et aux programmes d'accéder aux données de manière structurée en utilisant des commandes spécifiques telles que SELECT, INSERT, UPDATE et DELETE.

En résumé, les requêtes SQL sont utilisées pour :

Récupérer des données : Avec des commandes SELECT, vous pouvez extraire des informations spécifiques d'une base de données.

Mettre à jour des données : Les commandes UPDATE permettent de modifier les données existantes dans la base de données.

Insérer de nouvelles données : Les commandes INSERT permettent d'ajouter de nouvelles lignes de données dans une table.

Supprimer des données : Les commandes DELETE permettent de retirer des lignes de données de la base de données.

En somme, les requêtes SQL sont essentielles pour gérer, manipuler et récupérer des données stockées dans des bases de données relationnelles, ce qui les rend cruciales dans le développement d'applications et dans la gestion des systèmes d'information.

4. La principale différence entre SQL (Structured Query Language) et NoSQL réside dans la manière dont ils abordent la gestion des données :

SQL (Bases de données relationnelles) :

Structure : Les bases de données relationnelles utilisent un schéma prédéfini et une structure tabulaire. Elles reposent sur des tables avec des lignes (enregistrements) et des colonnes (attributs) qui définissent les relations entre les données.
Langage : SQL est un langage utilisé pour manipuler et interroger ces bases de données relationnelles. Il suit des normes bien définies pour exécuter des opérations comme SELECT, INSERT, UPDATE et DELETE.
Consistance : Les bases de données relationnelles visent généralement la cohérence des données et suivent le principe ACID (Atomicité, Cohérence, Isolation, Durabilité).
NoSQL (Not Only SQL) :

Structure flexible : Les bases de données NoSQL adoptent une structure plus flexible, permettant de stocker différents types de données. Elles peuvent être basées sur des modèles comme les bases de données clé-valeur, de documents, de colonnes ou de graphes.
Scalabilité : Les bases de données NoSQL sont souvent conçues pour être facilement évolutives, horizontalement (ajout de nœuds) ou verticalement (ajout de capacités au nœud existant).
Consistance variable : Les bases de données NoSQL peuvent prioriser la disponibilité et la partition plutôt que la cohérence stricte des données, suivant le théorème CAP (Consistency, Availability, Partition tolerance). Elles offrent souvent une consistance eventual (éventuelle) plutôt qu'une consistance stricte comme dans les bases de données relationnelles.
En résumé, SQL se concentre sur des bases de données structurées, rigides et fortement normalisées, tandis que NoSQL offre une approche plus souple et évolutive, adaptée à une variété de types de données et à des besoins de traitement massivement distribués. Le choix entre SQL et NoSQL dépend des besoins spécifiques d'une application en termes de structure des données, de scalabilité, de performances et de tolérance aux pannes.


5. 
Les bases de données NoSQL sont généralement regroupées en quatre grandes familles en fonction de leur modèle de stockage des données :

Bases de données de type Clé-Valeur :

Elles stockent les données sous forme de paires clé-valeur, où chaque élément est associé à une clé unique. Ces systèmes offrent une récupération rapide des données mais sont souvent limités en termes de requêtes complexes.
Exemples : Redis, DynamoDB, Riak.
Bases de données de type Documents :

Elles stockent les données sous forme de documents, généralement au format JSON, XML ou BSON, où chaque document peut contenir un ensemble de paires clé-valeur.
Exemples : MongoDB, Couchbase, CouchDB.
Bases de données de type Colonnes :

Elles stockent les données dans des colonnes plutôt que dans des lignes, ce qui permet une récupération efficace des données par colonne plutôt que par ligne entière. Elles sont souvent utilisées pour des cas où il est nécessaire d'analyser de grandes quantités de données.
Exemples : Cassandra, HBase, Google Bigtable.
Bases de données de type Graphes :

Elles sont conçues pour stocker des informations sous forme de graphes, où les données sont représentées sous forme de nœuds, d'arêtes et de propriétés. Ces bases de données sont excellentes pour modéliser des relations complexes entre les données.
Exemples : Neo4j, Amazon Neptune, ArangoDB.
Chaque famille de bases de données NoSQL a ses propres avantages et inconvénients, et le choix dépend souvent des besoins spécifiques de l'application, de la nature des données à stocker et de la manière dont elles seront manipulées. Certains systèmes NoSQL peuvent également présenter des caractéristiques hybrides, combinant les aspects de plusieurs familles pour répondre à des besoins plus complexes.

# Exercice 3
