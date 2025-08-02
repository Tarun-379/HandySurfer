# HandySurfer
Control Subway surfer just using your right hand gestures, code made using python openCV, mediapipe, time, pyautogui liberaries.




🖐️ HandySurfer – Gesture Controlled Actions Using Hand Tracking
Control your keyboard with hand gestures using MediaPipe, OpenCV, and PyAutoGUI. HandySurfer lets you perform actions like Jump, Roll, and Swipe Left/Right using real-time hand gestures.


✨ Features
🖐️ Real-time hand and finger detection using MediaPipe

🎮 Map gestures to keyboard keys:
0 fingers: Press Down (ROLL)
4 or more fingers: Press Up (JUMP)
Right/Left wrist swipe: Press Right / Left arrow keys

⚡ Smooth gesture-to-keyboard response
⏱️ Built-in swipe cooldown to prevent spamming

🛠️ Requirements
Install these dependencies before running the project:
pip install opencv-python mediapipe pyautogui

🚀 How to Run
python gesture_control.py
Make sure your webcam is connected and working. Press ESC or Q to exit the program.

🧠 How It Works
Hand Tracking: Uses MediaPipe to detect landmarks of the hand in real-time.

Gesture Detection:
Counts how many fingers are up.
Detects horizontal wrist movement for swipe gestures.
Keyboard Control: pyautogui simulates key presses based on the gesture.

📁 File Structure
📁 HandySurfer/
│
├── gesture_control.py    # Main script
└── README.md             # Project documentation

⚠️ Notes
Thumb detection may be inaccurate for left-handed users or if the palm orientation changes quickly.
May not work well in low-light or with fast hand movements.
For swipe detection, keep wrist visible and swipe smoothly across the screen.

📌 To Do
 Improve thumb classification using hand label
 Add more gestures like pause/reset
 Add sound feedback
 Display FPS and hand labels

 
🧑‍💻 Author
Tarun – GitHub

Feel free to fork, contribute, or open an issue!


📜 License
This project is open source and available under the MIT License.
