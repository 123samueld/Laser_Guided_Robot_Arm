from machine import Pin, PWM
import utime

startingPos = [1,1,179]
#Min XY reach
#minPos= [90,55,90]
#Reach to dot
destPos = [89.0, 34.0, 87.0]
#Max XY reach
#maxPos = [55,50,150]

#Arm Speed, high number is slower
armSpeed = 0.1
ledState = 0

#Servo calibration
shoulderYDegree = 10555
shoulderYMax = 2650000
shoulderYMin = 1700000

shoulderZDegree = 10000
shoulderZMax = 2000000
shoulderZMin = 1550000

elbowDegree = 11389
elbowMax = 2650000
elbowSafeMin = 927780
elbowActualMin = 600000

#Pins n' freqsiz
led = Pin(16, Pin.OUT)
shoulderY = PWM(Pin(15))
shoulderZ = PWM(Pin(14))
elbow = PWM(Pin(13))
shoulderY.freq(20)
shoulderZ.freq(20)
elbow.freq(20)

def MoveToPos(destPos):
    currentPos = [0,0,180]
    incrementPercent = [1.0, 2.5, 4.0, 5.5, 9.5, 13.5, 18.5, 23.0, 33.5, 50.0, 75.0, 82.5, 87.5, 91.5, 93.5, 97.5, 98.5, 99.0, 99.5, 100]

    #Shoulder Y servo
    diffY = abs(startingPos[0]-destPos[0])/100
    diffZ = abs(startingPos[1]-destPos[1])/100
    diffEl = abs(startingPos[2]-destPos[2])/100


    for i in range(0,20):
        incrementY = incrementPercent[i]*diffY
        incrementZ = incrementPercent[i]*diffZ
        incrementEl = incrementPercent[i]*diffEl

        
        if startingPos[0] > destPos[0]:
            currentPos[0] = startingPos[0] - incrementY
        elif destPos[0] > startingPos[0]:
            currentPos[0] = startingPos[0] + incrementY
        shoulderY.duty_ns(shoulderYMin + (shoulderYDegree*int(currentPos[0])))
        
        if startingPos[1] > destPos[1]:
            currentPos[1] = startingPos[1] - incrementZ
        elif destPos[1] > startingPos[1]:
            currentPos[1] = startingPos[1] + incrementZ
        shoulderZ.duty_ns(shoulderZMin + (shoulderZDegree*int(currentPos[1])))
        
        if startingPos[2] > destPos[2]:
            currentPos[2] = startingPos[2] - incrementEl
        elif destPos[2] > startingPos[2]:
            currentPos[2] = startingPos[2] + incrementEl
        elbow.duty_ns(elbowActualMin + (elbowDegree*int(currentPos[2])))
        
        utime.sleep(armSpeed)
        print(currentPos)
        
    startingPos[0] = destPos[0]
    startingPos[1] = destPos[1]
    startingPos[2] = destPos[2]

     
    
    led.value(1)
    utime.sleep(0.1)
    led.value(0)
    utime.sleep(0.1)
    led.value(1)
    utime.sleep(0.1)
    led.value(0)
    led.value(1)
    utime.sleep(0.1)
    led.value(0)
    utime.sleep(0.1)
    led.value(1)
    utime.sleep(0.1)
    led.value(0)
    led.value(1)
    utime.sleep(0.1)
    led.value(0)
    utime.sleep(0.1)
    led.value(1)
    utime.sleep(0.1)
    led.value(0)
    
restPos = [0,0,179]
MoveToPos(restPos)
utime.sleep(1)
MoveToPos(destPos)
utime.sleep(10)
MoveToPos(restPos)






    

    
    


