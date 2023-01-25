"""
    This program sends a message to a queue on the RabbitMQ server.

    Author: Denise Case
    Editied by: Zak Davlin
    Date: January 25, 2023

"""

# add imports at the beginning of the file
import pika

# create a blocking connection to the RabbitMQ server
conn = pika.BlockingConnection(pika.ConnectionParameters("LOCALHOST"))
# use the connection to create a communication channel
ch = conn.channel()
# use the channel to declare a queue
ch.queue_declare(queue="hello")
#Create Body Variable
a="Put Message here"
# use the channel to publish a message to the queue
ch.basic_publish(exchange="", routing_key="hello", body=a)
# print a message to the console for the user
print(f" [x] Sent '{a}'")
# close the connection to the server
conn.close()
