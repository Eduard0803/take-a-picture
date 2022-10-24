import cv2      #Biblioteca usada para controlar a WebCam

webcam = cv2.VideoCapture(0)    #Faz a Captura da foto

while (True):
    validacao, frame = webcam.read()
    cv2.imshow("img1", frame)
    break
cv2.imwrite("Foto_teste.png", frame)    #Salva a foto no arquivo "Foto_teste.png"
cv2.destroyAllWindows()

webcam.release()
