def decrypt(encrypted_message):
    decrypted_message = ""
    for char in encrypted_message:
        decrypted_char = ord(char) ^ 23
        c = decrypted_char
        b = (c + 7) // 3
        a = (b - 5) ^ 42
        original_char = (a - 10) // 2
        decrypted_message += chr(original_char)
    return decrypted_message


with open("flag.txt.enc", "r") as file:
    data = file.read()

decrypted_flag = decrypt(data)
print(decrypted_flag)