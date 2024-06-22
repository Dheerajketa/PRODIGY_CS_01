def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def main():
    print("Welcome to the Caesar Cipher Program!")
    while True:
        choice = input("Would you like to (E)ncrypt or (D)ecrypt a message? (Enter Q to quit): ").upper()
        if choice == 'Q':
            break
        if choice not in ['E', 'D']:
            print("Invalid choice. Please enter 'E' to encrypt, 'D' to decrypt, or 'Q' to quit.")
            continue

        message = input("Enter the message: ")
        shift = int(input("Enter the shift value: "))

        if choice == 'E':
            result = caesar_cipher_encrypt(message, shift)
            print(f"Encrypted message: {result}")
        elif choice == 'D':
            result = caesar_cipher_decrypt(message, shift)
            print(f"Decrypted message: {result}")

if __name__ == "__main__":
    main()
