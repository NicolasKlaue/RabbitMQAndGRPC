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