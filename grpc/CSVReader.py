import csv
import io.grpc.Server;
import io.grpc.ServerBuilder;
import io.grpc.stub.StreamObserver;

#region root directory
import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
#endregion


with open('cp-national-datafile-csv.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))






# NodeJS Server
# libraries
const grpc = require('grpc');
const protoLoader = require('@grpc/proto-loader');

# proto definition
const packageDefinition = protoLoader.loadSync('proto/node.proto');
const nodeProto = grpc.loadPackageDefinition(packageDefinition).node;

# new GRPC server
const server = new grpc.Server();

server.addService(nodeProto.Node.service, {
    # manage data reception
    sendData: (call, callback) => {
        # data process 
        console.log('Received data from Python:', call.request.data);

        # confirmation message
        callback(null, { message: 'Node.js server received the data.' });
    },
});


# specific port and direction
server.bind('127.0.0.1:8080', grpc.ServerCredentials.createInsecure());
console.log('Node.js gRPC server running at http://127.0.0.1:8080');
server.start();