#Webcam Dimensions: 640 x 480

import cv2
import mediapipe as mp 
import csv 
import numpy as np
import time 
import math 

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

log_count = -1

def calculations(image, landmarks):
    image_width, image_height = image.shape[1], image.shape[0]

    landmark_point = []
    data_point = []
    landmark_array = np.empty((0, 2), int)

    # Keypoint
    for _, landmark in enumerate(landmarks.landmark):
        x = float("{:.3f}".format(landmark.x))
        y = float("{:.3f}".format(landmark.y))
        landmark_x = min(int(landmark.x * image_width), image_width - 1)
        landmark_y = min(int(landmark.y * image_height), image_height - 1)
        #landmark_z = float("{:.3f}".format(landmark.z))

        data_point.append([x, y])

        landmark_point.append([landmark_x, landmark_y])
        landmark_array = np.append(landmark_array, landmark_point, axis=0)

    x, y, w, h = cv2.boundingRect(landmark_array)

    box_coords = [x, y, x + w, y + h]
    center_coords = [ int(x + w/2) , int(y + h/2)]

    area = float("{:.3f}".format(w * h / (307200)))
    #print(data_point[0][0])
    #print(data_point[12][0])
    distance_x = data_point[0][0] - data_point[12][0]
    distance_y = data_point[0][1] - data_point[12][1]
    distance = float("{:.3f}".format(math.sqrt(distance_x**2 + distance_y**2)))
    print(distance)
    #distance = data_point[]
    midpoint_x = float("{:.3f}".format((x + w/2) / 640))
    midpoint_y = float("{:.3f}".format((y + h/2) / 480))
            

    return area, distance, midpoint_x, midpoint_y, data_point, box_coords, center_coords

def logging_csv(area, distance, midpoint_x, midpoint_y, landmark_list):
   csv_path = 'ml/model/keypoint_classifier/keypoint3.csv'
   flat_landmark_list = list(np.concatenate(landmark_list).flat)
   with open(csv_path, 'a', newline="") as f:
        writer = csv.writer(f)
        writer.writerow([20, *flat_landmark_list, area, midpoint_x, midpoint_y, distance])
   return

# For webcam input:
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.8,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())

        area, distance, midpoint_x, midpoint_y, landmark_list, box_coords, center_coords = calculations(image, hand_landmarks)
        cv2.rectangle(image, (box_coords[0], box_coords[1]), (box_coords[2], box_coords[3]), (255,255,255), 1)
        cv2.putText(image, 'Fedex', (box_coords[0], box_coords[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
        cv2.circle(image, (center_coords[0], center_coords[1]), 5, (255,255,255), -1)

    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
    key = cv2.waitKey(10)

    if key == 27:  # ESC
        break
    if key == 108: # L 
        print("log")
        log_count = 100


    if log_count > 0: 
        logging_csv(area, distance, midpoint_x, midpoint_y, landmark_list)
        time.sleep(0.05)
        log_count = log_count - 1 
        if log_count == 1:
            print("log complete")

    #if cv2.waitKey(5) & 0xFF == 27:
    #  break


cap.release()