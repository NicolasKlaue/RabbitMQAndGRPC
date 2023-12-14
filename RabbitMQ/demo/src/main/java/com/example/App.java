package com.example;

import org.springframework.amqp.rabbit.annotation.RabbitListener;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class App 

{
     
         public static void main(String[] args) {
             SpringApplication.run(App.class, args);
         }
     
         @RabbitListener(queues = "MyQueue")
         public void receiveMessage(String message) {
             System.out.println("Received message: " + message);
         }
}
