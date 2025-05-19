from db.database import insert_password


class passwordEntry:
    def __init__(self, item,user,site,password):
        self.item = item
        self.user = user
        self.site = site
        self.password = password


    def save_to_db(self):
        insert_password(self.item,
                        self.user,
                        self.site,
                        self.password)

    def __str__(self):
        return f"{self.item} | {self.user} |{self.site} |{self.password}"

entry = passwordEntry
print(entry)