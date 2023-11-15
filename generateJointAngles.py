import math


def findShoulderYAndAD(XY):
	AB = 190
	BD = XY[0]
	AD = math.sqrt(math.pow(AB,2)+math.pow(BD,2))
	ATheta1 = round(math.degrees(math.atan(AB/BD)), 0)

	shoulderYAndAD = [ATheta1,AD]
	return shoulderYAndAD

def findPartialShoulderZAndAC(XY, AD):
	DC = XY[1]
	print("DC", DC)
	print("AD",AD)
	AC = math.sqrt(math.pow(AD,2)+math.pow(DC,2))
	print("AC", AC)
	ATheta2 = round(math.degrees(math.atan(DC/AD)), 0)
	partialShoulderZ = ATheta2

	partialShoulderZAndAC = [partialShoulderZ,AC]

	return partialShoulderZAndAC

def findFullShoulderZAndElbow(partialShoulderZ, AC):
	AE = 140
	EC = 140
	a = AC
	b = AE
	CosE = (2*math.pow(b, 2)-math.pow(a,2))/(2*math.pow(b,2))
	E = round(math.degrees(math.acos(CosE)),0)
	ETheta = E
	Elbow = ETheta
	ATheta3 = (180-ETheta)/2
	shoulderZ = round(90- (partialShoulderZ + ATheta3),0)

	fullShoulderZAndElbow = [shoulderZ,Elbow]
	return fullShoulderZAndElbow

def generateJointAngles(XY):
	theta1AndHype1 = findShoulderYAndAD(XY)
	theta2AndHype2 = findPartialShoulderZAndAC(XY, theta1AndHype1[1])
	theta2AndTheta4 = findFullShoulderZAndElbow(theta2AndHype2[0], theta2AndHype2[1])
	servoAngles = [theta1AndHype1[0], theta2AndTheta4[0], theta2AndTheta4[1]]

	return servoAngles	

XY = [62.0, 67.0]

print(generateJointAngles(XY))