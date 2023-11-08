# Import necessary libraries and modules
import board
import digitalio
import time

# Define a dictionary that maps characters to Morse code representations
MORSE_CODE = { 'A':'.-', 'B':'-...',       
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-', ' ':'/'}    

# Identify the pin on the board that will power the LED
R = digitalio.DigitalInOut(board.GP17)
R.direction = digitalio.Direction.OUTPUT

# Define time durations for Morse code elements
modifier = 0.25
dot_time = 1 * modifier
dash_time = 3 * modifier
between_taps = 1 * modifier
between_letters = 3 * modifier
between_words = 7 * modifier

# Prompt the user to enter a message or type "-q" to quit
print("Enter a message to be translated into Morse Code or type '-q' to quit:")
string = ""   # Initialize an empty string to store the Morse code representation

while True:
    message = input()  # Get input from the user
    if message == "-q":  # Check if the user wants to quit
        break  # Exit the loop if the user wants to quit

    # Iterate through each letter in the input message, converting it to Morse code
    for letter in message.upper():  # Convert the letter to uppercase
        string += MORSE_CODE[letter]  # Append the Morse code representation to the string
        string += " "  # Add a space between Morse code letters

    print(string)  # Print the Morse code representation of the input message

    for character in string:  # Iterate through the Morse code representation
        if character == ".":  # If it's a dot
            R.value = True  # Turn on the LED
            time.sleep(dot_time)  # Keep the LED on for dot_time
            R.value = False  # Turn off the LED
            time.sleep(between_taps)  # Wait for the gap between taps
        elif character == "-":  # If it's a dash
            R.value = True  # Turn on the LED
            time.sleep(dash_time)  # Keep the LED on for dash_time
            R.value = False  # Turn off the LED
            time.sleep(modifier)  # Wait for the gap between taps
        elif character == " ":  # If it's a space (between letters)
            time.sleep(between_letters)  # Wait for the gap between letters
        elif character == " / ":  # If it's a space (between words)
            time.sleep(between_words)  # Wait for the gap between words
