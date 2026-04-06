import cv2
import mediapipe as mp
import pyautogui

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
screen_w, screen_h = pyautogui.size()

def process_gesture():
    cap = cv2.VideoCapture(0)

    while True:
        success, img = cap.read()
        img = cv2.flip(img, 1)

        results = hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                lm = handLms.landmark

                index = lm[8]
                thumb = lm[4]

                x = int(index.x * screen_w)
                y = int(index.y * screen_h)

                pyautogui.moveTo(x, y)

                # Click gesture
                if abs(index.x - thumb.x) < 0.03:
                    pyautogui.click()

        cv2.imshow("Gesture Control", img)

        if cv2.waitKey(1) & 0xFF == 27:
            break