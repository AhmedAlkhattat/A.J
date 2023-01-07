# A&R_main 
# This program is fairly simple - it utilises the IR and ultrasonic sensors
# on the A&R_main in order to sense obstacles and avoid them
# Created by Ahmed Alkhattat

import A&R_main, time

A&R_main.init()

# Here we set the speed to 40 out of 100 - feel free to change!
speed = 40

# Here is the main body of the program - a lot of while loops and ifs!
# In order to get your head around it go through the logical steps slowly!
try:
  while True:
    if A&R_main.irLeft():
      while A&R_main.irLeft():
        # While the left sensor detects something - spin right
        A&R_main.spinRight(speed)
      A&R_main.stop()
    if A&R_main.irRight():
      while A&R_main.irRight():
        # While the right sensor detects something - spin left
        A&R_main.spinLeft(speed)
      A&R_main.stop()
    while not (A&R_main.irLeft() or A&R_main.irRight()):
      if A&R_main.getDistance() <= 0.3: # If the distance is less than 0.3, spin right for 1 second
        A&R_main.spinRight(speed)
        time.sleep(1)
      else:
        A&R_main.forward(speed)
    A&R_main.stop()

finally: # Even if there was an error, cleanup
  A&R_main.cleanup()