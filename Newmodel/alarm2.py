import cv2
import numpy as np
import dlib
import pygame
import threading
import tkinter as tk
from imutils import face_utils

# Initialize pygame for alarm system
pygame.mixer.init()
pygame.mixer.music.load("alarm_sound.mp3")

# Global variables
alarm_active = False
root = None  # Reference for Tkinter window

# Function to play alarm
def play_alarm():
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.play(-1)  # Play alarm in loop

# Function to stop alarm
def stop_alarm():
    global alarm_active, root
    alarm_active = False
    pygame.mixer.music.stop()
    if root:
        root.destroy()  # Close the Tkinter window

# Function to show stop button in separate thread
def show_stop_button():
    global root
    root = tk.Tk()
    root.title("Alarm")
    root.geometry("200x100")
    
    label = tk.Label(root, text="ALARM RINGING!", font=("Arial", 12, "bold"), fg="red")
    label.pack(pady=10)
    
    stop_button = tk.Button(root, text="STOP ALARM", command=stop_alarm, bg="red", fg="white", font=("Arial", 12))
    stop_button.pack(pady=5)
    
    root.mainloop()

# Initialize camera
cap = cv2.VideoCapture(0)

# Load face detector & landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Drowsiness detection variables
drowsy_count = 0
sleep_count = 0
active_count = 0
status = ""
color = (0, 0, 0)

# Function to compute Euclidean distance
def compute(ptA, ptB):
    return np.linalg.norm(ptA - ptB)

# Function to calculate Eye Aspect Ratio (EAR)
def eye_aspect_ratio(eye):
    A = compute(eye[1], eye[5])
    B = compute(eye[2], eye[4])
    C = compute(eye[0], eye[3])
    return (A + B) / (2.0 * C)

# Function to calculate Mouth Aspect Ratio (MAR)
def mouth_aspect_ratio(mouth):
    A = compute(mouth[3], mouth[9])
    B = compute(mouth[2], mouth[10])
    C = compute(mouth[4], mouth[8])
    D = compute(mouth[0], mouth[6])
    return (A + B + C) / (3.0 * D)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    
    # Create a copy of the frame for landmarks window
    landmark_frame = frame.copy()

    for face in faces:
        landmarks = predictor(gray, face)
        landmarks = face_utils.shape_to_np(landmarks)
        
        # Get Eye & Mouth landmarks
        left_eye = landmarks[36:42]
        right_eye = landmarks[42:48]
        mouth = landmarks[48:68]

        # Calculate EAR and MAR
        ear = (eye_aspect_ratio(left_eye) + eye_aspect_ratio(right_eye)) / 2.0
        mar = mouth_aspect_ratio(mouth)

        # Define thresholds
        EAR_THRESHOLD = 0.22  # Lower threshold means eyes more closed
        MAR_THRESHOLD = 0.6  # High MAR means mouth open (yawning)
        DROWSY_TIME = 10  # Frames to detect drowsiness before alarm
        SLEEP_TIME = 5  # Frames to detect sleep before alarm

        # Detect status
        if ear < EAR_THRESHOLD and mar < MAR_THRESHOLD:
            sleep_count += 1
            drowsy_count = 0
            active_count = 0
            if sleep_count > SLEEP_TIME:
                status = "SLEEPING !!!"
                color = (255, 0, 0)
                if not alarm_active:
                    alarm_active = True
                    threading.Thread(target=play_alarm, daemon=True).start()
                    threading.Thread(target=show_stop_button, daemon=True).start()

        elif EAR_THRESHOLD < ear < 0.26:  # Eyes not fully open
            drowsy_count += 1
            sleep_count = 0
            active_count = 0
            if drowsy_count > DROWSY_TIME:
                status = "Drowsy !"
                color = (0, 0, 255)
                if not alarm_active:
                    alarm_active = True
                    threading.Thread(target=play_alarm, daemon=True).start()
                    threading.Thread(target=show_stop_button, daemon=True).start()
        
        elif mar > MAR_THRESHOLD:  # Detect yawning
            status = "Yawning !"
            color = (0, 165, 255)
            sleep_count = 0
            drowsy_count = 0
            active_count = 0

        else:  # Awake state
            active_count += 1
            sleep_count = 0
            drowsy_count = 0
            status = "Active :)"
            color = (0, 255, 0)
            alarm_active = False  # Stop alarm when awake
            pygame.mixer.music.stop()

        # Display status
        cv2.putText(frame, status, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 3)

        # Draw landmarks on landmark window
        for (x, y) in landmarks:
            cv2.circle(landmark_frame, (x, y), 1, (255, 255, 255), -1)

    # Show both windows
    cv2.imshow("Drowsiness Detection", frame)  # Status Window
    cv2.imshow("Landmark Detection", landmark_frame)  # Landmarks Window
    
    key = cv2.waitKey(1)
    if key == 27:  # ESC key to exit
        break

# Release resources on exit
cap.release()
cv2.destroyAllWindows()
pygame.mixer.quit()
