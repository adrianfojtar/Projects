import board 
import adafruit_vl53l0x 
import time 
i2c = board.I2C() 
sensor = adafruit_vl53l0x.VL53L0X(i2c) 
while True:
    distance = sensor.range 
    if distance > 500:
        print("DALeko")
    elif distance >= 200:
        print("BLISKO")
    else:
        print("ALARM")
    time.sleep(0.2)