import RPi.GPIO as g
from time import sleep
g.setwarnings(False)
g.setmode(g.BOARD)
inp=8
led=10
g.setup(inp. g.IN)
g.setup(led, g.OUT)
# while True:
#     if g.input(inp):
#         g.output(led, g.HIGH)
#         print("Motion detected")
#     else:
#         g.output(led, g.LOW)
#         print("No motion detected")
#     sleep(1)




#### sensor has 4 pins: ground, echo, trig and positive, ground to 6, echo to 12, trig to 8 and + to 2 
# 2 and 4 are 5v, 1 and 17 are 3.3v 