def encrypt(original_text, shift_amount):
    final = ""
    for enc_letter in original_text:
        if enc_letter not in alphabet:
            final += enc_letter
            continue
        index = alphabet.index(enc_letter) + shift_amount
        if len(alphabet) <= index:
            index -= len(alphabet)
        save_letter = alphabet[index]

        final += save_letter
    print(f"Here is encoded word {final}")

def decode(crypt_text:str, shift_amount:int):
    final = ""
    for cr_letter in crypt_text:
        if cr_letter not in alphabet:
            final += cr_letter
            continue
        index = alphabet.index(cr_letter) - shift_amount
        if index < 0:
            index += len(alphabet)
        save_letter = alphabet[index]

        final += save_letter
    print(f"Here is decoded word {final}")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

go_on = "yes"

while go_on == 'yes':

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == 'encode':
        encrypt(text, shift)
    elif direction == 'decode':
        decode(text, shift)
    else:
        print("Uncorrect text")

    go_on = input("Type 'yes' if you want to go again. Otherwise type 'no':")
print()