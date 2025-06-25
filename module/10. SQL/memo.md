# Memo : Base de Donnée

## Culture
<ins>Base de Donnée :</ins>


<ins>Bases de données relationnelle (RDBMS) :</ins> table où les données sont organisées en lignes et colonnes, idéal pour transactions complexes et une forte consistance des données. Défaut : Scalabité horizontal
- exemples :   MySQL, PostgreSQL, Oracle

<ins>Bases de données Columnar (RDBMS) :</ins> table où il y a beacoup de collones colonnes, idéal pour aggrégations de lignes, data science
- exemples :   Cassandra, Hbase, Bigquery, Redshift

<ins>Bases de données NoSQL :</ins> système clé-valeur (Redis) pour les données, idéal pour  accés rapide à une donnée, scalabilité horizontale, gros volume de donnée.
 - exemples :   MongoDB, Reddis

<ins> Base de données de Graph :</ins>
ex: Neo4j, Neptune, Arangodb

<ins>Bases de données Distribuées :</ins> La gestion est traitée par un réseaux de noeux (ordinateur) interconnecté qui stock les données de manière distribuée.
 - exemples :   Amazon DynamoDB, H2(en Java, pour le test et dev)


<ins>TimeSeries Data Base (TSDB) :</ins> Idea pour les valeurs capté dans le temps, bonne compression pour les données qui évoluent peu, pas de modification possible à part la compaction ex. Prometheus, Grafite, Influxdb 

<ins>Base de donnée Vectorielle :</ins> optimisé pour vecteur de chiffre pour application IA, search engine  ex. Pinecone, Weaviate, Qdrant

PostgreSQL peut utliser les relational querry (SQL) et les  non-relational querry (JSON)

<div>Exemple : JSON</div> 


```JSON
{
    "menu": {
        "id": "file",
        "value": "File",
        "popup": {
            "menuitem": [
                { "value": "New", "onclick": "CreateNewDoc()" },
                { "value": "Open", "onclick": "OpenDoc()" },
                { "value": "Close", "onclick": "CloseDoc()" }
            ]
        }
    }
}
```
CAP Theorem:
Il est impossible pour un système de BDD distribuée de garantir simultanément:
1. Consistency (Cohérence) : Tous les nœuds voient les mêmes données au même moment. Une lecture garantit de retourner le résultat de la dernière écriture.
2. Availability (Disponibilité) : Chaque requête reçoit une réponse, sans garantie que cette réponse soit la plus récente. Le système est opérationnel et répond aux requêtes même en cas de panne de certains nœuds.
3. Partition Tolerance (Tolérance aux partitions): Le système continue de fonctionner malgré des partitions réseau. Les nœuds peuvent être divisés en plusieurs groupes qui ne peuvent pas communiquer entre eux.

Utiliser Postgre en ligne de commande
```bash
(base) tmari@PYTHON-02:/etc/apt/sources.list.d$39,16:09$sudo su - postgres
postgres@PYTHON-02:~$ psql
psql (16.9 (Ubuntu 16.9-0ubuntu0.24.04.1))
Type "help" for help.

postgres=# 
```

Client SQL pgAdmin 4 (GUI)

## Méthode Merise
| Code Mnémonique       | Column 2      | Column 1      | Column 2      |
| -------------         | ------------- | ------------- | ------------- 
| latitude              | Cell 2, Row 1 | Cell 1, Row 1 | Cell 1, Row 1 |
| longitude             | Cell 1, Row 2 | Cell 1, Row 1 | Cell 1, Row 1 |


## SQL and querry
```SQL
CREATE TABLE cars (
  brand VARCHAR(255),
  model VARCHAR(255),
  year INT
); 
```

