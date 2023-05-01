import RPi.GPIO as g
from time import sleep
g.setwarnings(False)
g.setmode(g.BOARD)
g.setup(8,g.OUT,initial=g.LOW)
g.setup(10,g.OUT,initial=g.LOW)
g.setup(12,g.OUT,initial=g.LOW)
P=g.PWM(8,100)
Q=g.PWM(10,100)
R=g.PWM(12,100)
P.start(0)
Q.start(0)
R.start(0)
# while True: //serial
#     for i in range (0,100,5):
#         P.ChangeDutyCycle(i)
#         sleep(0.1)
#     for i in range (0,100,5):
#         Q.ChangeDutyCycle(i)
#         sleep(0.1)
#     for i in range (0,100,5):
#         R.ChangeDutyCycle(i)
#         sleep(0.1)
#     for i in range (100,0,-5):
#         P.ChangeDutyCycle(i)
#         sleep(0.1)
#     for i in range (100,0,-5):
#         Q.ChangeDutyCycle(i)
#         sleep(0.1)
#     for i in range (100,0,-5):
#         R.ChangeDutyCycle(i)
#         sleep(0.1)
# while True: //reverse
#     for i in range (0,100,5):
#         P.ChangeDutyCycle(i)
#         sleep(0.1)
#     for i in range (100,0,-5):
#         P.ChangeDutyCycle(i)
#         sleep(0.1)
#     for i in range (0,100,5):
#         Q.ChangeDutyCycle(i)
#         sleep(0.1)
#     for i in range (100,0,-5):
#         Q.ChangeDutyCycle(i)
#         sleep(0.1)
#     for i in range (0,100,5):
#         R.ChangeDutyCycle(i)
#         sleep(0.1)
#     for i in range (100,0,-5):
#         R.ChangeDutyCycle(i)
#         sleep(0.1)

# while True: /together
# 	for i in range (0,100,5):
#         P.ChangeDutyCycle(i)
#         Q.ChangeDutyCycle(i)
#         R.ChangeDutyCycle(i)
#         sleep(0.1)
#     for i in range (100,0,-5):
#         P.ChangeDutyCycle(i)
#         Q.ChangeDutyCycle(i)
#         R.ChangeDutyCycle(i)
#         sleep(0.1)

choices=[P,Q,R] #random
while True:
    temp=random.choice(choices)
    for x in range(0,100,5):
        temp.ChangeDutyCycle(x)
        sleep(0.1)
    for x in range(100,0,-5):
        temp.ChangeDutyCycle(x)
        sleep(0.1)