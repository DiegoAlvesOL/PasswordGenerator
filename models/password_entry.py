from db.database import insert_password

# Classe responsável por representar e salvar uma entrada de senha
# Class responsible for representing and saving a password entry
class PasswordEntry:
    def __init__(self, item,user,site,password):
        self.item = item
        self.user = user
        self.site = site
        self.password = password

    # Salva os dados no banco de dados chamando a função insert_password
    # Saves the data to the database using the insert_password function
    def save_to_db(self):
        insert_password(self.item,
                        self.user,
                        self.site,
                        self.password)

    def __str__(self):
        return f"{self.item} | {self.user} |{self.site} |{self.password}"

# entry = PasswordEntry
# print(entry)