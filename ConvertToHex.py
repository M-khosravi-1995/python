def ConvertToHex(dec):
    x = (dec % 16)
    digits = "0123456789ABCDEF"
    rest = dec / 16
    if (rest == 0):
        return digits[x]
    return ConvertToHex(rest) + digits[x]

numbers = [0, 11, 16, 32, 33, 41, 45, 678, 574893]
print [ConvertToHex(x) for x in numbers]
print [hex(x) for x in numbers]