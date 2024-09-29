import RPi.GPIO as GPIO
import time

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the pins for the ultrasonic sensors
TRIGGER_PIN_FRONT = 18
ECHO_PIN_FRONT = 24
TRIGGER_PIN_LEFT = 23
ECHO_PIN_LEFT = 25
TRIGGER_PIN_RIGHT = 12
ECHO_PIN_RIGHT = 16

# Define the pins for the DC motors
MOTOR_LEFT = 20
MOTOR_RIGHT = 21

# Set up the trigger pins as outputs and the echo pins as inputs
GPIO.setup(TRIGGER_PIN_FRONT, GPIO.OUT)
GPIO.setup(ECHO_PIN_FRONT, GPIO.IN)
GPIO.setup(TRIGGER_PIN_LEFT, GPIO.OUT)
GPIO.setup(ECHO_PIN_LEFT, GPIO.IN)
GPIO.setup(TRIGGER_PIN_RIGHT, GPIO.OUT)
GPIO.setup(ECHO_PIN_RIGHT, GPIO.IN)

# Set up the motor pins as outputs
GPIO.setup(MOTOR_LEFT, GPIO.OUT)
GPIO.setup(MOTOR_RIGHT, GPIO.OUT)

def get_distance_front():
    # Send a pulse to the trigger pin to initiate the measurement
    GPIO.output(TRIGGER_PIN_FRONT, GPIO.HIGH)
    time.sleep(0.01)
    GPIO.output(TRIGGER_PIN_FRONT, GPIO.LOW)

    # Measure the time it takes for the echo to return
    start_time = time.time()
    while GPIO.input(ECHO_PIN_FRONT) == 0:
        start_time = time.time()
    while GPIO.input(ECHO_PIN_FRONT) == 1:
        end_time = time.time()

    # Calculate the distance based on the speed of sound (approximately 343 m/s)
    distance = (end_time - start_time) * 34300 / 2
    return distance

def get_distance_left():
    # Send a pulse to the trigger pin to initiate the measurement
    GPIO.output(TRIGGER_PIN_LEFT, GPIO.HIGH)
    time.sleep(0.01)
    GPIO.output(TRIGGER_PIN_LEFT, GPIO.LOW)

    # Measure the time it takes for the echo to return
    start_time = time.time()
    while GPIO.input(ECHO_PIN_LEFT) == 0:
        start_time = time.time()
    while GPIO.input(ECHO_PIN_LEFT) == 1:
        end_time = time.time()

    # Calculate the distance based on the speed of sound (approximately 343 m/s)
    distance = (end_time - start_time) * 34300 / 2
    return distance

def get_distance_right():
    # Send a pulse to the trigger pin to initiate the measurement
    GPIO.output(TRIGGER_PIN_RIGHT, GPIO.HIGH)
    time.sleep(0.01)
    GPIO.output(TRIGGER_PIN_RIGHT, GPIO.LOW)

    # Measure the time it takes for the echo to return
    start_time = time.time()
    while GPIO.input(ECHO_PIN_RIGHT) == 0:
        start_time = time.time()
    while GPIO.input(ECHO_PIN_RIGHT) == 1:
        end_time = time.time()

    # Calculate the distance based on the speed of sound (approximately 343 m/s)
    distance = (end_time - start_time) * 34300 / 2
    return distance

def move_forward():
    GPIO.output(MOTOR_LEFT, GPIO.HIGH)
    GPIO.output(MOTOR_RIGHT, GPIO.HIGH)

def move_backward():
    GPIO.output(MOTOR_LEFT, GPIO.LOW)
    GPIO.output(MOTOR_RIGHT, GPIO.LOW)

def stop():
    GPIO.output(MOTOR_LEFT, GPIO.LOW)
    GPIO.output(MOTOR_RIGHT, GPIO.LOW)

try:
    while True:
        distance_front = get_distance_front()
        distance_left = get_distance_left()
        distance_right = get_distance_right()

        print("Distance Front: {:.2f} cm".format(distance_front))
        print("Distance Left: {:.2f} cm".format(distance_left))
        print("Distance Right: {:.2f} cm".format(distance_right))

        # Simple obstacle avoidance logic
        if distance_front < 20:
            stop()
            move_backward()
            time.sleep(0.5)
        elif distance_left < 20:
            stop()
            move_backward()
            time.sleep(0.5)
        elif distance_right < 20:
            stop()
            move_backward()
            time.sleep(0.5)
        else:
            move_forward()

except KeyboardInterrupt:
    GPIO.cleanup()