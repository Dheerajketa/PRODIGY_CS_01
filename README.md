# Caesar Cipher Program

This Python program allows you to encrypt and decrypt text using the Caesar Cipher algorithm. You can input a message and a shift value to perform encryption and decryption.

## Features

- Encrypt a message using a specified shift value.
- Decrypt a message using a specified shift value.
- Handles both uppercase and lowercase letters.
- Maintains non-alphabetic characters (e.g., punctuation, spaces) unchanged.

## Requirements

- Python 3.x

## Usage

1. Clone the repository or download the script file.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the script.
4. Run the script using the command:

    ```sh
    python caesar_cipher.py
    ```

5. Follow the on-screen prompts to encrypt or decrypt a message.

## Example

```sh
Welcome to the Caesar Cipher Program!
Would you like to (E)ncrypt or (D)ecrypt a message? (Enter Q to quit): E
Enter the message: Hello, World!
Enter the shift value: 3
Encrypted message: Khoor, Zruog!

Would you like to (E)ncrypt or (D)ecrypt a message? (Enter Q to quit): D
Enter the message: Khoor, Zruog!
Enter the shift value: 3
Decrypted message: Hello, World!
