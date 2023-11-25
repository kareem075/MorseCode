###############################################################################################

MORSE_CODE_DICT = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
                  'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
                  'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
                  'y': '-.--', 'z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
                  '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ' ': ' '}

def encryption(text):
    morse_code = ''
    for words in text.lower():
        if words in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[words] + ' '
    return morse_code

def decryption(morse_code):
    morse_code = morse_code.split(' ')
    text = ''
    for code in morse_code:
        for key, value in MORSE_CODE_DICT.items():
            if code == value:
                text += key
    return text
    
def main():
    while True:
        user_input = input("Enter a sentence or Morse code (type 'exit' to end): ")

        if any(words.isalpha() for words in user_input):
            result = encryption(user_input)
            print("Morse code: ", result)
        else:
            result = decryption(user_input)
            print("Decription: ", result)

        if user_input.lower() == 'exit':
            break
if __name__ == "__main__":
    main()