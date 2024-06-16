# LED Button Control with Pico and Speaker

This project demonstrates how to control multiple LEDs using buttons and play different tones with a speaker on a Raspberry Pi Pico. It uses the `machine` and `picozero` libraries to manage hardware interactions.

## Components

- Raspberry Pi Pico
- LEDs (Green, Yellow, Orange, Red)
- Buttons (Blue, Purple, Grey, White)
- Speaker

## Connections

| Component | GPIO Pin |
|-----------|----------|
| Green LED | 21       |
| Yellow LED| 20       |
| Orange LED| 19       |
| Red LED   | 18       |
| Blue Button | 10     |
| Purple Button | 11   |
| Grey Button | 12     |
| White Button | 13    |
| Speaker | 14         |

## Features

- The onboard LED blinks at a frequency of 2.5 Hz.
- Four LEDs can be toggled using four corresponding buttons.
- Each button press will toggle an LED and play a specific tone on the speaker.

## Code

```python
from machine import Pin, Timer
import utime 
from picozero import Speaker

speaker = Speaker(14)

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
button_1_blue = Pin(10, Pin.IN)
button_2_purple = Pin(11, Pin.IN)
button_3_grey = Pin(12, Pin.IN)
button_4_white = Pin(13, Pin.IN)

while True:
    if button_1_blue.value() == 1:
        led_1_green.toggle()
        speaker.play('c3', 0.2) # Play the note C3 for 0.2 seconds
        utime.sleep(0.2)
    if button_2_purple.value() == 1:
        led_2_yellow.toggle()
        speaker.play('d3', 0.2) # Play the note D3 for 0.2 seconds
        utime.sleep(0.2)
    if button_3_grey.value() == 1:
        led_3_orange.toggle()
        speaker.play('e3', 0.2) # Play the note E3 for 0.2 seconds
        utime.sleep(0.2)
    if button_4_white.value() == 1:
        led_4_red.toggle()
        speaker.play('f3', 0.2) # Play the note F3 for 0.2 seconds
        utime.sleep(0.2)
```

## Setup

1. Connect the components to the corresponding GPIO pins on the Raspberry Pi Pico.
2. Ensure you have the `machine` and `picozero` libraries installed.
3. Upload the code to your Pico using Thonny or another suitable Python editor.
4. Run the code to start controlling the LEDs and playing tones with the buttons.

## Usage

- Press any button to toggle the corresponding LED and play the assigned tone.
- The onboard LED will blink continuously at a frequency of 2.5 Hz.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [PicoZero Library](https://github.com/RaspberryPiFoundation/picozero) for simplified hardware interaction.
- Raspberry Pi Foundation for the hardware and software support.

Feel free to contribute to this project by opening issues or submitting pull requests. Happy tinkering!