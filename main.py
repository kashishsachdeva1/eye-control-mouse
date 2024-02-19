import cv2 #its in the package opencv-contibute-python
import mediapipe as mp #mediapipe could be given with the short name that is mp
import pyautogui

# pyautogui.FAILSAFE = False


cam = cv2.VideoCapture(0)#thus capturing the vedio over here
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks = True)#for detecting the eye
screen_w,screen_h = pyautogui.size()
while True : # loop is running so as we could get the vedio capturing going on until the frame is their
    _, frame = cam.read() #on right side we are telling cv2 to read what ever is comming
    frame = cv2.flip(frame,1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmarks_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape
    if landmarks_points:
        landmarks = landmarks_points[0].landmark
        for id, landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame,(x,y), 3,(0,255,0))
            if id == 1:
                screen_x = int(landmark.x *screen_w)
                screen_y = int(landmark.y * screen_h)
                pyautogui.moveTo(screen_x,screen_y)
        left = [landmarks[145],landmarks[159]]
        for landmark in left:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))
        if(left[0].y - left[1].y) < 0.002:
            pyautogui.click()
            pyautogui.sleep(1)
    cv2.imshow('Eye Controlled Mouse',frame)
    cv2.waitKey(1) # wait untill the key is press and that for only 1

