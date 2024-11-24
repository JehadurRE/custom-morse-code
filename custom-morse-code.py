# Morse code dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
    '8': '---..', '9': '----.', '0': '-----', ',': '--..--', 
    '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', 
    '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', 
    ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '_': '..--.-', 
    '"': '.-..-.', '$': '...-..-', '!': '-.-.--', '@': '.--.-.', 
    ' ': '/'
}
# Reverse dictionary for decoding
REVERSE_MORSE_CODE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}

def customize_morse_code():
    """
    Customize the Morse code symbols for 'dot' and 'dash'.
    """
    dot = input("Enter your preferred symbol for 'dot': ").strip()
    dash = input("Enter your preferred symbol for 'dash': ").strip()
    return dot, dash

def translate_to_custom_morse(text, dot, dash):
    """
    Translate the given text into Morse code with customized symbols.
    """
    text = text.upper()
    morse_code = []
    for char in text:
        if char in MORSE_CODE_DICT:
            morse = MORSE_CODE_DICT[char]
            # Replace dot and dash with custom symbols
            custom_morse = morse.replace('.', dot).replace('-', dash)
            morse_code.append(custom_morse)
        else:
            morse_code.append('')  # For unsupported characters
    return ' '.join(morse_code)

def translate_from_custom_morse(custom_morse, dot, dash):
    """
    Translate custom Morse code back to plain text.
    """
    morse = custom_morse.replace(dot, '.').replace(dash, '-')
    words = morse.split(' / ')  # Morse words are separated by ' / '
    decoded_message = []
    
    for word in words:
        letters = word.split()  # Morse letters are separated by spaces
        decoded_word = ''.join(REVERSE_MORSE_CODE_DICT.get(letter, '') for letter in letters)
        decoded_message.append(decoded_word)
    
    return ' '.join(decoded_message)

def main():
    print("Welcome to the Custom Morse Code Translator!")
    dot, dash = customize_morse_code()
    print(f"Your custom Morse code will use '{dot}' for 'dot' and '{dash}' for 'dash'.")
    
    while True:
        print("\nOptions:")
        print("1. Translate text to custom Morse code")
        print("2. Translate custom Morse code to text")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            text = input("Enter the text to translate: ")
            result = translate_to_custom_morse(text, dot, dash)
            print(f"Custom Morse Code: {result}")
        elif choice == '2':
            custom_morse = input("Enter the custom Morse code to translate: ")
            result = translate_from_custom_morse(custom_morse, dot, dash)
            print(f"Plain Text: {result}")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
