from mpu6050 import mpu6050 
import math 
import time 
sensor = mpu6050(0x68)     
while True: 
    a = sensor.get_accel_data() 
    magnitude = math.sqrt(a["x"]**2 + a["y"]**2 + a["z"]**2) 
    print(f"Przyspieszenie: {magnitude:.2f}") 
    if magnitude > 12: 
        print("WYKRYTO RUCH!") 
    time.sleep(0.1)