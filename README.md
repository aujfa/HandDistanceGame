# Hand Distance Measurement with Normal Webcam + Game 

This project uses the distance between a single camera and a hand. Knowledge about basic mathematics is needed to create this application. Simple game is created using the measured distance.

https://user-images.githubusercontent.com/37661642/155226788-5383c7f2-999b-4022-87fa-a67a17d9a9a1.mp4

## Getting Started

### Requirements

- python 3.10.1
- cvzone 1.5.3
- mediapipe 0.8.9.1

### Installation

Make sure you have installed cvzone and mediapipe packages before running the `HandDistanceDetection.py`

## How to Play

The countdown in the game starts as soon as you run the `HandDistanceDetection.py`. Remaining time is shown in the upper right corner. Your current score is shown in the upper left corner. Your goal is to press as many buttons as you can before the time runs out. When the time runs out, your score will be displayed on the screen. If you want to play again after the time has run out you can press "R" on the keyboard to reset the game.

### Rules

To get a point you must **PRESS** the button. The successful button press is recorded only in the case where you place your hand covering the button and move closer to the camera so that the button turns green. After the button has changed the color you need to move your hand away from the camera. Keeping your hand close to the camera at all times won't get you points!

## Resources

Code is based on tutorial by [Murtaza's Workshop - Robotics and AI](https://www.computervision.zone/courses/hand-distance-measurement/)


