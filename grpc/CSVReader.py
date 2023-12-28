import csv
import grpc
from generated import java_pb2, java_pb2_grpc  # Adjust the import based on your proto file location
from generated import node_pb2, node_pb2_grpc  # Adjust the import based on your proto file location


# Store the CSV path
csv_file = 'cp-national-datafile-csv.csv'

# gRPC server addresses
java_server_address = 'localhost:9090'
node_server_address = 'localhost:8080'

def send_to_java(data):
    with grpc.insecure_channel(java_server_address) as channel:
        stub = java_pb2_grpc.JavaStub(channel)
        request = java_pb2.JavaRequest(data=data)
        response = stub.sendData(request)
    print("Java server response:", response.message)
 

def send_to_node(data):
    return None

# Read CSV file and send data to Java and Node.js servers
with open(csv_file, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        data = ', '.join(row)
        print(data)
        send_to_java(data)
        send_to_node(data)






