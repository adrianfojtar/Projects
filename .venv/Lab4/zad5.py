import board 
import adafruit_vl53l0x 
import time 
i2c = board.I2C() 
sensor = adafruit_vl53l0x.VL53L0X(i2c) 
while True:      
    distance = sensor.range 
    if distance < 100: 
        print("UWAGA - obiekt bardzo blisko!") 
    elif distance < 300: 
        print("Obiekt blisko") 
    else: 
        print("Brak obiektu w poblizu") 
    time.sleep(0.2)