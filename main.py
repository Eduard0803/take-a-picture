import cv2

webcam = cv2.VideoCapture(0)

while (True):
    validacao, frame = webcam.read()
    cv2.imshow("img1", frame)
    break
cv2.imwrite("Foto_teste.png", frame)
cv2.destroyAllWindows()

webcam.release()
