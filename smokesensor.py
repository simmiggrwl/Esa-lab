#sudo raspi-config
#interfacing options->i2c->yes
#cd /etc/modules
#sudo nano /etc/modules => eof has line i2c-dev
#sudo nano /boot/config.txt =>uncomment dt.param=i2c-arm=on
#sudo apt-get install i2c-tools
#sudo reboot
#sudo i2c detect -y 1 => output should show 48 in 40th row and 8th column
#sudo pip3 install --upgrade setuptools
#sudo pip3 install RPi.GPIO adafruit_blinka
#sudo pip3 install adafruit_circuitpython_ada1x15

import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

i2c=busio.I2C(board.SCL,board.SDA)
ads=ADS.ADS1015(i2c)
ads.gain=8 #amplifying signal before it reaches adc
chan=AnalogIn(ads,ADS.P0)
# print(chan.value,chan.voltage)
print("{:>5}\t{:>5}".format('raw','v'))
while True:
    print({"{:>5}\t{:>5.5f}".format(chan.value,chan.voltage)})
    time.sleep(0.5)


#### smoke sensor has 3 pins: vcc, ground and a0: vcc to 2, ground to 20 and a0 to a0 of i2c adc
### vdd to 4, gnd to 6, scl to 5, sda to 3, addr to 12, a0 to a0 of sensor

#vdd,gnd,scl,sda,addr,alrt,a0,a1,a2,a3