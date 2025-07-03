# camera.py
import cv2
import numpy as np
import mediapipe as mp
import csv
import os
import tensorflow as tf
#from tensorflow.keras.models import load_model
import PIL.Image
from PIL import Image

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5)

# Create CSV file
DATA_DIR = "static/hand_gesture_data"
os.makedirs(DATA_DIR, exist_ok=True)




class VideoCamera1(object):
    def __init__(self):
        
        # Open CSV file
        

        self.video = cv2.VideoCapture(0)
        #print(self.classNames)
        #self.video = cv2.VideoCapture(0)
        #self.k=1
        
    
    def __del__(self):
        self.video.release()
        
    
    def get_frame(self):
        _, frame = self.video.read()

        frame = cv2.flip(frame, 1)

        ff=open("static/label.txt","r")
        glabel=ff.read()
        ff.close()

        ff=open("static/label1.txt","r")
        gfile=ff.read()
        ff.close()
        
        GESTURE_LABEL = glabel  # Change for different gestures
        FILE_NAME = os.path.join(DATA_DIR, f"{gfile}")


        with open(FILE_NAME, mode="a", newline="") as f:
            writer = csv.writer(f)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            result = hands.process(rgb_frame)

            if result.multi_hand_landmarks:
                for hand_landmarks in result.multi_hand_landmarks:
                    mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                    # Extract hand landmark data
                    landmark_list = []
                    for lm in hand_landmarks.landmark:
                        landmark_list.extend([lm.x, lm.y, lm.z])

                    # Save to CSV
                    writer.writerow(landmark_list)

            cv2.putText(frame, f"Recording: {GESTURE_LABEL}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
            
        
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()
