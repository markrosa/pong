from machine import Pin, Timer
from lib.lcd_1inch14 import LCD_1inch14
from random import randint


LCD = LCD_1inch14()
#color BRG
LCD.fill(LCD.black)

LCD.show()
LCD.text("Raspberry Pi Pico",90,40,LCD.red)
LCD.text("PicoGo",90,60,LCD.green)
LCD.text("Pico-LCD-1.14",90,80,LCD.blue)



LCD.hline(10,10,220,LCD.blue)
LCD.hline(10,125,220,LCD.blue)
LCD.vline(10,10,115,LCD.blue)
LCD.vline(230,10,115,LCD.blue)


LCD.show()
keyA = Pin(15,Pin.IN,Pin.PULL_UP)
keyB = Pin(17,Pin.IN,Pin.PULL_UP)

key2 = Pin(2 ,Pin.IN,Pin.PULL_UP) #上 Oben
key3 = Pin(3 ,Pin.IN,Pin.PULL_UP)#中 Mitte
key4 = Pin(16 ,Pin.IN,Pin.PULL_UP)#左 Links
key5 = Pin(18 ,Pin.IN,Pin.PULL_UP)#下 Unten
key6 = Pin(20 ,Pin.IN,Pin.PULL_UP)#右 Rechts

while(1):
    if(keyA.value() == 0):
        LCD.fill_rect(208,12,20,20,LCD.red)
    else :
        LCD.fill_rect(208,12,20,20,LCD.white)
        LCD.rect(208,12,20,20,LCD.red)
        
        
    if(keyB.value() == 0):
        LCD.fill_rect(208,103,20,20,LCD.red)
    else :
        LCD.fill_rect(208,103,20,20,LCD.white)
        LCD.rect(208,103,20,20,LCD.red)




    if(key2.value() == 0):#上
        LCD.fill_rect(37,35,20,20,LCD.red)
    else :
        LCD.fill_rect(37,35,20,20,LCD.white)
        LCD.rect(37,35,20,20,LCD.red)
        
        
    if(key3.value() == 0):#中
        LCD.fill_rect(37,60,20,20,LCD.red)
    else :
        LCD.fill_rect(37,60,20,20,LCD.white)
        LCD.rect(37,60,20,20,LCD.red)
        
    

    if(key4.value() == 0):#左
        LCD.fill_rect(12,60,20,20,LCD.red)
    else :
        LCD.fill_rect(12,60,20,20,LCD.white)
        LCD.rect(12,60,20,20,LCD.red)
        
        
    if(key5.value() == 0):#下
        LCD.fill_rect(37,85,20,20,LCD.red)
    else :
        LCD.fill_rect(37,85,20,20,LCD.white)
        LCD.rect(37,85,20,20,LCD.red)
        
        
    if(key6.value() == 0):#右
        LCD.fill_rect(62,60,20,20,LCD.red)
    else :
        LCD.fill_rect(62,60,20,20,LCD.white)
        LCD.rect(62,60,20,20,LCD.red)

        
    LCD.show()
time.sleep(1)
LCD.fill(0xFFFF)
