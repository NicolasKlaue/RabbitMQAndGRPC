package com.example;

import org.springframework.amqp.rabbit.annotation.RabbitListener;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;


@SpringBootApplication
public class App

{

     

     public static void main(String[] args) {
          SpringApplication.run(App.class, args);
     }

     @RabbitListener(queues = "MyQueue")
     public void receiveMessage(String message) {
          try {
               ObjectMapper objectMapper = new ObjectMapper();
               JsonNode jsonNode = objectMapper.readTree(message);
               
                       // Extract filename and content fields
        String filename = jsonNode.get("filename").asText();
        String content = jsonNode.get("content").asText();

        // Print filename and content separately
        System.out.println("Received message:");
        System.out.println("Filename: " + filename);
        System.out.println("Content:\n" + content);
               // Process the message here
           } catch (Exception e) {
               System.err.println("Error processing message: " + e.getMessage());
           }

          }
}
