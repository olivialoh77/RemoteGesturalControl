import paho.mqtt.client as mqtt

import os
#import playsound
from gtts import gTTS
import pygame

import RPi.GPIO as GPIO
from time import sleep

from mecanumdrive import *

# 0. define callbacks - functions that run when events happen.
# The callback for when the client receives a CONNACK response from the server.

def on_connect(client, userdata, flags, rc):
	print("Connection returned result: "+str(rc))

	# Subscribing in on_connect() means that if we lose the connection and
	# reconnect then subscriptions will be renewed.
	client.subscribe("film/test", qos=1)

# The callback of the client when it disconnects.
def on_disconnect(client, userdata, rc):
	if rc != 0:
		print('Unexpected Disconnect')
	else:
		print('Expected Disconnect')

# The default message callback.
# (you can create separate callbacks per subscribed topic)
def on_message(client, userdata, message):
	txt = str(message.payload).replace("b'","")
	print('Received message: "' + txt + '"on topic "' + message.topic + '" with QoS ' + str(message.qos))
	tts = gTTS(text=txt, lang='en', slow=False)
	tts.save("playback.mp3")
	pygame.mixer.init()
	pygame.mixer.music.load("playback.mp3")
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy() == True:
		continue
    	#playsound.playsound("playback.mp3")
	#os.remove("playback.mp3")
	
	if txt == "Pan right'":
		#print("k")
		right()
	elif txt == "Pan left'":
		#print("j")
		left()
	elif txt == "Tilt Up'":
		#print("i")
		forward()
	elif txt == "Tilt Down'":
		#print("h")
		backward()

# 1. create a client instance.
client = mqtt.Client()
# add additional client options (security, certifications, etc.)
# many default options should be good to start off.
# add callbacks to client.

client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message

# 2. connect to a broker using one of the connect*() functions.5

client.connect_async('test.mosquitto.org')
# client.connect("mqtt.eclipse.org")

# 3. call one of the loop*() functions to maintain network traffic flow with the broker.
client.loop_start()
# client.loop_forever()

while True:
	pass
# use subscribe() to subscribe to a topic and receive messages.

# use publish() to publish messages to the broker.

# use disconnect() to disconnect from the broker.
client.loop_stop()
client.disconnect()
GPIO.cleanup()

