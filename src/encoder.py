def caesar_shift(word: str, shift: int):
    result = ""
    for char in word:
        if not char.isalpha():
            result += char
            continue

        normalizationShift = ord("a") if char.islower() else ord("A")
        
        normalizedShifted = (ord(char) - normalizationShift + shift) % 26
        shifted = chr(normalizedShifted + normalizationShift)

        result += shifted

    return result