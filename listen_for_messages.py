"""

Listens for messages on the queue.
This process runs continously. 

Approach
---------
Simple - one producer / one consumer.


Since this process runs continuously, 
if we want to emit more messages, 
we'll need to open a new terminal window.


Terminal Reminders
------------------

- Use Control c to close a terminal and end a process.

- Use the up arrow to get the last command executed.

"""

import pika
import sys
import os


def listen_for_messages():
    """ Continuously listen for messages on a named queue."""

    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    channel = connection.channel()

    def callback(ch, method, properties, body):
        """ Define behavior on getting a message."""
        print(" [x] Received %r" % body.decode())

    channel.queue_declare(queue="hello")
    channel.basic_consume(queue="hello", on_message_callback=callback, auto_ack=True)

    print(" [*] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()


if __name__ == "__main__":
    try:
        listen_for_messages()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
