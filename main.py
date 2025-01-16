import cv2
import mediapipe as mp

# Setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# Landmarks
def classify_hand_gesture(landmarks):
    thumb_tip = landmarks[4]
    index_tip = landmarks[8]
    middle_tip = landmarks[12]
    ring_tip = landmarks[16]
    pinky_tip = landmarks[20]
    
    # Check for 'Paper'
    if (thumb_tip[1] < landmarks[3][1] and 
        index_tip[1] < landmarks[7][1] and
        middle_tip[1] < landmarks[11][1] and
        ring_tip[1] < landmarks[15][1] and
        pinky_tip[1] < landmarks[19][1]):
        return 'paper'

    # Check for 'Rock'
    if (thumb_tip[1] > landmarks[3][1] and
        index_tip[1] > landmarks[7][1] and
        middle_tip[1] > landmarks[11][1] and
        ring_tip[1] > landmarks[15][1] and
        pinky_tip[1] > landmarks[19][1]):
        return 'rock'
    
    # Check for 'Scissors'
    if (index_tip[1] < landmarks[7][1] and
        middle_tip[1] < landmarks[11][1] and
        thumb_tip[1] > landmarks[3][1] and
        ring_tip[1] > landmarks[15][1] and
        pinky_tip[1] > landmarks[19][1]):
        return 'scissors'

    # Default
    return 'unknown'

# Winner
def determine_winner(gesture1, gesture2):
    rules = {
        'rock': 'scissors',
        'scissors': 'paper',
        'paper': 'rock'
    }
    if gesture1 == gesture2:
        return "Draw"
    elif rules[gesture1] == gesture2:
        return "Player 1 Wins!"
    else:
        return "Player 2 Wins!"

# Start capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    frame = cv2.flip(frame, 1)
    height, width, _ = frame.shape
    half_width = width // 2

    # Draw boundaries
    cv2.line(frame, (half_width, 0), (half_width, height), (255, 255, 255), 2)

    # Process landmarks
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    player1_gesture = "unknown"
    player2_gesture = "unknown"
    player1_position = None
    player2_position = None

    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            hand_landmarks = [(lm.x * width, lm.y * height) for lm in landmarks.landmark]
            gesture = classify_hand_gesture(hand_landmarks)
            x_pos = hand_landmarks[9][0]
            y_pos = int(hand_landmarks[9][1])

            if x_pos < half_width and player1_gesture == "unknown":
                player1_gesture = gesture
                player1_position = (int(x_pos), y_pos)
            elif x_pos >= half_width and player2_gesture == "unknown":
                player2_gesture = gesture
                player2_position = (int(x_pos), y_pos)

    # Display gestures
    if player1_position:
        cv2.putText(frame, f"{player1_gesture}", player1_position, cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    if player2_position:
        cv2.putText(frame, f"{player2_gesture}", player2_position, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Determine winner
    if player1_gesture != "unknown" and player2_gesture != "unknown":
        result = determine_winner(player1_gesture, player2_gesture)
        cv2.putText(frame, result, (width // 4, height - 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 3)

    # Display frame
    cv2.imshow('Rock Paper Scissors Gesture Recognition', frame)

    # Exit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
