def main():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    dir = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("enter the text:\n").lower()
    shift = int(input("enter the shift:\n"))

    if dir == 'encode':
        caesar(text, shift, alphabet)
    elif dir == 'decode':
        caesar(text, shift * -1, alphabet)
    else:
        print("Error!")


def caesar(text, shift, alphabet):
    cipher_text = ""
    for letter in text:
        position = alphabet.index(letter)
        new_position = position + shift % 26
        cipher_text += alphabet[new_position]
    print(cipher_text)


if __name__ == '__main__':
    main()

