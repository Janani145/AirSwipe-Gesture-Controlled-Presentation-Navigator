import cv2
import mediapipe as mp
import pyautogui

# Initialize Mediapipe Hand module
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.6, max_num_hands=5)

# Initialize webcam
cap = cv2.VideoCapture(0)

prev_index_x = {}  # Store previous x-coordinate for index finger
prev_ring_x = {}   # Store previous x-coordinate for ring finger

selected_hand_id = None  # Initially, no hand is selected
hand_positions = {}  # Store hand positions

while cap.isOpened():
    success, img = cap.read()
    if not success:
        continue

    # Convert the image to RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    # Convert back to BGR
    img = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)

    hand_positions.clear()  # Clear previous hand positions

    if results.multi_hand_landmarks:
        for i, hand_landmarks in enumerate(results.multi_hand_landmarks):
            hand_id = i + 1  # Assign ID to hands (1, 2, 3...)
            hand_positions[hand_id] = hand_landmarks.landmark[0]  # Store wrist position

            # Draw landmarks
            mp_drawing.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Display hand ID
            wrist_x = int(hand_landmarks.landmark[0].x * img.shape[1])
            wrist_y = int(hand_landmarks.landmark[0].y * img.shape[0])
            cv2.putText(img, f"Hand {hand_id}", (wrist_x, wrist_y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

            # Ignore gestures unless a hand is selected
            if selected_hand_id is None or selected_hand_id != hand_id:
                continue  # Skip unselected hands

            # If selected, detect gestures
            index_finger_x = hand_landmarks.landmark[8].x
            ring_finger_x = hand_landmarks.landmark[16].x
            ring_raised = hand_landmarks.landmark[16].y < hand_landmarks.landmark[14].y  # Check if ring finger is up

            # Left Swipe (One Finger - Index)
            if selected_hand_id in prev_index_x and not ring_raised:
                if prev_index_x[selected_hand_id] - index_finger_x > 0.1:  # Moving left
                    print("Swipe Left ← Previous Slide")
                    pyautogui.press("left")

            # Right Swipe (Two Fingers - Index + Ring)
            if selected_hand_id in prev_index_x and selected_hand_id in prev_ring_x and ring_raised:
                if index_finger_x - prev_index_x[selected_hand_id] > 0.1 and ring_finger_x - prev_ring_x[selected_hand_id] > 0.1:
                    print("Swipe Right → Next Slide")
                    pyautogui.press("right")

            # Update previous positions for only the selected hand
            prev_index_x[selected_hand_id] = index_finger_x
            prev_ring_x[selected_hand_id] = ring_finger_x

    # Show webcam feed
    cv2.imshow("Hand Gestures", img)

    # Keyboard inputs
    key = cv2.waitKey(5) & 0xFF
    if key == ord("q"):  # Quit
        break
    elif key == ord("c"):  # Reset selection
        selected_hand_id = None
        print("Hand selection cleared.")
    elif key in [ord(str(num)) for num in range(1, 6)]:  # Select hand
        num = int(chr(key))
        if num in hand_positions:
            selected_hand_id = num
            print(f"Selected Hand {num}")

cap.release()
cv2.destroyAllWindows()
