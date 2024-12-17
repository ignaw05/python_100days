alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
        encripted = ''
        for i in original_text:
            mov = alphabet.index(i)+shift_amount
            mov %= len(alphabet)
            encripted += alphabet[mov]
        print(encripted)


def decrypt(original_text, shift_amount):
    decripted = ''
    for i in original_text:
        mov = alphabet.index(i)-shift_amount
        mov %= len(alphabet)
        decripted += alphabet[mov]
    print(decripted)

def caesar(orignal_text,shift_amount,direction):
    if direction == 'encode':
        encrypt(orignal_text,shift_amount)
    elif direction == 'decode':
        decrypt(orignal_text,shift_amount)
    else: print("You entered a wrong parameter")

caesar(text,shift,direction)
          
    

