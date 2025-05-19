class passwordEntry:
    def __init__(self, item_name, user_entry, website_address, password):
        self.item_name = item_name
        self.user_entry = user_entry
        self.website_address = website_address
        self.password = password

    def __str__(self):
        return f"{self.item_name} | {self.user_entry} |{self.website_address} |{self.password}"

entry = passwordEntry
print(entry)