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
