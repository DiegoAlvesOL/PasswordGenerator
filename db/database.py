import sqlite3
from pathlib import Path
from datetime import datetime

# Caminho do banco de dados (na mesma pasta do projeto)
# Database path (in the same project folder)
db_path = Path(__file__).parent / "lockit.db"

# Criação da tabela 'passwords' caso não exista
# Creates the 'passwords' table if it doesn't exist
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

# Função que insere uma nova senha no banco de dados
# Inserts a new password record into the database
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
