import cv2
import mediapipe as mp

# Face Mesh 모델 로드
face_mesh = mp.solutions.face_mesh.FaceMesh()
mp_drawing = mp.solutions.drawing_utils
# 비디오 캡처 객체 생성
cap = cv2.VideoCapture(0)

while True:
    # 프레임 단위로 읽기
    success, image = cap.read()
    if not success:
        break
    
    # 이미지를 RGB로 변환하여 face mesh 적용
    results = face_mesh.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # 얼굴 랜드마크 추출
    face_landmarks = results.multi_face_landmarks

    # 얼굴 랜드마크를 이용해 안경 부분을 덮어씌움
    if face_landmarks is not None:
        for face_lm in face_landmarks:
            for idx, lm in enumerate(face_lm.landmark):
                if idx == 234 or idx == 454:  # 오른쪽/왼쪽 눈 삼각형 중앙 지점
                    x, y = int(lm.x * image.shape[1]), int(lm.y * image.shape[0])
                    cv2.circle(image, (x, y), 10, (0, 255, 0), -1)
    
            # 얼굴 랜드마크를 연결하여 선으로 그리기
            mp_drawing.draw_landmarks(image, face_lm, mp.solutions.face_mesh.FaceMesh.FACEMESH_CONTOURS,
                                      mp_drawing.DrawingSpec(color=(0,0,255), thickness=1, circle_radius=1),
                                      mp_drawing.DrawingSpec(color=(0,255,0), thickness=1, circle_radius=1))
    
    # 화면에 보여주기
    cv2.imshow('Face Mesh', image)
    
    # q키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 객체 해제
cap.release()
cv2.destroyAllWindows()
