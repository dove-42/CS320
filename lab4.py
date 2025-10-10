def convertToBase(num, base):
    convertedNum = ""
    if num == 0:
        return ""
    else:
        quotient, remainder = divmod(num, base)
        return convertToBase(quotient, base) + str(remainder)
