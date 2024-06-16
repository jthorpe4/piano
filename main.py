from machine import Pin, Timer
import utime 
from picozero import Speaker

speaker = Speaker(14)
#speakerBig = Speaker(2)
 
print ("LED Button")
led_onboard = Pin("LED", Pin.OUT)
timer = Timer()

def blink(timer):
    led_onboard.toggle()

timer.init(freq=2.5, mode=Timer.PERIODIC, callback=blink)

led_1_green = Pin(21, Pin.OUT)
led_2_yellow = Pin(20, Pin.OUT)
led_3_orange = Pin(19, Pin.OUT)
led_4_red = Pin(18, Pin.OUT)
button_1_blue = Pin ( 10, Pin.IN)
button_2_purple = Pin ( 11, Pin.IN)
button_3_grey = Pin ( 12, Pin.IN)
button_4_white = Pin (13, Pin.IN)

#button_p1_blue = Pin ( 16, Pin.IN)
  
while True:
    if button_1_blue.value()==1:
       led_1_green.toggle()
       speaker.play('c3', 0.2) # play the middle c for half a second
       utime.sleep(0.2)
    if button_2_purple.value()==1:
       led_2_yellow.toggle()
       speaker.play('d3', 0.2) # play the middle c for half a second	
       utime.sleep(0.2)
    if button_3_grey.value()==1:
       led_3_orange.toggle()
       speaker.play('e3', 0.2) # play the middle c for half a second
       utime.sleep(0.2)
    if button_4_white.value()==1:
       led_4_red.toggle()
       speaker.play('f3', 0.2) # play the middle c for half a second
       utime.sleep(0.2)
  #  if button_p1_blue.value()==1:
    #    print ("hello")
    #    utime.sleep (0.2)
        #speakerBig.play('f3', 0.2) # play the middle c for half a second
    #Blue buttons   
    #if button_p1_blue.value()==1:
       #speakerBig.play('c3', 0.2) # play the middle c for half a second
       #print ("hello")
       #utime.sleep(0.2)
  