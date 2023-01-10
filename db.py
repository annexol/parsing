import sqlite3
import typing


class DataBase:
    def __init__(self, data: typing.List):
        self.data = data
        self.connection = sqlite3.connect('apps2.db')
        self.cursor = self.connection.cursor()
        self.create_table()
        self.save_data()
        self.connection.close()

    def create_table(self):
        self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS microsoft_apps(id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(255),
             release_year INTEGER,
             company_name VARCHAR(255),
             email VARCHAR(255))'''

        )

        self.connection.commit()

    def save_data(self):
        for i in self.data:
            self.cursor.execute(f'''INSERT INTO windows_apps(name, release_year, company_name, email) VALUES 
                ('{i["name"]}',
                 '{i["release_year"]}', 
                 '{i["company_name"]}', 
                 '{i["email"]}')''')
        self.connection.commit()
