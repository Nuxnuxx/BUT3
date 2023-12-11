## Exo 1

1. 2. test> use club_tennis
switched to db club_tennis
club_tennis> delete *

club_tennis> db.createCollection("joueurs")
{ ok: 1 }
club_tennis> db.joueurs.insertMany([
...     { id_joueur: 1, nom_joueur: "Dupont", prenom_joueur: "Alice", login: "alice", mdp: "1234" },
...     { id_joueur: 2, nom_joueur: "Durand", prenom_joueur: "Belina", login: "belina", mdp: "5694" },
...     { id_joueur: 3, nom_joueur: "Caron", prenom_joueur: "Camilia", login: "camilia", mdp: "9478" },
...     { id_joueur: 4, nom_joueur: "Dupont", prenom_joueur: "Dorine", login: "dorine", mdp: "1347" }
... ])
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6572e474883dfd1047ba1b42'),
    '1': ObjectId('6572e474883dfd1047ba1b43'),
    '2': ObjectId('6572e474883dfd1047ba1b44'),
    '3': ObjectId('6572e474883dfd1047ba1b45')
  }
}
club_tennis> db.createCollection("matchs")
{ ok: 1 }
club_tennis> db.createCollection("terrains")
{ ok: 1 }
club_tennis> db.createCollection("creneaux")
{ ok: 1 }
club_tennis> // Table matchs

club_tennis> db.matchs.insertMany([
...     { id_match: 2, date: "2020-08-01", id_creneau: 3, id_terrain: 1, id_joueur1: 2, id_joueur2: 3 },
...     { id_match: 3, date: "2020-08-02", id_creneau: 6, id_terrain: 2, id_joueur1: 1, id_joueur2: 3 },
...     { id_match: 4, date: "2020-08-02", id_creneau: 7, id_terrain: 2, id_joueur1: 2, id_joueur2: 4 },
...     { id_match: 5, date: "2020-08-08", id_creneau: 3, id_terrain: 3, id_joueur1: 1, id_joueur2: 2 },
...     { id_match: 6, date: "2020-08-08", id_creneau: 5, id_terrain: 2, id_joueur1: 3, id_joueur2: 4 }
... ])
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6572e4a0883dfd1047ba1b46'),
    '1': ObjectId('6572e4a0883dfd1047ba1b47'),
    '2': ObjectId('6572e4a0883dfd1047ba1b48'),
    '3': ObjectId('6572e4a0883dfd1047ba1b49'),
    '4': ObjectId('6572e4a0883dfd1047ba1b4a')
  }
}
club_tennis>

club_tennis> // Table terrains

club_tennis> db.terrains.insertMany([
...     { id_terrain: 2, nom_terrain: "gymnase synthétique", surface: "synthétique" },
...     { id_terrain: 3, nom_terrain: "hangar terre battue", surface: "terre battue" }
... ])
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6572e4a1883dfd1047ba1b4b'),
    '1': ObjectId('6572e4a1883dfd1047ba1b4c')
  }
}
club_tennis> db.matchs.insertMany([
...     { id_match: 2, date: "2020-08-01", id_creneau: 3, id_terrain: 1, id_joueur1: 2, id_joueur2: 3 },
...     { id_match: 3, date: "2020-08-02", id_creneau: 6, id_terrain: 2, id_joueur1: 1, id_joueur2: 3 },
...     { id_match: 4, date: "2020-08-02", id_creneau: 7, id_terrain: 2, id_joueur1: 2, id_joueur2: 4 },
...     { id_match: 5, date: "2020-08-08", id_creneau: 3, id_terrain: 3, id_joueur1: 1, id_joueur2: 2 },
...     { id_match: 6, date: "2020-08-08", id_creneau: 5, id_terrain: 2, id_joueur1: 3, id_joueur2: 4 }
... ])
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6572e4a5883dfd1047ba1b4d'),
    '1': ObjectId('6572e4a5883dfd1047ba1b4e'),
    '2': ObjectId('6572e4a5883dfd1047ba1b4f'),
    '3': ObjectId('6572e4a5883dfd1047ba1b50'),
    '4': ObjectId('6572e4a5883dfd1047ba1b51')
  }
}
club_tennis> db.terrains.insertMany([
...     { id_terrain: 2, nom_terrain: "gymnase synthétique", surface: "synthétique" },
...     { id_terrain: 3, nom_terrain: "hangar terre battue", surface: "terre battue" }
... ])
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6572e4a9883dfd1047ba1b52'),
    '1': ObjectId('6572e4a9883dfd1047ba1b53')
  }
}

club_tennis> db.creneaux.insertMany([
...     { id_creneau: 2, plage_horaire: "9h-10h" },
...     { id_creneau: 3, plage_horaire: "10h-11h" },
...     { id_creneau: 4, plage_horaire: "11h-12h" },
...     { id_creneau: 5, plage_horaire: "12h-13h" },
...     { id_creneau: 6, plage_horaire: "13h-14h" },
...     { id_creneau: 7, plage_horaire: "14h-15h" }
...     //... (insert the remaining data)
... ])
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6572e53a883dfd1047ba1b54'),
    '1': ObjectId('6572e53a883dfd1047ba1b55'),
    '2': ObjectId('6572e53a883dfd1047ba1b56'),
    '3': ObjectId('6572e53a883dfd1047ba1b57'),
    '4': ObjectId('6572e53a883dfd1047ba1b58'),
    '5': ObjectId('6572e53a883dfd1047ba1b59')
  }
}
club_tennis> db.creneaux.insertMany([
...     { id_creneau: 8, plage_horaire: "15h-16h" },
...     { id_creneau: 9, plage_horaire: "16h-17h" },
...     { id_creneau: 10, plage_horaire: "17h-18h" },
...     { id_creneau: 11, plage_horaire: "18h-19h" },
...     { id_creneau: 12, plage_horaire: "19h-20h" }
... ])
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6572e53d883dfd1047ba1b5a'),
    '1': ObjectId('6572e53d883dfd1047ba1b5b'),
    '2': ObjectId('6572e53d883dfd1047ba1b5c'),
    '3': ObjectId('6572e53d883dfd1047ba1b5d'),
    '4': ObjectId('6572e53d883dfd1047ba1b5e')
  }
}

3.

club_tennis> db.joueurs.find(
...   { nom_joueur: "Dupont" }, // Query to filter documents where nom_joueur is 'Dupont'
...   { _id: 0, prenom_joueur: 1 } // Projection to include only prenom_joueur field, excluding _id
... )
[
  { prenom_joueur: 'Alice' },
  { prenom_joueur: 'Alice' },
  { prenom_joueur: 'Dorine' }
]

4. 

club_tennis> db.joueurs.updateOne(
...   { nom_joueur: "Dupont", prenom_joueur: "Dorine" }, // Filter to find Dorine Dupont
...   { $set: { mdp: "1976" } } // Update operation to set the new password to '1976'
... )
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}

5.

club_tennis> db.joueurs.insertOne(
...   { nom_joueur: "MAGID", prenom_joueur: "Zora", login: "zora", mdp: "2021" }
... )
{
  acknowledged: true,
  insertedId: ObjectId('6572e58e883dfd1047ba1b5f')
}

6.

club_tennis> db.matchs.aggregate([
...   {
...     $lookup: {
...       from: "joueurs",
...       localField: "id_joueur1",
...       foreignField: "id_joueur",
...       as: "player1"
...     }
...   },
...   {
...     $unwind: "$player1"
...   },
...   {
...     $lookup: {
...       from: "joueurs",
...       localField: "id_joueur2",
...       foreignField: "id_joueur",
...       as: "player2"
...     }
...   },
...   {
...     $unwind: "$player2"
...   },
...   {
...     $match: {
...       $or: [
...         { "player1.nom_joueur": "Durand", "player1.prenom_joueur": "Belina" },
...         { "player2.nom_joueur": "Durand", "player2.prenom_joueur": "Belina" }
...       ],
...       $or: [
...         { "player1.nom_joueur": "Caron", "player1.prenom_joueur": "Camilia" },
...         { "player2.nom_joueur": "Caron", "player2.prenom_joueur": "Camilia" }
...       ]
...     }
...   },
...   {
...     $lookup: {
...       from: "creneaux",
...       localField: "id_creneau",
...       foreignField: "id_creneau",
...       as: "timeslot"
...     }
...   },
...   {
...     $unwind: "$timeslot"
...   },
...   {
...     $project: {
...       day: "$date",
...       timeslot: "$timeslot.plage_horaire"
...     }
...   }
... ])
[
  {
    _id: ObjectId('6572e4a0883dfd1047ba1b46'),
    day: '2020-08-01',
    timeslot: '10h-11h'
  },
  {
    _id: ObjectId('6572e4a0883dfd1047ba1b46'),
    day: '2020-08-01',
    timeslot: '10h-11h'
  },
  {
    _id: ObjectId('6572e4a0883dfd1047ba1b47'),
    day: '2020-08-02',
    timeslot: '13h-14h'
  },
  {
    _id: ObjectId('6572e4a0883dfd1047ba1b47'),
    day: '2020-08-02',
    timeslot: '13h-14h'
  },
  {
    _id: ObjectId('6572e4a0883dfd1047ba1b4a'),
    day: '2020-08-08',
    timeslot: '12h-13h'
  },
  {
    _id: ObjectId('6572e4a5883dfd1047ba1b4d'),
    day: '2020-08-01',
    timeslot: '10h-11h'
  },
  {
    _id: ObjectId('6572e4a5883dfd1047ba1b4d'),
    day: '2020-08-01',
    timeslot: '10h-11h'
  },
  {
    _id: ObjectId('6572e4a5883dfd1047ba1b4e'),
    day: '2020-08-02',
    timeslot: '13h-14h'
  },
  {
    _id: ObjectId('6572e4a5883dfd1047ba1b4e'),
    day: '2020-08-02',
    timeslot: '13h-14h'
  },
  {
    _id: ObjectId('6572e4a5883dfd1047ba1b51'),
    day: '2020-08-08',
    timeslot: '12h-13h'
  }
]

7. 

club_tennis> db.matchs.aggregate([
...     { $match: { "id_terrain": 3 } },
...     { $lookup: { from: "joueurs", localField: "id_joueur1", foreignField: "id", as: "player1" } },
...     { $unwind: "$player1" },
...     { $project: { _id: 0, nom_joueur: "$player1.nom_joueur" } },
...     { $lookup: { from: "joueurs", localField: "id_joueur2", foreignField: "id", as: "player2" } },
...     { $unwind: "$player2" },
...     { $project: { _id: 0, nom_joueur: "$player2.nom_joueur" } },
...     { $sort: { nom_joueur: 1 } }
... ])

8.

club_tennis> db.matchs.aggregate([
...   {
...     $group: {
...       _id: "$id_terrain",
...       count: { $sum: 1 }
...     }
...   },
...   {
...     $lookup: {
...       from: "terrains",
...       localField: "_id",
...       foreignField: "id_terrain",
...       as: "terrain_info"
...     }
...   },
...   {
...     $unwind: "$terrain_info"
...   },
...   {
...     $project: {
...       _id: 0,
...       terrain: "$terrain_info.nom_terrain",
...       match_count: "$count"
...     }
...   }
... ])
[
  { terrain: 'hangar terre battue', match_count: 2 },
  { terrain: 'hangar terre battue', match_count: 2 },
  { terrain: 'gymnase synthétique', match_count: 6 },
  { terrain: 'gymnase synthétique', match_count: 6 }
]

9.

club_tennis> db.matchs.aggregate([
...   {
...     $group: {
...       _id: "$id_creneau",
...       count: { $sum: 1 }
...     }
...   },
...   {
...     $lookup: {
...       from: "creneaux",
...       localField: "_id",
...       foreignField: "id_creneau",
...       as: "timeslot_info"
...     }
...   },
...   {
...     $unwind: "$timeslot_info"
...   },
...   {
...     $sort: { count: -1 }
...   },
...   {
...     $limit: 1
...   },
...   {
...     $project: {
...       _id: 0,
...       timeslot: "$timeslot_info.plage_horaire",
...       match_count: "$count"
...     }
...   }
... ])
[ { timeslot: '10h-11h', match_count: 4 } ]

10.

club_tennis> db.matchs.aggregate([
...   {
...     $facet: {
...       player1Matches: [
...         { $group: { _id: "$id_joueur1", count: { $sum: 1 } } }
...       ],
...       player2Matches: [
...         { $group: { _id: "$id_joueur2", count: { $sum: 1 } } }
...       ]
...     }
...   },
...   {
...     $project: {
...       allMatches: { $concatArrays: ["$player1Matches", "$player2Matches"] }
...     }
...   },
...   {
...     $unwind: "$allMatches"
...   },
...   {
...     $group: {
...       _id: "$allMatches._id",
...       totalMatches: { $sum: "$allMatches.count" }
...     }
...   },
...   {
...     $lookup: {
...       from: "joueurs",
...       localField: "_id",
...       foreignField: "id_joueur",
...       as: "player_info"
...     }
...   },
...   {
...     $unwind: "$player_info"
...   },
...   {
...     $sort: { totalMatches: 1 }
...   },
...   {
...     $limit: 1
...   },
...   {
...     $project: {
...       _id: 0,
...       playerName: { $concat: ["$player_info.prenom_joueur", " ", "$player_info.nom_joueur"] },
...       totalMatches: 1
...     }
...   }
... ])
[ { totalMatches: 4, playerName: 'Dorine Dupont' } ]

11.

club_tennis> db.matchs.aggregate([
...   {
...     $group: {
...       _id: "$id_terrain",
...       count: { $sum: 1 }
...     }
...   },
...   {
...     $lookup: {
...       from: "terrains",
...       localField: "_id",
...       foreignField: "id_terrain",
...       as: "terrain_info"
...     }
...   },
...   {
...     $unwind: "$terrain_info"
...   },
...   {
...     $sort: { count: -1 }
...   },
...   {
...     $limit: 1
...   },
...   {
...     $project: {
...       _id: 0,
...       terrain: "$terrain_info.nom_terrain",
...       match_count: "$count"
...     }
...   }
... ])
[ { terrain: 'gymnase synthétique', match_count: 6 } ]

## Exo 2

1. 2.

club_tennis> use cycle_formation
switched to db cycle_formation
cycle_formation> // Collection ETUDIANT

cycle_formation> db.createCollection("ETUDIANT")
{ ok: 1 }
cycle_formation> db.ETUDIANT.insertMany([
...     { NEtudiant: "01234567", Nom: "Bruno", Prenom: "Alex", Section: "Informatique" },
...     { NEtudiant: "01234568", Nom: "Lavand", Prenom: "Stive", Section: "Math" },
...     { NEtudiant: "01234569", Nom: "Lahoche", Prenom: "Aline", Section: "Informatique" }
... ])
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6572e7d6883dfd1047ba1b60'),
    '1': ObjectId('6572e7d6883dfd1047ba1b61'),
    '2': ObjectId('6572e7d6883dfd1047ba1b62')
  }
}
cycle_formation>

cycle_formation> // Collection MATIERE

cycle_formation> db.createCollection("MATIERE")
{ ok: 1 }
cycle_formation> db.MATIERE.insertMany([
...     { CodeMat: "12508", NomMat: "Base de données", CoeffMat: 1.5 },
...     { CodeMat: "12518", NomMat: "Algorithmes", CoeffMat: 2 }
... ])
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6572e7d6883dfd1047ba1b63'),
    '1': ObjectId('6572e7d6883dfd1047ba1b64')
  }
}
cycle_formation>

cycle_formation> // Collection ENSEIGNANT

cycle_formation> db.createCollection("ENSEIGNANT")
{ ok: 1 }
cycle_formation> db.ENSEIGNANT.insertMany([
...     { CodeEns: "123", NomEns: "Lois", GradeEns: "Grd1", CodeMat: "12508" },
...     { CodeEns: "124", NomEns: "Philippe", GradeEns: "Grd2", CodeMat: "12518" }
... ])
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6572e7d6883dfd1047ba1b65'),
    '1': ObjectId('6572e7d6883dfd1047ba1b66')
  }
}
cycle_formation>

cycle_formation> // Collection NOTE

cycle_formation> db.createCollection("NOTE")
{ ok: 1 }
cycle_formation> db.NOTE.insertMany([
...     { NEtudiant: "01234567", CodeMat: "12508", Date: "YYYY-MM-DD", Note_examen: 15.5 },
...     { NEtudiant: "01234567", CodeMat: "12518", Date: "YYYY-MM-DD", Note_examen: 5.5 },
...     { NEtudiant: "01234568", CodeMat: "12518", Date: "YYYY-MM-DD", Note_examen: 10.5 },
...     { NEtudiant: "01234569", CodeMat: "12518", Date: "YYYY-MM-DD", Note_examen: 8.75 }
... ])
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6572e7d6883dfd1047ba1b67'),
    '1': ObjectId('6572e7d6883dfd1047ba1b68'),
    '2': ObjectId('6572e7d6883dfd1047ba1b69'),
    '3': ObjectId('6572e7d6883dfd1047ba1b6a')
  }
}

3. 

cycle_formation> db.ETUDIANT.count()
3

4.

cycle_formation> db.NOTE.aggregate([
...   { $sort: { Note_examen: -1 } },
...   { $limit: 1 }
... ])
[
  {
    _id: ObjectId('6572e7d6883dfd1047ba1b67'),
    NEtudiant: '01234567',
    CodeMat: '12508',
    Date: 'YYYY-MM-DD',
    Note_examen: 15.5
  }
]

cycle_formation> db.NOTE.aggregate([
...   { $sort: { Note_examen: 1 } },
...   { $limit: 1 }
... ])
[
  {
    _id: ObjectId('6572e7d6883dfd1047ba1b68'),
    NEtudiant: '01234567',
    CodeMat: '12518',
    Date: 'YYYY-MM-DD',
    Note_examen: 5.5
  }
]

5. 

cycle_formation> db.NOTE.aggregate([
...   {
...     $group: {
...       _id: { NEtudiant: "$NEtudiant", CodeMat: "$CodeMat" },
...       average: { $avg: "$Note_examen" }
...     }
...   },
...   {
...     $lookup: {
...       from: "ETUDIANT",
...       localField: "_id.NEtudiant",
...       foreignField: "NEtudiant",
...       as: "student_info"
...     }
...   },
...   {
...     $lookup: {
...       from: "MATIERE",
...       localField: "_id.CodeMat",
...       foreignField: "CodeMat",
...       as: "subject_info"
...     }
...   },
...   {
...     $unwind: "$student_info"
...   },
...   {
...     $unwind: "$subject_info"
...   },
...   {
...     $project: {
...       _id: 0,
...       Student: { $concat: ["$student_info.Prenom", " ", "$student_info.Nom"] },
...       Subject: "$subject_info.NomMat",
...       Average: "$average"
...     }
...   }
... ])
[
  { Student: 'Alex Bruno', Subject: 'Algorithmes', Average: 5.5 },
  { Student: 'Alex Bruno', Subject: 'Base de données', Average: 15.5 },
  { Student: 'Aline Lahoche', Subject: 'Algorithmes', Average: 8.75 },
  { Student: 'Stive Lavand', Subject: 'Algorithmes', Average: 10.5 }
]

6.

cycle_formation> db.NOTE.aggregate([
...   {
...     $group: {
...       _id: "$NEtudiant",
...       average: { $avg: "$Note_examen" }
...     }
...   },
...   {
...     $lookup: {
...       from: "ETUDIANT",
...       localField: "_id",
...       foreignField: "NEtudiant",
...       as: "student_info"
...     }
...   },
...   {
...     $unwind: "$student_info"
...   },
...   {
...     $project: {
...       _id: 0,
...       Student: { $concat: ["$student_info.Prenom", " ", "$student_info.Nom"] },
...       Average: "$average"
...     }
...   }
... ])
[
  { Student: 'Alex Bruno', Average: 10.5 },
  { Student: 'Aline Lahoche', Average: 8.75 },
  { Student: 'Stive Lavand', Average: 10.5 }
]

7.

cycle_formation> db.NOTE.aggregate([
...   {
...     $group: {
...       _id: "$NEtudiant",
...       average: { $avg: "$Note_examen" }
...     }
...   },
...   {
...     $match: {
...       average: { $gte: 7, $lte: 12 }
...     }
...   },
...   {
...     $project: {
...       _id: 0,
...       StudentID: "$_id"
...     }
...   }
... ])
[
  { StudentID: '01234568' },
  { StudentID: '01234567' },
  { StudentID: '01234569' }
]

8.

cycle_formation> db.ETUDIANT.find({ Nom: { $regex: /^L/i } })
[
  {
    _id: ObjectId('6572e7d6883dfd1047ba1b61'),
    NEtudiant: '01234568',
    Nom: 'Lavand',
    Prenom: 'Stive',
    Section: 'Math'
  },
  {
    _id: ObjectId('6572e7d6883dfd1047ba1b62'),
    NEtudiant: '01234569',
    Nom: 'Lahoche',
    Prenom: 'Aline',
    Section: 'Informatique'
  }
]

9.

cycle_formation> db.NOTE.aggregate([
...   {
...     $match: {
...       CodeMat: "12518" // Filtre pour la matière spécifique
...     }
...   },
...   {
...     $group: {
...       _id: "$NEtudiant" // Regroupe par numéro d'étudiant
...     }
...   },
...   {
...     $group: {
...       _id: null,
...       count: { $sum: 1 } // Compte le nombre d'étudiants uniques
...     }
...   }
... ])
[ { _id: null, count: 3 } ]

10.

cycle_formation> db.MATIERE.aggregate([
...   {
...     $group: {
...       _id: null,
...       totalCoefficients: { $sum: "$CoeffMat" } // Somme des coefficients des matières
...     }
...   }
... ])
[ { _id: null, totalCoefficients: 3.5 } ]

11.

cycle_formation> db.ETUDIANT.find({ NEtudiant: { $in: studentIds } }, { Nom: 1, Prenom: 1 })
[
  {
    _id: ObjectId('6572e7d6883dfd1047ba1b60'),
    Nom: 'Bruno',
    Prenom: 'Alex'
  },
  {
    _id: ObjectId('6572e7d6883dfd1047ba1b61'),
    Nom: 'Lavand',
    Prenom: 'Stive'
  }
]

12.

cycle_formation> let subjectCodes = db.NOTE.find({ NEtudiant: '01234568' }, { CodeMat: 1 }).toArray().map(doc => doc.CodeMat);

cycle_formation>

cycle_formation> // Recherche des noms et coefficients des matières correspondant aux codes obtenus précédemment

cycle_formation> db.MATIERE.find({ CodeMat: { $in: subjectCodes } }, { NomMat: 1, CoeffMat: 1 })
[
  {
    _id: ObjectId('6572e7d6883dfd1047ba1b64'),
    NomMat: 'Algorithmes',
    CoeffMat: 2
  }
]

13.

cycle_formation> db.ETUDIANT.find({}, { NEtudiant: 1, Nom: 1, DateNaissance: 1 }).sort({ Nom: 1 })
[
  {
    _id: ObjectId('6572e7d6883dfd1047ba1b60'),
    NEtudiant: '01234567',
    Nom: 'Bruno'
  },
  {
    _id: ObjectId('6572e7d6883dfd1047ba1b62'),
    NEtudiant: '01234569',
    Nom: 'Lahoche'
  },
  {
    _id: ObjectId('6572e7d6883dfd1047ba1b61'),
    NEtudiant: '01234568',
    Nom: 'Lavand'
  }
]

14.

cycle_formation> let matiereBD = db.MATIERE.findOne({ NomMat: 'Base de données' });

cycle_formation> let codeMatiereBD = matiereBD ? matiereBD.CodeMat : null;

cycle_formation>

cycle_formation> // Recherche des enseignants associés à la matière 'BD'

cycle_formation> db.ENSEIGNANT.find({ CodeMat: codeMatiereBD }, { NomEns: 1, GradeEns: 1 })
[
  {
    _id: ObjectId('6572e7d6883dfd1047ba1b65'),
    NomEns: 'Lois',
    GradeEns: 'Grd1'
  }
]

15.

cycle_formation> let matieresGrd2 = db.ENSEIGNANT.find({ GradeEns: 'Grd2' }, { CodeMat: 1 }).toArray().map(doc => doc.CodeMat);

cycle_formation>

cycle_formation> // Recherche des noms et des coefficients des matières correspondantes aux codes obtenus précédemment

cycle_formation> db.MATIERE.find({ CodeMat: { $in: matieresGrd2 } }, { NomMat: 1, CoeffMat: 1 })
[
  {
    _id: ObjectId('6572e7d6883dfd1047ba1b64'),
    NomMat: 'Algorithmes',
    CoeffMat: 2
  }
]

16.

cycle_formation> // Récupération du code de la matière 'Informatique'

cycle_formation> let matiereInformatique = db.MATIERE.findOne({ NomMat: 'Informatique' });

cycle_formation> let codeMatiereInformatique = matiereInformatique ? matiereInformatique.CodeMat : null;

cycle_formation>

cycle_formation> // Comptage du nombre d'enseignants associés à la matière 'Informatique'

cycle_formation> db.ENSEIGNANT.find({ CodeMat: codeMatiereInformatique }).count()
0
