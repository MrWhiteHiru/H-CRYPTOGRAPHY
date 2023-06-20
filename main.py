import hashlib
import base64

# Colors
colors = {
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'purple': '\033[95m',
    'cyan': '\033[96m',
    'end': '\033[0m'
}

def print_banner():
    banner = r"""
{}█░█   █▀▀ █▀█ █▄█ █▀█ ▀█▀ █▀█ █▀▀ █▀█ ▄▀█ █▀█ █░█ █▄█
█▀█   █▄▄ █▀▄ ░█░ █▀▀ ░█░ █▄█ █▄█ █▀▄ █▀█ █▀▀ █▀█ ░█░
                                [#] By MR WHITE HIRU
                                [#] HISL TEAM
     """.format(colors['green'], colors['end'])
    
    print(banner)

def md5_encrypt(text):
    md5_hash = hashlib.md5()
    md5_hash.update(text.encode())
    return md5_hash.hexdigest()

def md5_decrypt(hashed_text):
    print("")
    print(colors['red'] + " [!] Decryption of MD5 hash is not possible due to its irreversible nature." + colors['end'])
    print("")
def base32_encrypt(text):
    base32_encoded = base64.b32encode(text.encode()).decode()
    return base32_encoded

def base32_decrypt(encoded_text):
    try:
        base32_decoded = base64.b32decode(encoded_text).decode()
        return base32_decoded
    except base64.binascii.Error:
        print("")
        print(colors['red'] + "[!] Invalid Base32 input!" + colors['end'])
        print("")
        return None

def base64_encrypt(text):
    base64_encoded = base64.b64encode(text.encode()).decode()
    return base64_encoded

def base64_decrypt(encoded_text):
    try:
        base64_decoded = base64.b64decode(encoded_text).decode()
        return base64_decoded
    except base64.binascii.Error:
        print("")
        print(colors['red'] + "[!] Invalid Base64 input!" + colors['end'])
        print("")
        return None

# Main program
print_banner()

while True:
    print(colors['blue'] + "[1] Encrypt text with MD5")
    print("[2] Decrypt MD5 hash")
    print("[3] Encrypt text with Base32")
    print("[4] Decrypt Base32")
    print("[5] Encrypt text with Base64")
    print("[6] Decrypt Base64")
    print("[7] Exit" + colors['end'])
    choice = input(colors['blue'] + "[+] Enter your choice (1-7): " + colors['end'])

    if choice == '1':
        plaintext = input(colors['blue'] + "[#] Enter the text to encrypt: " + colors['end'])
        encrypted_text = md5_encrypt(plaintext)
        print("")
        print("[$] Encrypted text (MD5 hash):", colors['green'] + encrypted_text + colors['end'])
        print("")
        print("*"*50)
        print("")
    elif choice == '2':
        hashed_text = input(colors['blue'] + "[#] Enter the MD5 hash to decrypt: " + colors['end'])
        md5_decrypt(hashed_text)
    elif choice == '3':
        plaintext = input(colors['blue'] + "Enter the text to encrypt: " + colors['end'])
        encrypted_text = base32_encrypt(plaintext)
        print("")
        print("[$] Encrypted text (Base32):", colors['green'] + encrypted_text + colors['end'])
        print("")
        print("*"*50)
        print("")
    elif choice == '4':
        encoded_text = input(colors['blue'] + "[#] Enter the Base32 encoded text to decrypt: " + colors['end'])
        decrypted_text = base32_decrypt(encoded_text)
        if decrypted_text:
            print("")
            print("[$] Decrypted text (Base32):", colors['green'] + decrypted_text + colors['end'])
            print("")
            print("*"*50)
            print("")
    elif choice == '5':
        plaintext = input(colors['blue'] + "[#] Enter the text to encrypt: " + colors['end'])
        encrypted_text = base64_encrypt(plaintext)
        print("")
        print(" [#] Encrypted text (Base64):", colors['green'] + encrypted_text + colors['end'])
        print("")
        print("*"*50)
        print("")
    elif choice == '6':
        encoded_text = input(colors['blue'] + "[#] Enter the Base64 encoded text to decrypt: " + colors['end'])
        decrypted_text = base64_decrypt(encoded_text)
        if decrypted_text:
            print("[$] Decrypted text (Base64):", colors['green'] + decrypted_text + colors['end'])
            print("")
            print("*"*50)
            print("")


    elif choice == '7':
        break
    else:
        print("")
        print(colors['red'] + "[!] Invalid choice! Please enter a valid option." + colors['end'])
        print("")
print("")
print("-"*60 + "                                                                                         +")
print(colors['blue'] + " [#] Thank you for using the encryption and decryption tool!" + colors['end'] + "+")
print("                                                                                                  +")
print("-"*60+"                                                                                           +")