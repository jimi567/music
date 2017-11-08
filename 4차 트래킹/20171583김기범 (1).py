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
# import trackingMoudule
# =======================================================================
from trackingMoudule import *



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



try:
    while True:
        # ultra sensor replies the distance back
        distance = getDistance()
        print('distance= ', distance)

        # when the distance is above the dis, moving object forwards
        if (distance > dis):
		tl = trackinglist
		while tl == [1,1,0,1,1] or tl ==[1,0,0,0,1]: # 전진 
			go_any_forward(30, 25)
		while tl == [0,1,1,1,1] or tl == [0,0,1,1,1] or tl == [0,0,0,1,1] or\ # 좌측 
				 tl ==[1,0,1,1,1] or tl == [1,0,0,1,1]:
			go_any_forward(30,28)
		while tl == [1,1,1,1,0] or tl == [1,1,1,0,0] or tl == [1,1,0,0,0] or\ # 우측 
				 tl ==[1,1,1,0,1] or tl == [1,1,0,0,1]:
			go_any_forward(30,30)  #제 왼쪽 모터가 오른쪽모터보다 파워가 좀더 강함 ,,,
            

        # when the distance is below the dis, moving object stops
        else:
            # stop and wait 1 second
            	stop()
            	sleep(1)
            	rightPointTurn(30, 0.2)
            	sleep(0.5)
		go_forward_any(20)
		sleep(0.5)
		leftPointturn(30, 0.2)
		sleep(0.5)
		go_forward_any(20)
		leftPointturn(30, 0.2)
		sleep(0.5)
		go_forward_any(20)
                continue


            ########################################################
            ### please continue the code or change the above code
            ### # student assignment (10)
            ########################################################


# when the Ctrl+C key has been pressed,
# the moving object will be stopped

except KeyboardInterrupt:
    pwm_low()
