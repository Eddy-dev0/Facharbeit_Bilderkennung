import pyautogui
import time

# Funktion zur kontinuierlichen Anzeige der Mauskoordinaten
def show_mouse_coordinates():
    while True:
        print("Aktuelle Mauskoordinaten:", pyautogui.position())
        time.sleep(1)  # Warte 1 Sekunde vor der nächsten Anzeige

# Rufe die Funktion zum Anzeigen der Mauskoordinaten auf
if __name__ == "__main__":
    show_mouse_coordinates()