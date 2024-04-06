import cv2

# 웹캠으로부터 비디오 캡처
cap = cv2.VideoCapture(0)

# 비디오 캡처 시작
while True:
    # 비디오 프레임 읽기
    ret, frame = cap.read()

    # 프레임 내 특정 범위의 픽셀 RGB값 변경
    for y in range(100, 110):
        for x in range(100, 110):
            frame[y, x] = (0, 0, 255)  # (B, G, R) 값 변경

    # 결과 출력
    cv2.imshow('result', frame)

    # 'q' 키를 누르면 비디오 캡처 종료
    if cv2.waitKey(1) == ord('q'):
        break

# 비디오 캡처 해제
cap.release()
cv2.destroyAllWindows()
