from collections import Counter
import math

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

def sumCharCountFactorials(charCounts):
    sum = 0
    for count in charCounts:
        sum += math.factorial(count)
    return sum

def getNumPerms(ref, query):
    numPerms = 0

    refDict = getDictionary(ref)
    queryDict = getDictionary(query)

    if refDict == queryDict:
        charCounts = queryDict.values()
        sumCharCounts = sumCharCountFactorials(charCounts)
        numPerms = math.factorial(len(query)) / sumCharCounts

    return numPerms      

def countPermStr(string1, string2):
    if isEmpty(string2):
        raise ValueError
    if isNone(string1) or isNone(string2):
        raise ValueError
    if not isValidLength(string1, string2):
        raise ValueError

    numMatches = 0
    #for every subSequence of query --> send to getNumPerms(subRefOfProperlength, subQuery)
    #add return value of getNumPerms to numMatches
    #shift subRefOfProperLength by one char every time getNumPerms returns until you hit the end of the string or the remaining chars are fewer than len(query)

    return numMatches


def countAllPerms(ref, query, refSub, querySub):
    if len(refSub) < len(querySub) or #end of refLine:

