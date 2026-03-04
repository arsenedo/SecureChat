def caesar_shift(string: str, shift: int):
    result = ""
    for char in string:
        shifted = chr(ord(char) + shift)

        result += shifted
    return result

def xor(string, key):
    lengthMultiple = len(string) // len(key) + 1
    lenAdjustedKey = (key * lengthMultiple)[:len(string)]

    stringBytes = bytes(string, "utf-8")
    keyBytes = bytes(lenAdjustedKey, "utf-8")
    
    encodeTuple = zip(stringBytes, keyBytes)
    
    xorArray = []
    for pair in encodeTuple:
        xor = pair[0] ^ pair[1]

        xorArray.append(xor)
    
    xorBytes = bytes(xorArray)

    return xorBytes