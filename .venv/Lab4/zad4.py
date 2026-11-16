import board 
import adafruit_vl53l0x 
import time 
i2c = board.I2C() 
sensor = adafruit_vl53l0x.VL53L0X(i2c) 
while True: 
    distance = sensor.range 
    print("Odleglosc:", distance, "mm") 
    time.sleep(0.2) 