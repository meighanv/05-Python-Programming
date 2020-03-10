def convertAndShift(bStr):
    if len(bStr) != 16:
        return f"INVALID_LENGTH"
    else:
        if (string.isdigit() == False):
            return f"INVALID_VALUE"
        try:
            num = int(bStr,2)
            if (num%2 == 0):
                num = num << 2
            else:
                num = num >> 1
            if (num > 200):
                num = ~num
            else:
                pass
        except ValueError:
            return f"INVALID_VALUE"
        return num
