from picamera2 import Picamera2, Preview 
from time import sleep 
# Utworzenie obiektu kamery 
picam2 = Picamera2() 
# Konfiguracja aparatu 
config = picam2.create_still_configuration() 
picam2.configure(config) 
# Uruchomienie podglądu 
picam2.start_preview(Preview.QTGL) 
picam2.start() 
print("Przygotowanie kamery...") 
sleep(3) 
# Wykonanie zdjęcia 
picam2.capture_file("zdjecie.jpg") 
print("Zdjęcie zapisane jako: zdjecie.jpg") 
# Jeszcze chwilę pokazujemy podgląd 
sleep(2) 
# Zatrzymanie kamery 
picam2.stop() 
picam2.stop_preview()