import board 
import adafruit_vl53l0x 
import time 
i2c = board.I2C() 
sensor = adafruit_vl53l0x.VL53L0X(i2c) 
while True:
    distance = sensor.range 
    if distance > 300:
        print("BEZPIECZNIE")
    elif distance < 300:
        print("ALARM")
    else:
        print("GRANICA: 300 mm")
    time.sleep(0.2)