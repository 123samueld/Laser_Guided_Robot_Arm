import math
import cv2 as c
import numpy as np
from PIL import Image

def main():
	XYcoords =  XYFinder(imgIntoArr())
	XYAdjusted = adjustXYForArmBase(XYcoords)
	print("XY pos of target:", XYcoords)
	hypotenuse = getTheHype(XYAdjusted)
	theta = getTheta(XYcoords)
	angles = generateJointAngles(theta, hypotenuse, XYAdjusted)
	return angles
	

def imgIntoArr():
	path = 	"####/Desktop/Laser_Guided_Robot_Arm/img/red_dot.png"

	pic = Image.open(path)
	pix = np.array(pic)


	yLen = len(pix)
	xLen = len(pix[0])

	XYarr = []
	Y = []


	for i in range(0, yLen):
	    for j in range(0, xLen):
	        if pix[i][j][0] > 200:
	            Y.append(1)
	        else:
	        	Y.append(0)
	    XYarr.append(Y)
	    Y = []
	XYarr.reverse()
	print(XYarr)
	return XYarr

def XYFinder(imgArr):
	X = []
	Y = []
	XYList = []
	yLen = len(imgArr)
	xLen = len(imgArr[0])

	found = False

	for i in range(0, yLen):
		for j in range(0, xLen):
			if imgArr[i][j] == 1:
				found = True
				if j not in Y:
					Y.append(j)
		if found:
			X.append(i)
			found = False
	xMax = np.max(X) 
	xMin = np.min(X)
	yMax = np.max(Y)
	yMin = np.min(Y)
	indexX = (xMax-xMin)/2 + xMin
	indexY = (yMax-yMin)/2 + yMin
	XY = [int(indexX), int(indexY)]
	XY.reverse()
	return XY


def adjustXYForArmBase(XY):
	armBaseXPx = 503
	armBaseYPx = 50

	viewPortWidthInMM = 262
	viewPortWidthInPx = 1920
	pxPerMM = viewPortWidthInPx/viewPortWidthInMM


	armBaseOffsetX = 75
	armBaseOffsetY = 75

	XYAdjusted = []
	adjustedX = round((XY[0]-armBaseXPx)/pxPerMM,0)
	XYAdjusted.append(adjustedX)
	adjustedY = round((XY[1]-armBaseYPx)/pxPerMM,0)
	XYAdjusted.append(adjustedY)
	XYAdjusted[0] = XYAdjusted[0]
	XYAdjusted[1] = XYAdjusted[1]

	return XYAdjusted


def getTheta(XY):
	thetaRads = math.atan(XY[0]/XY[1])
	theta = 90 - math.degrees(thetaRads)
	return theta

def getTheHype(XY):
	hypotenuseRaw = math.sqrt((XY[0] **2)+(XY[1]**2))
	hypotenuse = round(hypotenuseRaw, 2)
	return hypotenuse

def generateJointAngles(theta, hypotenuse, XY):
	focalLength = 190
	lenOfRobotArm = 140
	angles = []

	#Get Shoulder Y Theta and Hype
	yShoulderTheta = round(math.degrees(math.atan(focalLength/XY[0])),0)
	yAPlusO = math.pow(focalLength,2) + math.pow(XY[0],2)
	yShoulderHype = math.sqrt(yAPlusO)

	#Get Shoulder Z Theta and Hype
	zShoulderTheta = 90 - round(math.degrees(math.atan(XY[1]/yShoulderHype)),0)
	zAPlusO = math.pow(XY[1],2) + math.pow(yShoulderHype,2)
	zShoulderHype = math.sqrt(zAPlusO)

	#Get Elbow Theta
	elbowCosA = (2*math.pow(lenOfRobotArm, 2)-math.pow(zShoulderHype,2))/(2*math.pow(lenOfRobotArm,2))
	elbowTheta = round(math.degrees(math.acos(elbowCosA)),0)

	zShoulderTheta = zShoulderTheta - ((180-elbowTheta)/2)

	a= lenOfRobotArm
	b= lenOfRobotArm
	c=hypotenuse
	CosA = (math.pow(b,2)+math.pow(c,2)-math.pow(a,2))/(2*b*c)
	A = round(math.degrees(math.acos(CosA)),0)
	B = A
	C = A+B

	angles.append(yShoulderTheta)
	angles.append(zShoulderTheta)
	angles.append(elbowTheta)
	return angles

print(main())