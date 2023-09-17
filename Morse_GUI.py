import RPi.GPIO as GPIO
import time
import tkinter as tk

ledPin = 17

morseCode = ".... .. - . ... ...."
dotDuration = 0.35  # in seconds

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)  # Define ledPin as an output pin

def blinkMorseCode():
    for char in morseCode:
        GPIO.output(ledPin, GPIO.HIGH)
        if char == '.':
            time.sleep(dotDuration)
        elif char == '-':
            time.sleep(dotDuration * 3)  # dash duration
        GPIO.output(ledPin, GPIO.LOW)
        time.sleep(dotDuration)
        time.sleep(dotDuration)  # gap between symbols
    time.sleep(dotDuration * 3)  # gap between words

def start_blink():
    blinkMorseCode()

def cleanup_gpio():
    GPIO.cleanup()
    root.destroy()

root = tk.Tk()
root.title("Morse Code Blinker")

start_button = tk.Button(root, text="Start Blink", command=start_blink)
start_button.pack()

exit_button = tk.Button(root, text="Exit", command=cleanup_gpio)
exit_button.pack()

try:
    root.mainloop()
except KeyboardInterrupt:
    cleanup_gpio()
