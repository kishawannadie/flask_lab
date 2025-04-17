import os
import pymongo
from bson.objectid import ObjectId
from .DBStorage import *

from ..Students import *

class MongoStorage(DBStorage):
    def __init__(self):
        self.Load()
    
    def Load(self):
        self.client = pymongo.MongoClient(os.getenv('DBMONGOCONNECT', 'mongodb://mongo:Lone5864@mongo:27017/'))
        self.db = self.client["groups"]
        self.dbc = self.db["groups"]
        
    def Store(self):
        self.client.close() 
    
    def preProcess(self, r):
        r['id'] = str(r['_id'])
        del r['_id']
        return r
    
    def Add(self, student):
        if not str(student.id) or str(student.id) == '0':
            self.dbc.insert_one(student.getData())
        else:
            self.dbc.update_one({"_id": ObjectId(student.id)}, {"$set": student.getData()})
    
    def Delete(self, id):
        self.dbc.delete_one({"_id": ObjectId(id)})
        
    def GetStudents(self):
        
        for r in self.dbc.find():
            student = None
            studentType = r['studenttype']

            if studentType == 1:
                student = Student()
            elif studentType == 2:
                student = HeadStudent()
            elif studentType == 3:
                student = UnionOrganizer()
            
            student.setData(self.preProcess(r))
            yield student
            
    def GetStudent(self, id):
        student = Student()
        if id != '0':
            fetchedData = self.dbc.find_one({"_id": ObjectId(id)})
            if fetchedData:
                studentType = fetchedData['studenttype']
                if studentType == 1:
                    student = Student()
                elif studentType == 2:
                    student = HeadStudent()
                elif studentType == 3:
                    student = UnionOrganizer()
                student.setData(self.preProcess(self.dbc.find_one({"_id": ObjectId(id)})))
            
        return student