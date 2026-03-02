def caesar_shift(string: str, shift: int):
    result = ""
    for char in string:
        if not char.isalpha():
            result += char
            continue

        normalizationShift = ord("a") if char.islower() else ord("A")
        
        normalizedShifted = (ord(char) - normalizationShift + shift) % 26
        shifted = chr(normalizedShifted + normalizationShift)

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