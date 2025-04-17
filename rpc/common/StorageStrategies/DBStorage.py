import sqlite3

from .StorageBase import StorageBase
from ..Students.Student import Student
from ..Students.HeadStudent import HeadStudent
from ..Students.UnionOrganizer import UnionOrganizer


class DBStorage(StorageBase):
    def __init__(self, name="", placeholder='?'):
        self.storagePath += ('/' + name + '/')
        self.name = name
        self.placeholder = placeholder
        self.Load()
       

    def getInitFields(self):
        return "id integer primary key autoincrement"

    def initTable(self):
        fields = self.getInitFields()
        fields += ", name TEXT"
        fields += ", age INTEGER"
        fields += ", groupnumber TEXT"
        fields += ", faculty TEXT"
        fields += ", studenttype INTEGER"
        fields += ", phone TEXT"
        
        fields += ", salary REAL"
        self.dbc.execute(
            f"CREATE TABLE IF NOT EXISTS groups ({fields})"
        )
        self.db.commit()
        
    def Load(self):
        self.TryMakeStorageDirectory()
        self.db = sqlite3.connect(self.storagePath + self.name+'.sqlite', detect_types=sqlite3.PARSE_DECLTYPES)
        self.db.row_factory = sqlite3.Row
        self.dbc = self.db.cursor()
        self.initTable() 

    def Store(self):    
        self.dbc.close()
        self.db.close()

    def GetStudent(self, id):
        student = Student()
        if int(id) > 0:
            self.dbc.execute(f"select * from groups where id={self.placeholder}", (int(id),))

            fetchedData = self.dbc.fetchone()
            
            studentType = fetchedData['studenttype']

            if studentType == 1:
                student = Student()
            elif studentType == 2:
                student = HeadStudent()
            elif studentType == 3:
                student = UnionOrganizer()

            student.setData(fetchedData)
            
        return student

    def Add(self, student):
        names = ""
        values = ""
        params = []
        update = ""
        
        for field, value in student.getData().items():
            if field == "id":
                continue
            if names:
                names += f", {field}"
                values += f", {self.placeholder}"
                update += f", {field} = {self.placeholder}"
            else:
                names = field
                values = self.placeholder
                update += f"{field} = {self.placeholder}"
            params.append(value)
            
            
        if not student.id or int(student.id) == 0:
            self.dbc.execute(f"insert into groups({names}) values({values})", params)
        else:
            params.append(int(student.id))
            self.dbc.execute(f"update groups set {update} where id={self.placeholder}", params)
            
        self.db.commit()
    
    def Delete(self, id):
        self.dbc.execute(f"delete from groups where id={self.placeholder}", (int(id),))
        self.db.commit()

    def GetStudents(self):
        self.dbc.execute("select * from groups order by id desc")
        
        for r in self.dbc:
            student = None
            studentType = r['studenttype']

            if studentType == 1:
                student = Student()
            elif studentType == 2:
                student = HeadStudent()
            elif studentType == 3:
                student = UnionOrganizer()
            
            student.setData(r)
            yield student
