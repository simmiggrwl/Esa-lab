#git clone https://github.com/adafruit/Adafruit_Python_CharLCD.git
#cd ./Adafruit_Python_CharLCD
#sudo python3 setup.py install


import board
from time import sleep
import digitalio
import adafruit_character_lcd.character_lcd as charlcd

lcd_columns=16
lcd_rows=2
lcd_rs=digitalio.DigitalInOut(board.D26) #37
lcd_en=digitalio.DigitalInOut(board.D19) #35
lcd_d7=digitalio.DigitalInOut(board.D27) #13
lcd_d6=digitalio.DigitalInOut(board.D22) #15
lcd_d5=digitalio.DigitalInOut(board.D24) #18
lcd_d4=digitalio.DigitalInOut(board.D25) #22

lcd_backlight=digitalio.DigitalInOut(board.D4) #7

lcd=charlcd.Character_LCD_Mono(lcd_rs,lcd_en,lcd_d4,lcd_d5,;cd_d6,lcd_d7,lcd_columns,lcd_rows,lcd_backlight)
lcd.cursor_position(0,0)
lcd.message="Hi!"
lcd.cursor_position(8,0)
lcd.message="Hello World!"

# vss to 6(ground) and vdd to 2, v0 to 11, rs,en,d4,d5,d6,d7 acc to code and led- to ground(39)
# gpio26, 19, 13, 6, 5, 21 => pins 37,35,33,31,29,40
#vss vdd v0 rs r/w e d0 d1 d2 d3 d4 d5 d6 d7 led+ led-


# from Adafruit_CharLCD import Adafruit_CharLCD # Importing Adafruit library for LCD
# from time import sleep # Importing sleep from time library to add delay in program
# # initiate lcd and specify pins
# lcd = Adafruit_CharLCD (rs=26, en=19, d4=13, d5=6, d6=5, d7=21, cols=16, lines=2)
# lcd.clear()
# # display text on LCD, \n = new line
# lcd.message('WELCOME TO \nIoT STARTERS')
# sleep(2)



# import time
# import Adafruit_CharLCD as LCD

# # Raspberry Pi pin setup
# lcd_rs = 25
# lcd_en = 24
# lcd_d4 = 23
# lcd_d5 = 17
# lcd_d6 = 18
# lcd_d7 = 22
# lcd_backlight = 2

# # Define LCD column and row size for 16x2 LCD.
# lcd_columns = 16
# lcd_rows = 2

# lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

# lcd.message('Hello\nworld!')
# # Wait 5 seconds

# time.sleep(5.0)
# lcd.clear()
# text = raw_input("Type Something to be displayed: ")
# lcd.message(text)

# # Wait 5 seconds
# time.sleep(5.0)
# lcd.clear()
# lcd.message('Goodbye\nWorld!')

# time.sleep(5.0)
# lcd.clear()