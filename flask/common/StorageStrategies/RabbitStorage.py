import os
import pika, uuid, json
from ..Students import *
from .StorageBase import StorageBase

class RabbitStorage(StorageBase):
    
    class RpcClient(object):
        def __init__(self):
            self.connection = pika.BlockingConnection(
                pika.ConnectionParameters(host=os.getenv('RABBITIP','127.0.0.1')))
            
            self.channel = self.connection.channel()
            result = self.channel.queue_declare(queue='', exclusive=True)
            self.callback_queue = result.method.queue
            
            self.channel.basic_consume(
                queue = self.callback_queue,
                on_message_callback=self.on_response,
                auto_ack=True)
            
            self.response = None
            self.corr_id = None
            
        def disconnect(self):
            self.connection.close()
        
        def on_response(self, ch, method, props, body):
            if self.corr_id == props.correlation_id:
                self.response = body
                
        def call(self, data):
            self.response = None
            self.corr_id = str(uuid.uuid4())
            self.channel.basic_publish(
                exchange='',
                routing_key='rpc_queue',
                properties=pika.BasicProperties(
                    reply_to=self.callback_queue,
                    correlation_id=self.corr_id,
                ),
                body=json.dumps(data)
            )
            self.connection.process_data_events(time_limit=None)
            try:
                return json.loads(self.response)
            except:
                return None
                
    def __init__(self):
        self.rpc = self.RpcClient()
                
    def Load(self):
        pass
    def Store(self):
        self.rpc.disconnect()
            
    def call(self, command, id=0, data=''):
        return self.rpc.call({'command': command, 'id':id, 'data':data})
        
    def GetStudent(self, id):
        student = Student()
        if id > 0:
            res = self.call('GetStudent', id)
            studentType = res.get('studenttype')
            
            if studentType == 1:
                student = Student()
            elif studentType == 2:
                student = HeadStudent()
            elif studentType == 3:
                student = UnionOrganizer()
                
            student.setData(res) 
                 
        return student
        
        
    def Add(self, student):
        self.call('Add', student.id, student.getData())
            
    def Delete(self, id):
        self.call('Delete', id)
            
    def GetStudents(self):
        res = self.call('GetStudents')
        
        for r in res:
            student = None
            studentType = r.get('studenttype')

            if studentType == 1:
                student = Student()
            elif studentType == 2:
                student = HeadStudent()
            elif studentType == 3:
                student = UnionOrganizer() 
                
            student.setData(r)
            yield student

                
  
  
  
  
  