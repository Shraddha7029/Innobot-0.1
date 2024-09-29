import time
import RPi.GPIO as GPIO
import pygame
import speech_recognition as sr

# Initialize pygame for audio playback
pygame.init()

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the LED pins
led_pins = [17, 23, 24, 25, 5, 6, 12, 13, 16, 19, 20, 21, 26, 18, 15, 14, 7, 8, 9, 10, 11, 22, 27, 28, 3, 2, 4]

# Define the alphabet
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Define the audio files for each letter
audio_files = ['a.wav', 'b.wav', 'c.wav', 'd.wav', 'e.wav', 'f.wav', 'g.wav', 'h.wav', 'i.wav', 'j.wav', 'k.wav', 'l.wav', 'm.wav', 'n.wav', 'o.wav', 'p.wav', 'q.wav', 'r.wav', 's.wav', 't.wav', 'u.wav', 'v.wav', 'w.wav', 'x.wav', 'y.wav', 'z.wav']

# Set up the LEDs as outputs
for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT)

# Create a speech recognition object
r = sr.Recognizer()

# Loop through the alphabet
for i in range(len(alphabet)):
    # Play the audio file for the current letter
    pygame.mixer.music.load(audio_files[i])
    pygame.mixer.music.play()
    time.sleep(1)  # wait for 1 second

    # Listen for a response from the user
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    # Try to recognize the response
    try:
        response = r.recognize_google(audio)
        print("You said: " + response)
    except sr.UnknownValueError:
        print("Sorry, I didn't understand what you said.")
        continue

    # Check if the response matches the current letter
    while response.upper() != alphabet[i]:
        print("Incorrect! Try again.")
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)
        try:
            response = r.recognize_google(audio)
            print("You said: " + response)
        except sr.UnknownValueError:
            print("Sorry, I didn't understand what you said.")
            continue

    # Turn on the corresponding LED
    GPIO.output(led_pins[i], GPIO.HIGH)
    print("Correct!")
    time.sleep(1)  # wait for 1 second
    # Turn off the LED
    GPIO.output(led_pins[i], GPIO.LOW)
    time.sleep(0.5)  # wait for 0.5 seconds

# Clean up
GPIO.cleanup()
pygame.quit()