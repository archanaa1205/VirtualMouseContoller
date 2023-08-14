# Virtual Mouse Control Project

The Virtual Mouse Control project is a system that enables users to control the computer mouse cursor using hand gestures. 
By leveraging hand tracking technology and computer vision techniques, this project provides an alternative and intuitive
method of interacting with a computer's graphical interface.

## Project Overview

The Virtual Mouse Control system utilizes the following technologies:

- OpenCV: For capturing video input from the webcam, processing frames, and detecting hand gestures.
- MediaPipe: For hand tracking, detecting landmarks, and extracting fingertip positions.
- PyAutoGUI: For simulating mouse cursor movement and performing mouse button actions.

## Features

- **Cursor Movement:** Control the mouse cursor's position on the screen by moving your hand.
- **Left-Click and Right-Click:** Perform left-click and right-click actions by using hand gestures.
- **Drag-and-Drop:** Simulate drag-and-drop actions by moving the cursor with hand movements.

## Getting Started

1. Clone this repository to your local machine using `git clone <repository-url>`.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the project by executing `python virtual_mouse.py`.

## Usage

- Launch the project and position your hand in front of the webcam.
- Move your hand to control the cursor's position on the screen.
- Make gestures to perform left-click, right-click, and drag-and-drop actions.
- Press 'q' to exit the application.

## Contributions

Contributions to enhance the functionality, optimize performance, or add new features are welcome! 
Please open an issue or submit a pull request if you have any improvements to suggest.


## Acknowledgments

This project was inspired by the potential applications of hand tracking and computer vision in enhancing user interaction
with technology.

