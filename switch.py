import RPi.GPIO as g
from time import sleep
button_pin=16
g.setwarnings(False)
g.setmode(g.BOARD)
g.setup(button_pin,g.IN, pull_up_down=g.PUD_UP) #voltage set to 1 to be brought to 0 by external force
g.setup(8,g.OUT,initial=g.LOW)
g.setup(12,g.OUT,initial=g.LOW)
# while True:
#     g.wait_for_edge(button_pin, g.RISING)
#     g.output(8,g.HIGH)
#     g.output(12,g.HIGH)
#     sleep(1)
#     print("led glowing")
#     g.wait_for_edge(button_pin, g.FALLING)
#     g.output(8,g.LOW)
#     g.output(12,g.LOW)
#     sleep(1)
#     print("led stopped glowing")
# g.cleanup()


#PWM PATTERN alternate increase
# P=g.PWM(8,100)
# Q=g.PWM(12,100)
# P.start(0)
# Q.start(100)
# while True:
#     g.wait_for_edge(button_pin,g.FALLING)
#     for x in range (0,100,1):
#         P.ChangeDutyCycle(x)
#         Q.ChangeDutyCycle(100-x)
#         sleep(0.01)
#     print("intensity of led increasing")
#     g.wait_for_edge(button_pin,g.RISING)
#     for x in range (100,0,-1):
#         P.ChangeDutyCycle(x)
#         Q.ChangeDutyCycle(100-x)
#         sleep(0.01)
#     print("intensity of led decreasing")
# g.cleanup()

#glows in serial, goes out in reverse
while True:
    g.wait_for_edge(button_pin,g.RISING)
    g.output(8,g.HIGH)
    sleep(1)
    print("LED 1 glowing")
    g.wait_for_edge(button_pin,g.RISING)
    g.output(12,g.HIGH)
    sleep(1)
    print("LED 2 glowing")
    g.wait_for_edge(button_pin,g.FALLING)
    g.output(8,g.LOW)
    sleep(1)
    print("LED 2 stopped")
    g.wait_for_edge(button_pin,g.FALLING)
    g.output(12,g.LOW)
    sleep(1)
    print("LED 1 stopped")
g.cleanup()