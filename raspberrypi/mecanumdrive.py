import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

LFpinForward = 27
LFpinReverse = 22
GPIO.setup(LFpinForward, GPIO.OUT)
GPIO.setup(LFpinReverse, GPIO.OUT)
p1 = GPIO.PWM(LFpinForward, 50)
q1 = GPIO.PWM(LFpinReverse, 50)

LBpinForward = 24
LBpinReverse = 23
GPIO.setup(LBpinForward, GPIO.OUT)
GPIO.setup(LBpinReverse, GPIO.OUT)
p2 = GPIO.PWM(LBpinForward, 50)
q2 = GPIO.PWM(LBpinReverse, 50)

RFpinForward = 5
RFpinReverse = 6
GPIO.setup(RFpinForward, GPIO.OUT)
GPIO.setup(RFpinReverse, GPIO.OUT)
p3 = GPIO.PWM(RFpinForward, 50)
q3 = GPIO.PWM(RFpinReverse, 50)

RBpinForward = 26
RBpinReverse = 25
GPIO.setup(RBpinForward, GPIO.OUT)
GPIO.setup(RBpinReverse, GPIO.OUT)
p4 = GPIO.PWM(RBpinForward, 50)
q4 = GPIO.PWM(RBpinReverse, 50)

def right():
p1.start(0)
q2.start(0)
p3.start(0)
q4.start(0)

p1.ChangeDutyCycle(50)
q2.ChangeDutyCycle(50)
p3.ChangeDutyCycle(50)
q4.ChangeDutyCycle(50)
sleep(5)
p.stop()

GPIO.cleanup()

def left(): 
q1.start(0)
p2.start(0)
p3.start(0)
q4.start(0)

q1.ChangeDutyCycle(50)
p2.ChangeDutyCycle(50)
q3.ChangeDutyCycle(50)
p4.ChangeDutyCycle(50)
sleep(5)
p.stop()

GPIO.cleanup()

def forward():
p1.start(0)
p2.start(0)
p3.start(0)
p4.start(0)

p1.ChangeDutyCycle(50)
p2.ChangeDutyCycle(50)
p3.ChangeDutyCycle(50)
p4.ChangeDutyCycle(50)
sleep(5)
p.stop()

GPIO.cleanup()

def backward():
q1.start(0)
q2.start(0)
q3.start(0)
q4.start(0)

q1.ChangeDutyCycle(50)
q2.ChangeDutyCycle(50)
q3.ChangeDutyCycle(50)
q4.ChangeDutyCycle(50)
sleep(5)
p.stop()

GPIO.cleanup()