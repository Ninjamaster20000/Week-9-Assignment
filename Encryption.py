def _encrypt(text):
    secured = ''

    for i in range (len(text)):
        num = ord(text[i]) + 3
        letter = chr(num)

        secured = secured + letter
    
    print("Unsecured", text)
    print("Secured:", secured)
    return secured

def _decrypt(text):
    secured = ''

    for i in range (len(text)):
        num = ord(text[i]) - 3
        letter = chr(num)

        secured = secured + letter
    
    print("Unsecured", text)
    print("Secured:", secured)

encrypted = _encrypt("Howisitgoing")
print()
_decrypt(encrypted)