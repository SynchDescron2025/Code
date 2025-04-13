def ceaser_encrypt(text,shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            result+=char
    print(result)
    return result

ceaser_encrypt("hello",4)


def ceaser_decrypt(text,shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base - shift) % 26 + base
            result += chr(shifted)
        else:
            result+=char
    print(result)
    return result

ceaser_decrypt("lipps",4)
