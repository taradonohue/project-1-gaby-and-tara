#Project 1
#NAME(S): Gaby Ackermann Logan and Tara Donohue
#HOURS WORKED ON: 2

import microbit as mb
import radio  # Needs to be imported separately
import math
import time


# Change the channel if other microbits are interfering. (Default=7)
radio.on()  # Turn on radio
radio.config(channel=6, length=100)

print('Program Started')
mb.display.show(mb.Image.HAPPY)

while not mb.button_a.is_pressed():  # wait for button A to be pressed to begin logging
    mb.sleep(10)

radio.send('start') # Send the word 'start' to start the receiver
mb.sleep(1000)
mb.display.show(mb.Image.HEART)  # Display Heart while logging

# Read and send accelerometer data repeatedly until button A is pressed again
while not mb.button_a.is_pressed():
    time = mb.running_time()/1000
    x = mb.accelerometer.get_x()
    y = mb.accelerometer.get_y()
    z = mb.accelerometer.get_z()
#     x_data = find_tilt_x(x, y, z)
#     y_data = find_tilt_y(x, y, z)
#     z_data = find_tilt_z(x, y, z)
    message1 = (x ,y ,z , time)
    message = str(message1)
    radio.send(message)
    mb.sleep(10)



mb.display.show(mb.Image.SQUARE)  # Display Square when program ends
