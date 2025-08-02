import cv2
import mediapipe as mp
import pyautogui
import time

# Initialize webcam
cap = cv2.VideoCapture(0)

# Initialize MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7)
draw = mp.solutions.drawing_utils

# Finger tip IDs (for detection)
fingertip_ids = [8, 12, 16, 20]

# Swipe detection state
prev_x = 0
swipe_cooldown = 1  # seconds
last_swipe_time = 0

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:
            draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)
            landmarks = hand.landmark
            h, w, _ = frame.shape

            # Gesture Detection (Fingers Up)
            fingers_up = []

            # Thumb
            if landmarks[4].x < landmarks[3].x:
                fingers_up.append(1)
            else:
                fingers_up.append(0)

            # Other fingers
            for id in fingertip_ids:
                if landmarks[id].y < landmarks[id - 2].y:
                    fingers_up.append(1)
                else:
                    fingers_up.append(0)

            total_fingers = sum(fingers_up)

            # Show total fingers
            cv2.putText(frame, f"Fingers: {total_fingers}", (10, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # Action Mapping
            if total_fingers == 0:
                pyautogui.press("down")
                cv2.putText(frame, "ROLL", (10, 100),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 3)
            elif total_fingers >= 4:
                pyautogui.press("up")
                cv2.putText(frame, "JUMP", (10, 100),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 255), 3)

            # Swipe Detection
            current_x = landmarks[0].x  # wrist x
            now = time.time()
            delta_x = current_x - prev_x

            if abs(delta_x) > 0.15 and (now - last_swipe_time) > swipe_cooldown:
                if delta_x > 0:
                    pyautogui.press("right")
                    cv2.putText(frame, "SWIPE RIGHT", (10, 150),
                                cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 255), 3)
                else:
                    pyautogui.press("left")
                    cv2.putText(frame, "SWIPE LEFT", (10, 150),
                                cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 0), 3)
                last_swipe_time = now

            prev_x = current_x
    resized_frame = cv2.resize(frame, (640, 480))  # You can change size here
    cv2.imshow("HandySurfer - Gesture Control", resized_frame)


    if cv2.waitKey(1) & 0xFF == 27:  # ESC to exit
        break

cap.release()
cv2.destroyAllWindows()