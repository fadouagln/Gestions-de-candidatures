from flask import Flask
import sqlite3

def __init__(self):
    con=sqlite3.connect('database.db')
    cur=con.cursor
    cur.execute("CREATE TABLE utilisateurs(id INTEGER AUTOINCREMENT,"
    "nom TEXT NOT NULL,"
    "email TEXT UNIQUE NOT NULL"
    ",mot de passe TEXT NOT NULL "
    ")")


    cur.execute('CREATE TABLE candidatures(id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'utilisateur_id INTEGER NOT NULL,'
    'entreprise NOT NULL,'
    'poste TEXT NOT NULL,'
    'date_envoie TEXT NOT NULL,'
    'statut TEXT NOT NULL,'
    'FOREIGH KEY (utilisateur_id) REFERENCES utilisateurs(id)'
    ')')

    cur.execute('CREATE TABLE documents(id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'candidature_id INTEGER NOT NULL,type TEXT NOT NULL,'
    'chemin_fichier TEXT NOT NULL,'
    'FOREIGN KEY (candidature_id) REFERENCES candidatures(id)'
    ')')

    


