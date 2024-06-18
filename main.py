import cv2 as cv
import pyautogui as pg                          
import mediapipe as mp
cam=cv.VideoCapture(0)
face_mesh=mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
while True:
    _,frame=cam.read()
    frame=cv.flip(frame,1)
    rgb_frame=cv.cvtColor(frame,cv.COLOR_BGR2RGB)
    output=face_mesh.process(rgb_frame)
    landmark_points=output.multi_face_landmarks
    frame_h,frame_w,_=frame.shape                
    # print(landmark_points)
    if landmark_points:
        landmarks=landmark_points[0].landmark              
        for landmark in landmarks[474:478]:
            x=int(landmark.x*frame_w)
            y=int(landmark.y*frame_h)
            # print(x,y)
            cv.circle(frame,(x,y),3,(0,255,0))

            # print(x,y)
                         
        left=[landmarks[145],landmarks[159]]
        for landmark in left:
            x = int(landmark.x * frame_w)  
            y = int(landmark.y * frame_h)
            # print(x, y) 
            cv.circle(frame, (x, y), 3, (0,0 , 255))

        print(left[0].y,left[1].y)
        if left[0].y-left[1].y<0.007:
            print("click")
            pg.press('space')

    cv.imshow("Automated Dyno Game",frame)

    cv.waitKey(1)
  