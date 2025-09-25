def isEmpty(stringToCheck):
    return len(stringToCheck) == 0

def isNone(stringToCheck):
    return stringToCheck is None

def isValidLength(reference, query):
    return len(query) < len(reference)

def countPermStr(string1, string2):
    if isEmpty(string2):
        raise ValueError
    if isNone(string1) or isNone(string2):
        raise ValueError
    if not isValidLength(string1, string2):
        raise ValueError

    return
