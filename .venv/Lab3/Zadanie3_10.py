from gpiozero import AngularServo, LED
from time import sleep

servo = AngularServo(24, min_angle=-90, max_angle=90)
led = LED(23)

while True:
    servo.angle = -90
    led.on()
    sleep(1)
    led.off()
    sleep(1)

    servo.angle = 90
    led.on()
    sleep(0.2)
    led.off()
    sleep(0.2)