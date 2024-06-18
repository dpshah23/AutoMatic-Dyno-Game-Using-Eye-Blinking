import cv2 as cv
import pyautogui as pg
import mediapipe as mp

# Initialize webcam and FaceMesh
cam = cv.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)

while True:
    _, frame = cam.read()
    frame = cv.flip(frame, 1)  # Flip frame for mirror view
    rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)  # Convert to RGB
    output = face_mesh.process(rgb_frame)  # Process the frame to detect face landmarks
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape                
    
    if landmark_points:
        landmarks = landmark_points[0].landmark
        # Draw circles on landmarks 474 to 478
        for landmark in landmarks[474:478]:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv.circle(frame, (x, y), 3, (0, 255, 0))
                         
        # Draw circles on eye landmarks 145 and 159
        left = [landmarks[145], landmarks[159]]
        for landmark in left:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv.circle(frame, (x, y), 3, (0, 0, 255))

        # Check if eye landmarks are close enough to indicate a blink
        if left[0].y - left[1].y < 0.007:
            pg.press('space')  # Simulate spacebar press

    cv.imshow("Automated Dyno Game", frame)
    cv.waitKey(1)  # Display frame for 1ms
