import pickle

from .StorageBase import StorageBase
from ..Students.Student import Student

class PickleStorage(StorageBase):

    def __init__(self, name):
        self.storagePath += ('/' + name + '/')
        self.name = name
        try:
            self.Load()
            
        except:
            self.students = {}
            self.maxid = 0
            
    def SetGroup(self, group):  
        self.group = group

    def Load(self):
        self.TryMakeStorageDirectory()
        with open(self.storagePath + self.name + '.db', 'rb') as f:
            (self.maxid, self.students) = pickle.load(f)

    def Store(self):
        with open(self.storagePath + self.name + '.db', 'wb') as f:
            pickle.dump((self.maxid, self.students), f)

    def GetStudent(self, id):
        if id <= 0:
            return Student()
        else:  
            return self.students[id]
        
    def Add(self, student):
        if student.id <= 0:
            self.maxid += 1
            student.id = self.maxid
            self.students[student.id] = student
        else:
            self.students[student.id] = student
            self.Store()

    def Delete(self, id):
        del self.students[id]

    def GetStudents(self):
        for (id, student) in self.students.items():
            yield (student)
