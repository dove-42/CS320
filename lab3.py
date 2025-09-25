def isEmpty(stringToCheck):
    return len(stringToCheck) == 0

def isNone(stringToCheck):
    return stringToCheck is None

def isValidLength(reference, query):
    return len(query) < len(reference)

def bruteForceCompare(reference, query):
    i = 0
    while reference[i] == query[i] and i < len(query):
        i = i + 1
    if i == len(query) - 1:
        return True
    return False

def computeHashVal(sequence, alphabet):
    return

def countPermStr(string1, string2):
    if isEmpty(string2):
        raise ValueError
    if isNone(string1) or isNone(string2):
        raise ValueError
    if not isValidLength(string1, string2):
        raise ValueError

    numMatches = 0


    return numMatches
