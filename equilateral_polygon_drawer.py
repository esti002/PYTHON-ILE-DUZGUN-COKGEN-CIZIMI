from gettext import find
import cv2
import numpy as np
import typing
import math
from math import floor

cv2.rectangle

canvas = np.zeros((700,700,3),np.uint8)+255

#bu fonksiyona gerekli parametreleri verdigimizde olusturmak istedigimiz eskenar cokgenin kose noktalarini bizim icin tespit eder
def findPoints(parameters: typing.Tuple[int, int, int, int, int]): #bak karsim burda parametre olarak sirasiyla x noktasi, y noktasi, aci(angle), kenar uzunlugu ve kenar sayisi verildi
    
    result = np.zeros((parameters[4],2), dtype = int)
    result[0][0] = parameters[0]
    result[0][1] = parameters[1]

    angle = math.radians(parameters[2])
    inAngle = math.radians(360 / parameters[4])

    for i in range(parameters[4]-1):

        axisVar1 = math.sin(angle + (inAngle * i)) * parameters[3]
        axisVar2 = axisVar1 / math.tan(angle + (inAngle * i))

        newAxisX = axisVar1 + result[i][0]
        newAxisY = axisVar2 + result[i][1]

        result[i+1][0] = newAxisX
        result[i+1][1] = newAxisY

    return result

# bu fonksiyon bize iki nokta arasindaki dogrunun denklemini verir
def findEquation(point1: typing.Tuple[int, int], point2: typing.Tuple[int, int]): 

    m = (point2[1] - point1[1]) / (point2[0] - point1[0]) #m egimi ifade eder
    fixed = m * point1[0] * -1 + point1[1] #fixed denklemdeki sabit kismi temsil eder

    return(m,fixed)

# bu fonksiyon gerekli cokgenin cizimini gerceklestirir
def draw():
    points = findPoints((300,300,50,100,9))
    elementCount = floor(points.size / 2)
    
    minX = points[0][0]
    maxX = points[0][0]
    minY = points[0][1]
    maxY = points[0][1]
    
    for i in range(elementCount):
        if points[i][0] < minX:
            minX = points[i][0]
        if points[i][0] > maxX:
            maxX = points[i][0]

        if points[i][1] < minY:
            minY = points[i][1]
        if points[i][1] > maxY:
            maxY = points[i][1]

    for i in range(minX,maxX):
        for j in range(minY,maxY):

            canvas[i][j] = (0,0,0)

    for i in range(elementCount):
        equation = findEquation(points[i],points[(i+1) % elementCount])

        for j in range(minX,maxX):
            for k in range(minY,maxY):


                if ((equation[0] * points[(i + 2) % elementCount][0] + equation[1]) <= points[(i + 2) % elementCount][1]):
                    if ((equation[0] * j + equation[1]) > k):

                        canvas[j][k] = (255,255,255)

                if ((equation[0] * points[(i + 2) % elementCount][0] + equation[1]) >= points[(i + 2) % elementCount][1]):
                    if ((equation[0] * j + equation[1]) < k):

                        canvas[j][k] = (255,255,255)

    cv2.imshow("canvas", canvas)
    cv2.waitKey(0)

draw()