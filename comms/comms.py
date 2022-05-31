import paho.mqtt.client as mqtt
import numpy as np 

client = mqtt.Client()
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
	print("Connection returned result: " +str(rc))

# The callback of the client when it disconnects.
def on_disconnect(client, userdata, rc):
	if rc != 0:
		print("Unexpected Disconnect")
	else:
		print("Expected Disconnect")

# The default message callback.
def on_message(client, userdata, message):
	print('Received message: "' + str(message.payload) + '" on topic "' + message.topic + '" with QoS ' + str(message.qos))

def publish(msg):
	print(msg)
	client.publish("film/test", "hi", qos=1)

def main(c_conn):

	client.on_connect = on_connect 
	client.on_disconnect = on_disconnect 
	client.on_message = on_message
	
	client.connect_async("test.mosquitto.org")
	
	client.loop_start()

	while True: 
		pass
		#if (c_conn):
		#	publish(c_conn)

	client.loop_stop()
	client.disconnect()