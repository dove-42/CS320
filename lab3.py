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

def bruteForceCompare(reference, queryDict):
    return queryDict == Counter(reference)

def calculateHash(sequence):
    return Counter(sequence)

def recalculateHash(oldHash, oldChar, newChar):
    if oldHash.get(oldChar) > 1:
        oldHash[oldChar] -= 1
    else:
        del oldHash[oldChar]
    if oldHash.get(newChar, None) is None:
        oldHash[newChar] = 1
    else:
        oldHash[newChar] += 1
    return oldHash

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
    queryHash = calculateHash(string2)
    hashVal = calculateHash(string1[:m])

    while len(string1[i:]) >= m:
        if hashVal == queryHash:
            comparison = bruteForceCompare(string1[i:i + m], queryDict)
            if comparison:
                numMatches += 1
        if i + m < len(string1):
            hashVal = recalculateHash(hashVal, string1[i], string1[i + m])
        i += 1

    return numMatches

