import RPi.GPIO as g
from time import sleep
g.setwarnings(False)
g.setmode(g.BOARD)
arr=[[1,1,1,1,1,1,0],[0,1,1,0,0,0,0],[1,1,0,1,1,0,1],[1,1,1,1,0,0,1],[0,1,1,0,0,1,1],[1,0,1,1,0,1,1],[1,0,1,1,1,1,1],[1,1,1,0,0,0,0],[1,1,1,1,1,1,1],[1,1,1,1,0,1,1]]
x=[3,5,11,15,19,18,22] # g f commonanode a b decimalpoint c commoncathode d e in clockwise manner
for i in x:
    g.setup(i,g.OUT,initial=g.LOW)

# while True:
#     for num in arr:
#         for i in range (0,7):
#             if(num[i]==1):
#                 g.output(x[i],g.HIGH)
#         sleep(1.2)
#         for i in range (0,7):
#             g.output(x[i],g.LOW)


#trafficlights:
led=[8,10,12]
for i in led:
    g.setup(i,g.OUT,initial=g.LOW)

j=0
while True:
    for num in digits:
        for i in range (0,7):
            if(num[i]==1):
                g.output(x[i],g.HIGH)
        sleep(1.0)
        for i in range (0,7):
            g.output(x[i],g.LOW)

    g.output(led[j%3],g.LOW)
    sleep(1)
    j=j+1 
    g.output(led[j%3],g.HIGH)
