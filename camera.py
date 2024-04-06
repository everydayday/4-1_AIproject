import cv2
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils

drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
capture = cv2.VideoCapture(0)
with mp_face_mesh.FaceMesh(
        max_num_faces = 1,
        refine_landmarks = True,
        min_detection_confidence = 0.5,
        min_tracking_confidence = 0.5) as face_mesh :
    while cv2.waitKey(33) != ord('q') :
        ret, frame = capture.read()
        cv2.imshow("VideoFrame", cv2.flip(frame,1))
    
capture.release()
cv2.destroyAllWindows()