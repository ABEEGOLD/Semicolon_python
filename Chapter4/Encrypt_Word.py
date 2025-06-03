def encrypt_rot13(text):
    result = ""
    for char in text:
        if 'a' <= char <= 'z':  
            result += chr(((ord(char) - ord('a') + 13) % 26) + ord('a'))
        elif 'A' <= char <= 'Z': 
            result += chr(((ord(char) - ord('A') + 13) % 26) + ord('A'))
        else:
            result += char  
    return result


word_encrypt = "animation"
print(encrypt_rot13(word_encrypt)) 