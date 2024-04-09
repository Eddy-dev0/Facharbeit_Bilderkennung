import cv2
from simple_facerec import SimpleFacerec

sfr = SimpleFacerec()
sfr.load_encoding_images("Images/")
cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()
    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        top, left, bottom, right = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
        cv2.putText(frame, name, (right, top - 10), cv2.FONT_HERSHEY_PLAIN, 1, (100, 89, 0), 2)
        cv2.rectangle(frame, (left, top), (right, bottom), (99, 120, 200), 2)
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()