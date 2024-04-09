import cv2
# Lade den vortrainierten Gesichtserkennungsklassifikator
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cam = cv2.VideoCapture(0)
while True:
    _, image = cam.read()
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_edges = cv2.Canny(image_gray, 30, 100)

    # Erkenne Gesichter im Bild
    faces = face_cascade.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=5)

    # Zeichne Rechtecke um erkannte Gesichter
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 3)

    cv2.imshow("LiveVideo", image)
    cv2.imshow("Converted", image_edges)

    if cv2.waitKey(1) == ord('q'):#"q" um die Fenster zu schließen, da sonst immer neu drauf zu gegriffen wird
        break

cam.release()
cv2.destroyAllWindows()
