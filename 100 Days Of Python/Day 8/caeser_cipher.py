alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar(a,b):
    end_text = ''
    for char in a:
        if char in alphabet:
            if b == "decode":
                end_text += alphabet[coded_alphabet.index(char)]
            else:
                end_text += coded_alphabet[alphabet.index(char)]
        else:
            end_text += char
    print(f"The {b}d text is {end_text}")

run_program = input("Would you like to run the cipher program (y,n)?\n").lower()
while run_program == 'y':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    coded_alphabet = alphabet[shift:] + alphabet[:shift]
    caesar(a=text,b=direction)
    run_program = input("Would you like to run the cipher program (y,n)?\n").lower()