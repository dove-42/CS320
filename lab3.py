from collections import Counter

def isEmpty(stringToCheck):
    return len(stringToCheck) == 0

def isNone(stringToCheck):
    return stringToCheck is None

def isValidLength(reference, query):
    return len(query) < len(reference)

def ableToMatch(reference, query):
    dictQuery = Counter(query)
    dictRef = Counter(reference)

    queryKeys = set(dictQuery.keys())
    refKeys = set(dictRef.keys())

    return queryKeys.issubset(refKeys)

def countPermStr(string1, string2):
    if isEmpty(string2):
        raise ValueError

    if isNone(string1) or isNone(string2):
        raise ValueError

    if not isValidLength(string1, string2):
        raise ValueError

    if not ableToMatch(string1, string2):
        return 0

    numMatches = 0
    i = 0
    m = len(string2)
    queryDict = Counter(string2)

    while len(string[i:]) >= m:
        refDict = Counter(string1[i : i + m])

        if refDict == queryDict:
            numMatches += 1

        i += 1
    return numMatches
