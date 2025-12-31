
import Jetson.GPIO as GPIO
import time

led_pin = 7

# Use physical board pin numbering
GPIO.setmode(GPIO.BOARD)

# Set pin as output and initialize LOW
GPIO.setup(led_pin, GPIO.OUT, initial=GPIO.LOW)

try:
    while True:
        GPIO.output(led_pin, GPIO.HIGH)
        time.sleep(0.5)   # LED ON for 0.5 sec

        GPIO.output(led_pin, GPIO.LOW)
        time.sleep(0.5)   # LED OFF for 0.5 sec

except KeyboardInterrupt:
    print("Exiting gracefully")
finally:
    GPIO.cleanup()



