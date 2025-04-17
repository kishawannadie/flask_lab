import os
import psycopg2
import psycopg2.extras
from .DBStorage import *

class PostgreStorage(DBStorage):
    def __init__(self, name=""):
        super().__init__(name=name, placeholder='%s')
    
    def Load(self):
        self.db = psycopg2.connect(user=os.getenv('DBGPUSER', 'postgres'), 
                                   password=os.getenv('DBPGPASS', 'Lone5864'), 
                                   host=os.getenv('DBPGIP', '127.0.0.1'),
                                   database=os.getenv('DBPGDB', 'groups'))
        
        self.dbc = self.db.cursor(cursor_factory=psycopg2.extras.DictCursor)
        self.initTable()

    def getInitFields(self):
	    return "id serial primary key"
        
    