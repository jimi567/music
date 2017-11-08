######################################################################
### Date: 2017/10/5
### file name: project3_student.py
### Purpose: this code has been generated for the three-wheeled moving
###         object to perform the project3 with ultra sensor
###         swing turn, and point turn
### this code is used for the student only
######################################################################

# =======================================================================
# import GPIO library and time module
# =======================================================================
import RPi.GPIO as GPIO
from time import sleep

# =======================================================================
#  set GPIO warnings as false
# =======================================================================
GPIO.setwarnings(False)

# =======================================================================
# import getDistance() method in the ultraModule
# =======================================================================
from ultraModule import getDistance

# =======================================================================
# import TurnModule() method
# =======================================================================
from TurnModule import *


# =======================================================================
# rightPointTurn() and leftPointTurn() in TurnModule module
# =======================================================================
# student assignment (1)
# student assignment (2)



# =======================================================================
# import go_forward_any(), go_backward_any(), stop(), LeftPwm(),
# RightPwm(), pwm_setup(), and pwm_low() methods in the module of go_any
# =======================================================================
from go_any import *

# implement rightmotor(x)  # student assignment (3)
# implement go_forward_any(speed): # student assignment (4)
# implement go_backward_any(speed): # student assignment (5)
# implement go_forward(speed, running_time)  # student assignment (6)
# implement go_backward(speed, running_time)  # student assignment (7)

# =======================================================================
# setup and initilaize the left motor and right motor
# =======================================================================
pwm_setup()

# =======================================================================
#  define your variables and find out each value of variables
#  to perform the project3 with ultra sensor
#  and swing turn
# =======================================================================
dis = 20  # ??
obstacle = 1

# when obstacle=1, the power and
# running time of the first turn
SwingPr = 90  # student assignment (8)
SwingTr = 0.9  # student assignment (9)
# when obstacle=2, the power and
# running time of the second turn
PointPr = 90
PointTr = 0.9
# when the half final is reached,
# the power and running time of 180 degree turn
PointP180= 90
PointT180= 1.8
# when obstacle=3, the power and
# running time of the third turn
PointPl= 90
PointTl= 0.9
# when obstacle=4, the power and
# running time of the fourth turn
SwingPl= 90
SwingTl= 0.9
# when the final is reached,
# the power and running time of 180 degree turn
PointP360= 90
PointT360= 1.8

try:
    while True:
        # ultra sensor replies the distance back
        distance = getDistance()
        print('distance= ', distance)

        # when the distance is above the dis, moving object forwards
        if (distance > dis):
            go_forward_any(50)
            print('obstacle=', obstacle)

        # when the distance is below the dis, moving object stops
        else:
            # stop and wait 1 second
            stop()
            sleep(1)
            if obstacle == 1:
                rightSwingTurn(SwingPr, SwingTr)
                sleep(0.5)
                obstacle += 1
                continue
            if obstacle == 2:
                rightPointTurn(PointPr, PointTr)
                sleep(0.5)
                go_forward(50, 3)
                stop()
                sleep(1)
                rightPointTurn(PointP180, PointT180)
                sleep(0.5)
                obstacle += 1
                continue
            if obstacle == 3:
                leftPointTurn(PointPl, PointTl= 0.9)
                sleep(0.5)
                obstacle += 1
                continue
            if obstacle == 4:
                leftSwingTurn(SwingPl, SwingTl)
                sleep(0.5)
                go_forward(50, 3)
                stop()
                sleep(1)
                rightPointTurn(PointP360, PointT360)
                break


            ########################################################
            ### please continue the code or change the above code
            ### # student assignment (10)
            ########################################################


# when the Ctrl+C key has been pressed,
# the moving object will be stopped

except KeyboardInterrupt:
    pwm_low()
