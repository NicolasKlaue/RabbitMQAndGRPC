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


# Java Server 

public class JavaServer {
    public static void main(String[] args) throws Exception {
        # GRPC server, port: 9090 configuration
        Server server = ServerBuilder.forPort(9090)
                .addService(new JavaService()) # add service
                .build(); # build service

        server.start(); 
        server.awaitTermination(); # wait until server finishes its execution
    }

    static class JavaService extends JavaGrpc.JavaImplBase {
        @Override 
        public void sendData(JavaRequest request, StreamObserver<JavaResponse> responseObserver) {
            System.out.println("Received data from Python: " + request.getData()); 
            JavaResponse response = JavaResponse.newBuilder() # creates the response for the Python client
                    .setMessage("Java server received the data.")
                    .build(); 

            responseObserver.onNext(response); # sends the response created before
            responseObserver.onCompleted(); # complete operation advice
        }
    }
}



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