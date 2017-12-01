import RPi.GPIO as GPIO
import time

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    global MotorLeft_A, MotorLeft_B, MotorLeft_PWM
    global MotorRight_A, MotorRight_B, MotorRight_PWM 
    MotorLeft_A = 12
    MotorLeft_B = 11
    MotorLeft_PWM = 35
    MotorRight_A = 15
    MotorRight_B = 13
    MotorRight_PWM = 37

    global trig, echo
    trig = 33
    echo = 31

    global otd, otb, ota, otc, ote
    otd = 16
    otb = 18
    ota = 22
    otc = 40
    ote = 32

    GPIO.setup(MotorLeft_A, GPIO.OUT)
    GPIO.setup(MotorLeft_B, GPIO.OUT)
    GPIO.setup(MotorLeft_PWM, GPIO.OUT)
    GPIO.setup(MotorRight_A, GPIO.OUT)
    GPIO.setup(MotorRight_B, GPIO.OUT)
    GPIO.setup(MotorRight_PWM, GPIO.OUT)

    GPIO.setup(trig, GPIO.OUT)
    GPIO.setup(echo, GPIO.IN)

    GPIO.setup(otd, GPIO.IN)
    GPIO.setup(otb, GPIO.IN)
    GPIO.setup(ota, GPIO.IN)
    GPIO.setup(otc, GPIO.IN)
    GPIO.setup(ote, GPIO.IN)

    global LeftPwm, RightPwm
    LeftPwm = GPIO.PWM(MotorLeft_PWM, 100)
    RightPwm = GPIO.PWM(MotorRight_PWM, 100)

    LeftPwm.start(0)
    RightPwm.start(0)

    global forward0, forward1, backward0 , backward1
    forward0 = False
    forward1 = True

    backward0 = True
    backward1 = False


def leftmotor(x):
    if x == True:
        GPIO.output(MotorLeft_A, GPIO.HIGH)
        GPIO.output(MotorLeft_B, GPIO.LOW)
    elif x == False:
        GPIO.output(MotorLeft_A, GPIO.LOW)
        GPIO.output(MotorLeft_B, GPIO.HIGH)
    else:
        print('Config Error')


def rightmotor(x):
    if x == True:
        GPIO.output(MotorRight_A, GPIO.LOW)
        GPIO.output(MotorRight_B, GPIO.HIGH)
    elif x == False:
        GPIO.output(MotorRight_A, GPIO.HIGH)
        GPIO.output(MotorRight_B, GPIO.LOW)
    else:
        print('Config Error')

def stop():
    GPIO.output(MotorLeft_PWM, GPIO.LOW)
    LeftPwm.ChangeDutyCycle(0)

    GPIO.output(MotorRight_PWM, GPIO.LOW)
    RightPwm.ChangeDutyCycle(0)


def getSensor():
    Sensor = [GPIO.input(otd),
           GPIO.input(otb),
           GPIO.input(ota),
           GPIO.input(otc),
           GPIO.input(ote)]
    return Sensor

def go_forward(rs, ls , t):
    leftmotor(forward0)
    GPIO.output(MotorLeft_PWM,GPIO.HIGH)
    rightmotor(forward0)
    GPIO.output(MotorRight_PWM,GPIO.HIGH)
    LeftPwm.ChangeDutyCycle(40 + (ls))
    RightPwm.ChangeDutyCycle(48 + (rs))
    time.sleep(t)

def ptL(rs, ls, b,t):
    leftmotor(backward0)
    GPIO.output(MotorLeft_PWM,GPIO.HIGH)
    rightmotor(forward0)
    GPIO.output(MotorRight_PWM,GPIO.HIGH)
    LeftPwm.ChangeDutyCycle(ls)
    RightPwm.ChangeDutyCycle(rs + 8)
    if b:
        time.sleep(t)

def ptR(rs, ls , b,t):
    leftmotor(forward0)
    GPIO.output(MotorLeft_PWM,GPIO.HIGH)
    rightmotor(backward0)
    GPIO.output(MotorRight_PWM,GPIO.HIGH)
    LeftPwm.ChangeDutyCycle(ls)
    RightPwm.ChangeDutyCycle(rs + 8)
    if b:
        time.sleep(t)
def TurnR():
    while True:
        sl = getSensor()
        if sl[4] == 0:
            go_forward(0,0,0.0001)
        if sl[2] == 1:
            ptR(50,50,True,0.1)
        elif sl[2] == 0:
            break
def TurnL():
    while True:
        sl = getSensor()
        if sl[0] == 0:
            go_forward(0,0,0.0001)
        if sl[2] == 1:
            ptL(50,50,True,0.1)
        elif sl[2] == 0:
            break
def linetracing():
    while True:
        go_forward(0,0,1)

def U_Turn():
    while True:
        sl = getSensor()
        if sl[2] == 1:
            ptR(50,50,True,0.1)
        elif sl[2] == 0:
            break

def maze(sl):

    if sl == [0,0,0,0,0]:
        go_forward(0,0,1)
        sl = getSensor()
        if sl == [0,0,0,0,0]:
            stop()
            GPIO.cleanup()



    elif sl[4] == 0:
        TurnR()

    elif sl[2] == 0:
        linetracing()

    elif sl[0] == 0:
        TurnL()

    elif sl == [1,1,1,1,1]:
        go_forward(0,0,0.2)
        sl = getSensor()
        if sl == [1,1,1,1,1]:
            U_Turn()





    return True


if __name__ == '__main__':
    try:
        setup()
        while True:
            SensorList = getSensor()
            print(SensorList)
            gotracing = maze(SensorList)

    except KeyboardInterrupt:
        stop()
        GPIO.cleanup()


