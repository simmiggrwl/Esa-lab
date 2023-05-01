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


#no of motions
digits=[[1,1,1,1,1,1,0],[0,1,1,0,0,0,0],[1,1,0,1,1,0,1],[1,1,1,1,0,0,1],[0,1,1,0,0,1,1],[1,0,1,1,0,1,1],[1,0,1,1,1,1,1],[1,1,1,0,0,0,0],[1,1,1,1,1,1,1],[1,1,1,1,0,1,1]]
pins=[12,16,15,22,24,3,5] # g f commonanode a b decimalpoint c commoncathode d e in clockwise manner
for i in range (0,7):
    g.setup(pins[i], g.OUT, initial=g.LOW)

dig=0

def digitDisplay(digit):
    for i in range (0,7):
        if(digit[i]==1):
            g.output(pins[i],g.HIGH)

while True:
    if g.input(inp):
        digitDisplay(digits[dig])
        dig=(dig+1)%10
    sleep(1)



#### sensor has 3 pins: ground, pinout and vcc, ground to 6, pinout to inp, and vcc to 1 