
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


print("Welcome to Caeser Cipher")
print("What you want to do?")

def user_method():
    method = input("Write e/encrypt or d/decrypt: ").lower()
    if method == "encrypt" or method == "e":
        print("Encrypting ...")
        return "encrypt"
    elif method == "decrypt" or method == "d":
        print("Decrypting ...")
        return "decrypt"
    else:
        print("Wrong method!")
        user_method()


exit_app = False


while not exit_app:
    method = user_method()
    text = input("Write Your Message\nNo Spaces (If found Space, That will be auto removed)\n\n").lower()
    text = text.replace(" ", "")


    try:
        shift = int(input("Write Shift number: "))
    except:
        print("Not a number")


    def encrypt(text, shift):
        encrypted_text = ""
        for char in text:
            original_index = alphabet.index(char)
            new_index = original_index + shift

            if new_index > 25:
                new_index = new_index - 26
            
            encrypted_text += alphabet[new_index]
        print(f"Your Encrypted Text Is: {encrypted_text}")


    def decrypt(text, shift):
        decrypt_text = ""
        for char in text:
            original_index = alphabet.index(char)
            new_index = original_index - shift

            if new_index < 0:
                new_index = new_index + 26
            
            decrypt_text += alphabet[new_index]

        print(f"Your Decrypted Text Is: {decrypt_text}")


    if method == "encrypt":
        encrypt(text, shift)
    else:
        decrypt(text, shift)
    
    continue_app = input("Continue? (yes/no)").lower()

    if continue_app == "yes" or continue_app == "y":
        print("Continuing encrypt decrypt ...")
    else:
        print("Exiting Now!\nThanks for trying Caeser Cipher")
        exit_app = True
