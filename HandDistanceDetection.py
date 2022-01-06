import math
import random
import time

import numpy as np
from cv2 import cv2
from cvzone.HandTrackingModule import HandDetector
import cvzone

#Hand detector
detector = HandDetector(detectionCon=0.8, maxHands=1)

#Find Function
# x is the raw distance (in px) between points 5 and 17 in the hand
# (for detail see mediapipe docs for HandDetector, y is the distance in cm
# This is hardcoded solution. The distance in CM is measured by hand with the
# measuring tape and the corresponding distance in px is written down in x array.
# To calibrate for your camera you must measure the distance in cm and update
# the array.
# y = Ax**2 + Bx + C     find A, B and C
x = [300, 245, 200, 170, 145, 130, 112, 103, 93, 87, 80, 75, 70, 67, 62, 59, 57]
y = [ 20,  25,  30,  35,  40,  45,  50,  55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
coeff = np.polyfit(x, y, 2)
A, B, C = coeff

#Game Variables
cx, cy = 250, 250
button_color = (255, 0, 255)
green_color = (0, 255, 0)
purple_color = (255, 0, 255)
counter = 0
score = 0
time_start = time.time()
time_total = 40

#Webcam capture
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

#Loop
while True:
    success, img = cap.read()
    cv2.flip(img, 1, img)

    if time.time() - time_start < time_total:

        hands = detector.findHands(img, draw=False)

        if hands:
            lmList = hands[0]["lmList"]
            x, y, w, h = hands[0]["bbox"]
            x1, y1 = lmList[5]
            x2, y2 = lmList[17]

            distance = int(math.sqrt((y2-y1)**2 + (x2-x1)**2))
            distanceCM = A*distance**2 + B*distance + C

            if distanceCM < 40:
                if x < cx < x + w and y < cy < y + h:
                    counter = 1

            if counter:
                counter += 1
                button_color = green_color
                if counter == 3:
                    cx = random.randint(200, 1000)
                    cy = random.randint(200, 500)
                    button_color = purple_color
                    counter = 0
                    score += 1

            #print(distanceCM, distance)
            cv2.rectangle(img, (x,y), (x+w, y+h), purple_color,3)
            cvzone.putTextRect(img, f"{int(distanceCM)} cm", (x+5, y-10))

        #Draw Button
        cv2.circle(img, (cx, cy), 30, button_color, cv2.FILLED)
        cv2.circle(img, (cx, cy), 10, (255, 255, 255), cv2.FILLED)
        cv2.circle(img, (cx, cy), 20, (255, 255, 255), 2)
        cv2.circle(img, (cx, cy), 30, (50, 50, 50), 2)

        #Game HUD
        cvzone.putTextRect(img, f"Time: {int(time_total - (time.time() - time_start))}", (1000, 75), scale=3, offset=20)
        cvzone.putTextRect(img, f"Score: {str(score).zfill(2)}", (75, 75), scale=3, offset=20)
    else:
        cvzone.putTextRect(img, "Game over", (400, 400), scale=5, offset=30, thickness=7)
        cvzone.putTextRect(img, f"Your score: {score}", (440, 500), scale=3, offset=20)
        cvzone.putTextRect(img, "Press R to reset", (480, 575), scale=2, offset=10)

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)

    if key == ord("r"):
        time_start = time.time()
        score = 0
