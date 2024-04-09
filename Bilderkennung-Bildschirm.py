import pyautogui
import time
import keyboard

# Zeitintervall für das Scannen des Bildschirms und Klicken auf die Fliesen
scan_interval = 0.0000000000000000000000000000000000000000000000000000000000000000000001

# Koordinaten der Fliesen
tile_1_x, tile_1_y = 2492, 324
tile_2_x, tile_2_y = 2729, 324
tile_3_x, tile_3_y = 2997, 324
tile_4_x, tile_4_y = 3258, 324
target_color = (0,0,0)
# Funktion zum Bestimmen der schwarzen Fliese
def find_black_tile():
    tile_coordinates = [
        (tile_1_x, tile_1_y),
        (tile_2_x, tile_2_y),
        (tile_3_x, tile_3_y),
        (tile_4_x, tile_4_y)
    ]
    while True:
        for tile_x, tile_y in tile_coordinates:
            color = pyautogui.pixel(tile_x, tile_y)  # Überprüfe die Farbe der Fliese
            if color == target_color:  # Prüfe, ob die Fliese schwarz ist
                return tile_x, tile_y  # Wenn schwarz, gib die Position der Fliese zurück
        #time.sleep(scan_interval)
        tile_x, tile_y = find_black_tile()
        pyautogui.click(tile_x, tile_y)
        pyautogui.mouseDown(button='left')


# Rufe die Hauptfunktion auf
if __name__ == "__main__":
    time.sleep(1)  # Warte ein paar Sekunden, bevor das Klicken beginnt (um Zeit zu haben, das Spiel zu öffnen)
    find_black_tile()
