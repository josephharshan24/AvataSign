# camera.py
import joblib
import cv2
import numpy as np
import mediapipe as mp
#import tensorflow as tf
#from tensorflow.keras.models import load_model
import PIL.Image
from PIL import Image

# Load model and gesture map
model = joblib.load("gesture_model.pkl")
gesture_map = joblib.load("gesture_map.pkl")

# Get expected number of features
expected_features = model.n_features_in_

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5)


class VideoCamera(object):
    def __init__(self):
        
        
        #print(self.classNames)
        self.video = cv2.VideoCapture(0)
        self.k=1
        
    
    def __del__(self):
        self.video.release()
        
    
    def get_frame(self):
        ret, frame = self.video.read()

        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb_frame)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Extract features
                landmark_list = []
                for lm in hand_landmarks.landmark:
                    landmark_list.extend([lm.x, lm.y, lm.z])
                
                # Predict only if feature size matches
                if len(landmark_list) == expected_features:
                    prediction = model.predict([landmark_list])[0]
                    gesture_name = gesture_map.get(prediction, "Unknown")

                    gn=""
                    ff=open("static/class2.txt","r")
                    cn=ff.read()
                    ff.close()
                    cna=cn.split("|")

                    ff=open("static/class1.txt","r")
                    hn=ff.read()
                    ff.close()
                    hna=hn.split("|")
                    u=0
                    for cna1 in cna:
                        if cna1==gesture_name:
                            gn=hna[u]
                            break
                        u+=1
                    if gn=="":
                        s=1
                    else:
                        ff=open("static/detect.txt","w")
                        ff.write(gn)
                        ff.close()
                        print(gn)

                        cv2.putText(frame, f"{gn}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
                else:
                    ff=open("static/detect.txt","w")
                    ff.write("")
                    ff.close()
                        

        '''framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Get hand landmark prediction
        result = self.hands.process(framergb)

        # print(result)
        
        className = ''
        # post process the result
        if result.multi_hand_landmarks:
            landmarks = []
            for handslms in result.multi_hand_landmarks:
                for lm in handslms.landmark:
                    # print(id, lm)
                    lmx = int(lm.x * x)
                    lmy = int(lm.y * y)

                    landmarks.append([lmx, lmy])

                # Drawing landmarks on frames
                self.mpDraw.draw_landmarks(frame, handslms, self.mpHands.HAND_CONNECTIONS)

                # Predict gesture
                prediction = self.model.predict([landmarks])
                # print(prediction)
                classID = np.argmax(prediction)
                className = self.classNames[classID]
                ff=open("static/msg.txt","w")
                ff.write(className)
                ff.close()

                print("class="+className)

        # show the prediction on the frame
        cv2.putText(frame, className, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 
                       1, (0,0,255), 2, cv2.LINE_AA)'''
        
        
        
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()
