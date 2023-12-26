// Java Server 

public class JavaServer {
    public static void main(String[] args) throws Exception {
        // GRPC server, port: 9090 configuration
        Server server = ServerBuilder.forPort(9090)
                .addService(new JavaService()) // add service
                .build(); // build service

        server.start(); 
        server.awaitTermination(); // wait until server finishes its execution
    }

    static class JavaService extends JavaGrpc.JavaImplBase {
        @Override 
        public void sendData(JavaRequest request, StreamObserver<JavaResponse> responseObserver) {
            System.out.println("Received data from Python: " + request.getData()); 
            JavaResponse response = JavaResponse.newBuilder() // creates the response for the Python client
                    .setMessage("Java server received the data.")
                    .build(); 

            responseObserver.onNext(response); // sends the response created before
            responseObserver.onCompleted(); // complete operation advice
        }
    }
}