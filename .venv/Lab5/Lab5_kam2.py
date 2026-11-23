from picamera2 import Picamera2, Preview 
picam2 = Picamera2() 
config = picam2.create_preview_configuration( 
main={"size": (640, 480)} 
) 
picam2.configure(config) 
picam2.start_preview(Preview.QTGL) 
picam2.start() 
input("Naciśnij ENTER, aby zakończyć...\n") 
picam2.stop() 
picam2.stop_preview() 