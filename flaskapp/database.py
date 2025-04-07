import sqlite3

class Database:
    def __init__(self):
        """Initialisation de la base de données"""
        self.con = sqlite3.connect('database.db')
        self.cur = self.con.cursor()
        self.create_tables()

    def create_tables(self):
        """Création des tables si elles n'existent pas"""
        self.cur.execute('''CREATE TABLE IF NOT EXISTS utilisateurs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            mot_de_passe TEXT NOT NULL
        )''')
        self.con.commit()  # ✅ Ajout du commit ici

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

    def add_user(self, nom, email, mot_de_passe):
        """Ajoute un utilisateur dans la base"""
        try:
            self.cur.execute("INSERT INTO utilisateurs (nom, email, mot_de_passe) VALUES (?, ?, ?)", 
                             (nom, email, mot_de_passe))
            self.con.commit()
        except sqlite3.IntegrityError:
            print("❌ Erreur : Cet email est déjà utilisé.")

    def get_users(self):
        """Récupère tous les utilisateurs"""
        self.cur.execute("SELECT * FROM utilisateurs")
        return self.cur.fetchall()

    def close(self):
        """Ferme la connexion à la base de données"""
        self.con.close()


db = Database()


db.add_user("Fadoua", "fadoua@example.com", "motdepasse123")
print(db.get_users())  # Vérification

db.close()
