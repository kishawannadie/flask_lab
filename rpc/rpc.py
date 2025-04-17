import os, json
import pika

from common.IOStrategies import *
from common.StorageStrategies import *
from common.Students import *
from common.utils import *
from common.group import *
from common.handler import *


class RabbitServer(Handler):
    
    def on_request(self, ch, method, props, body):
        request = json.loads(body)
        result = self.handle(request.get('command'),request)
        if result != None:
            response = json.dumps(result)
        else:
            response = ""

        ch.basic_publish(exchange='',
                         routing_key=props.reply_to,
                         properties=pika.BasicProperties(correlation_id=props.correlation_id),
                         body=response)
        ch.basic_ack(delivery_tag=method.delivery_tag)
    def run(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=os.getenv('RABBITIP','127.0.0.1')))
        channel = connection.channel()
        channel.queue_declare(queue='rpc_queue')
        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(queue='rpc_queue', on_message_callback=self.on_request)
        channel.start_consuming()
        
def main():
    storage = DBStorage("rpc")
    
    group = Group(storage, getDictIO())
    
    server = RabbitServer()
    
    @server.set_handler("GetStudent")
    def GetStudent(data):
        return group.ShowForm(data.get('id'))
            
    @server.set_handler("GetStudents")
    def GetStudents(data):
        students = []
        for student in group.storage.GetStudents():
            students.append(student.getData())
        return students
    
    @server.set_handler("Delete")
    def Delete(data):
        return group.storage.Delete(data.get('id'))
    
    @server.set_handler("Add")
    def Add(data):
        group.io.setSource(data.get('data'))
        group.Add()
    
    server.run()
    
main()