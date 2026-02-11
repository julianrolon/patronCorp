def caesar_cipher(string, offset):
    result = ""
    for char in string:
        int_char = ord(char)
        if int_char - offset < ord('a'):
            int_char = int_char + 26
        int_char = int_char - offset
        result = result + chr(int_char)    
    return result

#print(caesar_cipher("hello", 3))


def caesar_cipher2(string, offset):
    alphabet = list(chr(i) for i in range(ord('a'), ord('z')+1))
    encode_string = ""
    for char in string:
        position = alphabet.index(char)
        offset_position = position - offset
        encode_char = alphabet[offset_position]
        # print(position, char, alphabet[position])
        encode_string += encode_char
        # print(encode_string)
    #print(alphabet)
    return encode_string

print(caesar_cipher2("zello", 3))


