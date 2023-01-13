"""

Creates and sends a message to the queue each execution.
This process runs and finishes. 

Approach
---------
Simple - one producer / one consumer.


"""

import pika

conn = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
ch = conn.channel()

ch.queue_declare(queue="hello")
ch.basic_publish(exchange="", routing_key="hello", body="Hello World!")

print(" [x] Sent 'Hello World!'")
conn.close()

