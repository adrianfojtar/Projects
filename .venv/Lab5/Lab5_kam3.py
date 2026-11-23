from picamera2 import Picamera2, Preview 
from picamera2.encoders import H264Encoder 
from time import sleep 
picam2 = Picamera2() 
config = picam2.create_video_configuration( 
main={"size": (1280, 720)} 
) 
picam2.configure(config) 
# Podgląd obrazu 
picam2.start_preview(Preview.QTGL) 
# Encoder H.264 
encoder = H264Encoder(bitrate=10_000_000) 
# Rozpoczęcie nagrywania 
picam2.start_recording(encoder, "film.h264") 
sleep(10) 
# Zakończenie nagrywania 
picam2.stop_recording() 
picam2.stop_preview() 
print("Nagrywanie zakończone.")