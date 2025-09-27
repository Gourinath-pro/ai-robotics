from gpiozero import LED
from time import sleep

led = LED(17)

led1 = LED(27)
while True:
    for i in range(1,5):
        led.on()
        led1.on()
        sleep(1)
        led.off()
        led1.off()
        sleep(1)
        