def karatsuba(num1, num2):
    num1Str = str(num1)
    num2Str = str(num2)
    if (num1 < 10) or (num2 < 10):
        return num1*num2

    maxLength = max(len(num1Str), len(num2Str))
    splitPosition = int(maxLength / 2)
    a, b= int(num1Str[:-splitPosition]), int(num1Str[-splitPosition:])
    c, d= int(num2Str[:-splitPosition]), int(num2Str[-splitPosition:])
    z0 = karatsuba(b, d)
    z1 = karatsuba((b + a), (d + c))
    z2 = karatsuba(a, c)

    return (z2*10**(2*splitPosition)) + ((z1-z2-z0)*10**(splitPosition))+z0
