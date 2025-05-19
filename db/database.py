import sqlite3
from pathlib import Path
from datetime import datetime
from time import strftime

# Cria o caminho do banco (no mesmo local do projeto)
db_path = Path(__file__).parent / "lockit.db"

# Função para criar a tabela
def create_table():
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS passwords(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item TEXT NOT NULL,
            user TEXT NOT NULL,
            site TEXT NOT NULL,
            password TEXT NOT NULL,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL);""")
    connection.commit()
    connection.close()

def insert_password(item, user, site, password):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    created_at = now
    updated_at = now
    cursor.execute("INSERT INTO passwords (item, user, site, password, created_at, updated_at) VALUES(?,?,?,?,?,?)",
                   (item, user, site, password, created_at, updated_at))
    connection.commit()
    connection.close()
