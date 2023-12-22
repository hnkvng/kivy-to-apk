from tinydb import Query, TinyDB

DATA = "../db/database.json"
#init database
class initDataBase():
    def connect(self):
        return TinyDB(DATA)
    def query(self):
        return Query() 
        