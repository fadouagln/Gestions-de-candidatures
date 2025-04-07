import sqlite3

class Database:
    def __init__(self):
        
        self.con = sqlite3.connect('database.db')
        self.cur = self.con.cursor()
        self.create_tables()

    def create_tables(self):
       
        self.cur.execute('''CREATE TABLE IF NOT EXISTS utilisateurs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            mot_de_passe TEXT NOT NULL
        )''')
        self.con.commit() 

        self.cur.execute('''CREATE TABLE IF NOT EXISTS candidatures (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            utilisateur_id INTEGER NOT NULL,
            entreprise TEXT NOT NULL,
            poste TEXT NOT NULL,
            date_envoi DATE NOT NULL,
            statut TEXT NOT NULL,
            date_entretien DATE,
            notes TEXT,
            FOREIGN KEY(utilisateur_id) REFERENCES utilisateurs(id) ON DELETE CASCADE
        )''')
        self.con.commit()

        self.cur.execute('''CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            candidature_id INTEGER NOT NULL,
            type TEXT NOT NULL,
            chemin_fichier TEXT NOT NULL,
            FOREIGN KEY (candidature_id) REFERENCES candidatures(id) ON DELETE CASCADE
        )''')
        self.con.commit()

  
  

    def close(self):
        """Ferme la connexion à la base de données"""
        self.con.close()


db = Database()




db.close()
