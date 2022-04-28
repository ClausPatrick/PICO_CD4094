from machine import Pin, Timer, I2C
import CD4094_display

led_onboard = machine.Pin(25, machine.Pin.OUT)
led_onboard.value(1)
cd = CD4094_display.CD4094()
led_onboard.value(0)

counter = 0
while True:
    led_onboard.value(0)
    cd.write(counter, red=1, pwm_duty = (0xffff//((counter % 100 + 1))))
    led_onboard.value(1)
    counter = (counter + 1) % 9999
