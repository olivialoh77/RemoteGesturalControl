import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BCM)

LFpinForward = 23
LFpinReverse = 24
GPIO.setup(LFpinForward, GPIO.OUT)
GPIO.setup(LFpinReverse, GPIO.OUT)
p1 = GPIO.PWM(LFpinForward, 50)
q1 = GPIO.PWM(LFpinReverse, 50)

LBpinForward = 27
LBpinReverse = 22
GPIO.setup(LBpinForward, GPIO.OUT)
GPIO.setup(LBpinReverse, GPIO.OUT)
p2 = GPIO.PWM(LBpinForward, 50)
q2 = GPIO.PWM(LBpinReverse, 50)

RFpinForward = 25
RFpinReverse = 26
GPIO.setup(RFpinForward, GPIO.OUT)
GPIO.setup(RFpinReverse, GPIO.OUT)
p3 = GPIO.PWM(RFpinForward, 50)
q3 = GPIO.PWM(RFpinReverse, 50)

RBpinForward = 6
RBpinReverse = 5
GPIO.setup(RBpinForward, GPIO.OUT)
GPIO.setup(RBpinReverse, GPIO.OUT)
p4 = GPIO.PWM(RBpinForward, 50)
q4 = GPIO.PWM(RBpinReverse, 50)

def left():
    p1.start(0)
    q2.start(0)
    p3.start(0)
    q4.start(0)

    p1.ChangeDutyCycle(80)
    q2.ChangeDutyCycle(80)
    p3.ChangeDutyCycle(80)
    q4.ChangeDutyCycle(80)
    sleep(1)

    p1.stop()
    q2.stop()
    p3.stop()
    q4.stop()

def right(): 
    q1.start(0)
    p2.start(0)
    q3.start(0)
    p4.start(0)

    q1.ChangeDutyCycle(80)
    p2.ChangeDutyCycle(80)
    q3.ChangeDutyCycle(80)
    p4.ChangeDutyCycle(80)
    sleep(1)
    
    q1.stop()
    p2.stop()
    q3.stop()
    p4.stop()

def backward():
    p1.start(0)
    p2.start(0)
    p3.start(0)
    p4.start(0)

    p1.ChangeDutyCycle(80)
    p2.ChangeDutyCycle(80)
    p3.ChangeDutyCycle(80)
    p4.ChangeDutyCycle(80)
    sleep(1)

    p1.stop()
    p2.stop()
    p3.stop()
    p4.stop()

def forward():
    q1.start(0)
    q2.start(0)
    q3.start(0)
    q4.start(0)

    q1.ChangeDutyCycle(80)
    q2.ChangeDutyCycle(80)
    q3.ChangeDutyCycle(80)
    q4.ChangeDutyCycle(80)
    sleep(1)

    q1.stop()
    q2.stop()
    q3.stop()
    q4.stop()

