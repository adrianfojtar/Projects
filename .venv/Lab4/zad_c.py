from mpu6050 import mpu6050
import time

sensor = mpu6050(0x68)
max_gyro = {"x": 0.0, "y": 0.0, "z": 0.0}
end_time = time.monotonic() + 10

while time.monotonic() < end_time:
    gyro = sensor.get_gyro_data()
    for axis in max_gyro:
        max_gyro[axis] = max(max_gyro[axis], abs(gyro[axis]))
    time.sleep(0.1)

print("Maksymalna prędkość obrotowa:")
print(f"X: {max_gyro['x']:.1f} deg/s")
print(f"Y: {max_gyro['y']:.1f} deg/s")
print(f"Z: {max_gyro['z']:.1f} deg/s")