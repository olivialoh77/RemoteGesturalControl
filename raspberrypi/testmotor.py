import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

pinForward = 23
pinReverse = 24

GPIO.setup(pinForward, GPIO.OUT)
GPIO.setup(pinReverse, GPIO.OUT)

p = GPIO.PWM(pinForward, 50)
q = GPIO.PWM(pinReverse, 50)

p.start(0)
p.ChangeDutyCycle(50)
sleep(5)
p.stop()

q.start(0)
q.ChangeDutyCycle(50)
sleep(5)
q.stop()

GPIO.cleanup()