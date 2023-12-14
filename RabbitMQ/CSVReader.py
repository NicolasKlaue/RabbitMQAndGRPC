import csv
import pika
import json

#region root directory
import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
#endregion

file_path = 'cp-national-datafile-csv.csv'
with open(file_path, newline='') as csvfile:
    csv_content = csvfile.read()
    

#region pika connection
try:
     connection = pika.BlockingConnection(pika.ConnectionParameters('localhost','5672'))
     channel = connection.channel()

     queue_name = 'MyQueue'
     channel.queue_declare(queue=queue_name)
     channel.confirm_delivery()
     message = {'filename':file_path,
               'content':csv_content}
     print(f"Sent CSV file {file_path}")
except Exception as e:
    print("Connection could not be established ERROR:\t" + str(e))

try:
    channel.basic_publish(exchange='', routing_key=queue_name, body=json.dumps(message),mandatory=True)
    print('Message publish was confirmed')
    connection.close()
except Exception as e:
    print('Message could not be confirmed ERROR:\t' + str(e))
#endregion