// Importar la biblioteca 'amqplib' que proporciona la implementación de cliente AMQP para Node.js
const amqp = require('amqplib');

// Definir el nombre de la cola que se va a utilizar
const QUEUE_NAME = 'MyQueue';

// Definir la función 'start' que se encargará de establecer la conexión y consumir mensajes
async function start() {
    // Establecer una conexión con el servidor RabbitMQ 
    const connection = await amqp.connect('amqp://localhost');
    
    // Crear un canal de comunicación dentro de la conexión
    const channel = await connection.createChannel();

    // Declarar la cola que se utilizará
    await channel.assertQueue(QUEUE_NAME, { durable: false });

    // Imprimir un mensaje indicando que el script está esperando mensajes en la cola
    console.log('Waiting for messages. (Press CTRL+C to exit)');

    // Configurar un consumidor para la cola 
    // El consumidor se activará cuando llegue un mensaje a la cola.
    channel.consume(QUEUE_NAME, (msg) => {
        // Convertir el contenido del mensaje a una cadena de texto.
        const message = msg.content.toString();
        
        // Imprimir en la consola el mensaje recibido.
        console.log('Received:', message);
        
        // Crear un mensaje de recibo.
        const acknowledgmentMessage = 'Node.js App Acknowledgment';
        
        // Enviar el mensaje  de recibo a la cola especificada en la propiedad 'replyTo' del mensaje original.
        channel.sendToQueue(msg.properties.replyTo, Buffer.from(acknowledgmentMessage), { correlationId: msg.properties.correlationId });
    }, { noAck: true });
}

// Llamar a la función 'start' para iniciar el proceso de consumo de mensajes.
// Capturar cualquier error y imprimirlo en la consola.
start().catch(console.error);
