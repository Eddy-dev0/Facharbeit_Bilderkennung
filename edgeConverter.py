import cv2
import matplotlib.pyplot as plt

# Bild laden (ersetze 'dein_bild.jpg' durch den Dateipfad deines Bildes)
image = cv2.imread("", cv2.IMREAD_GRAYSCALE)

# Kantenerkennung mit dem Canny-Algorithmus
edges = cv2.Canny(image, 50, 150)

# Originalbild und Kantenerkennung nebeneinander anzeigen
plt.subplot(1, 2, 1), plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), cmap='gray')
plt.title('Originalbild'), plt.xticks([]), plt.yticks([])

plt.subplot(1, 2, 2), plt.imshow(edges, cmap='gray')
plt.title('Kantenerkennung'), plt.xticks([]), plt.yticks([])

plt.show()
