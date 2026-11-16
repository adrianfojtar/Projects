import board
import adafruit_vl53l0x
import math
import time
from mpu6050 import mpu6050

movement_sensor = mpu6050(0x68)
i2c = board.I2C()
distance_sensor = adafruit_vl53l0x.VL53L0X(i2c)
movement_limit = 12.0

while True:
    acceleration = movement_sensor.get_accel_data()
    magnitude = math.sqrt(
        acceleration["x"] ** 2
        + acceleration["y"] ** 2
        + acceleration["z"] ** 2
    )
    distance = distance_sensor.range

    if magnitude > movement_limit and distance < 300:
        print("ALARM")
    else:
        print("OK")

    time.sleep(0.1)