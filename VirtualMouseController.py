import cv2
import numpy as np
import mediapipe as mp
import pyautogui

# Initialize hand tracking
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Initialize video capture
cap = cv2.VideoCapture(0)

# Initialize mouse button state variables
left_button_pressed = False
right_button_pressed = False
prev_x, prev_y = 0, 0

with mp_hands.Hands(static_image_mode=False, max_num_hands=1) as hands:
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            print("Failed to read video feed.")
            break

        # Convert the BGR image to RGB and process it with MediaPipe
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(image)

        # Get the height and width of the frame
        height, width, _ = frame.shape

        # Check if hand landmarks are detected
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Get the coordinates of the index finger tip
                index_finger = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                index_x, index_y = int(index_finger.x * width), int(index_finger.y * height)

                # Set the position of the mouse cursor
                pyautogui.moveTo(index_x, index_y)

                # Perform left-click action
                if not left_button_pressed:
                    pyautogui.mouseDown(button='left')
                    left_button_pressed = True

                # Perform right-click action
                if not right_button_pressed:
                    pyautogui.mouseDown(button='right')
                    right_button_pressed = True

                # Perform drag-and-drop action
                if prev_x != 0 and prev_y != 0:
                    pyautogui.dragTo(index_x, index_y, button='left')

                # Update previous coordinates
                prev_x, prev_y = index_x, index_y

        else:
            # Release mouse buttons if hand is not detected
            if left_button_pressed:
                pyautogui.mouseUp(button='left')
                left_button_pressed = False
            if right_button_pressed:
                pyautogui.mouseUp(button='right')
                right_button_pressed = False
            prev_x, prev_y = 0, 0

        # Display the frame
        cv2.imshow("Virtual Mouse Control", frame)

        # Break the loop by pressing the 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
