# Gesture Duel: Hand Battle Showdown

### A fun and interactive Rock-Paper-Scissors game powered by computer vision and gesture recognition!

---

## Overview
**Gesture Duel: Hand Battle Showdown** is a modern twist on the classic game of Rock-Paper-Scissors. Using a single camera and Mediapipe's Hand Tracking technology, this project allows two players to compete by displaying gestures with their hands. The game dynamically detects gestures, identifies the winner, and displays results in real time.

---

## Features
- **Single Camera Support**: Both players share one camera, with gestures detected on separate sides of the frame.
- **Real-Time Gesture Recognition**: Recognizes "Rock," "Paper," and "Scissors" instantly using hand landmarks.
- **Dynamic Feedback**: Displays each player's gesture above their hand and announces the winner at the bottom of the screen.
- **Simple and Fast**: No countdowns or delays – just play immediately.

---

## Getting Started
1. **Clone this repository**:
   ```bash
   idk man just download it and enter it

2. **Install dependencies**:
   ```bash
   pip install opencv-python mediapipe
   ```

3. **Run the game**:
   ```bash
   python main.py
   ```

---

## How to Play
1. Ensure both players are visible in the camera feed:
   - **Player 1**: Place your hand on the **left** side of the screen.
   - **Player 2**: Place your hand on the **right** side of the screen.

2. Display one of the following gestures:
   - **Rock**: Make a fist with all fingers curled in.
   - **Paper**: Extend all fingers outward.
   - **Scissors**: Extend the index and middle fingers while curling the others.

3. The game will:
   - Detect each player’s gesture.
   - Display the gestures above the players' hands.
   - Announce the winner at the bottom of the screen.

4. Press **`q`** to exit the game.

---

## Demo
Imagine a sleek interface where:
- Player gestures appear dynamically overlaid above their hands.
- A glowing announcement displays the winner at the bottom of the screen.

---

## How It Works
1. **Hand Tracking**: Utilizes Mediapipe's hand tracking model to identify 21 hand landmarks.
2. **Gesture Classification**: Compares landmark positions to classify gestures into "Rock," "Paper," or "Scissors."
3. **Winner Determination**: Applies the classic rules:
   - Rock beats Scissors
   - Scissors beat Paper
   - Paper beats Rock
4. **Real-Time Feedback**: Renders gestures and results on the video feed using OpenCV.

---

## Troubleshooting
- **The game isn't detecting gestures properly**:
  - Ensure the camera feed is clear and well-lit.
  - Place your hand fully in the respective half of the frame.
  
- **Low FPS or performance issues**:
  - Use a lower resolution for the camera feed in the `cv2.VideoCapture` line.

---

## Future Enhancements
- Add gesture customization to support unique hand signals.
- Incorporate sound effects for an engaging experience.
- Provide an option to play against an AI opponent.

---

Readme made with the assistance of AI
