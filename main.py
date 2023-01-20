# CLI Program that takes any string input and converts into Morse Code.

MORSE_DICT = {"A": "._", "B": "_...", "C": "_._.", "D": "_..", "E": ".", "F": ".._.", "G": "__.", "H": "....",
              "I": "..", "J": ".___", "K": "_._", "L": "._..", "M": "__", "N": "_.", "O": "___", "P": ".__.",
              "Q": "__._", "R": "._.", "S": "...", "T": "_", "U": ".._", "V": "..._", "W": ".__", "X": "_.._",
              "Y": "_.__", "Z": "__..", "1": ".____", "2": "..___", "3": "...__", "4": "...._", "5": ".....",
              "6": "_....", "7": "__...", "8": "___..", "9": "____.", "0": "_____", " ": "  "
              }

def morse_it(text):
    morse_phrase = ""
    for char in text.upper():
        if char in MORSE_DICT:
            morse_phrase += MORSE_DICT[char]
            morse_phrase += " "
    return morse_phrase


while True:
    phrase = input("Enter a phrase to switch to Morse Code or '/quit' to stop:")
    if phrase == "/quit":
        break
    print(morse_it(phrase))

