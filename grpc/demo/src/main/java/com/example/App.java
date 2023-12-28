package com.example;

import io.grpc.Server;
import io.grpc.ServerBuilder;
import io.grpc.stub.StreamObserver;
import communication.Communication.JsonDataRequest;
import communication.Communication.JsonDataResponse;

public class App extends CommunicationServiceGrpc.CommunicationServiceImplBase {
     @Override
     public void sendJsonData(JsonDataRequest request, StreamObserver<JsonDataResponse> responseObserver) {
         // Process the received JSON data
     
         System.out.println("Received JSON data: " + request.getJsonData());
     
         // Send a response
         JsonDataResponse response = JsonDataResponse.newBuilder()
                 .setStatus("Data received successfully")
                 .build();
         responseObserver.onNext(response);
         responseObserver.onCompleted();
     }
     

    public static void main(String[] args) throws Exception {
        Server server = ServerBuilder.forPort(9090)
                .addService(new CommunicationServer())
                .build();

        server.start();
        System.out.println("Server started on port 9090");
        server.awaitTermination();
    }
}