# 출처 : https://jinho_study.tistory.com/231
import numpy as np
import cv2

haar_face= 'haarcascade_frontalface_default.xml' # 얼굴 검출
face_cascade = cv2.CascadeClassifier(haar_face) # Cascade 분류기를 생성

cam = cv2.VideoCapture(0)
cam.set(3,640) # 너비
cam.set(4,480) # 높이

# 3번에 사용할 이미지 불러오기
img = cv2.imread('IronMan.png', cv2.IMREAD_UNCHANGED) # 원본 사용

while True:
    ret, frame = cam.read()
    frame = cv2.flip(frame, 1)  # 좌우 반전
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # 얼굴 검출을 위해 회색조로 영상 로드
    faces = face_cascade.detectMultiScale(gray, 1.05, 5)

    if len(faces):
        for (x, y, w, h) in faces:
            face_img = frame[y:y + h, x:x + w] # 탐지된 얼굴 이미지를 크롭

            # 1. 얼굴 모자이크 시키기
            face_img = cv2.resize(face_img, dsize=(0, 0), fx=0.04, fy=0.04)  # 축소
            face_img = cv2.resize(face_img, (w, h), interpolation=cv2.INTER_AREA)  # 확대
            frame[y:y + h, x:x + w] = face_img

    cv2.imshow('result', frame)

    k = cv2.waitKey(30) & 0xff
    if k == 27: # ESC 누르면 종료
        break

cam.release()
cv2.destroyAllWindows()