def verifyTree(t):
    if t is None:
        raise ValueError("no␣tree")
        return False
    return True

def verifyKey(k):
    if k is None:
        raise ValueError("null␣key")
        return False
    return True

def leftChildIsValid(index, t):
    if t[index  * 2 + 1] is not None:
        return True
    return False

def rightChildIsValid(index, t):
    if t[index * 2 + 2] is not None:
        return True
    return False

def hasLeftChild(index, t):
    if (index * 2 + 1) < len(t):
        return True
    return False

def hasRightChild(index, t):
    if ((index * 2) + 2) < len(t):
        return True
    return False

def findKeyHelper(k, t, index):
    if index >= len(t):
        return None
    if k == t[index]:
        return index
    elif k < t[index] and hasLeftChild(index, t):
        return findKeyHelper(k, t, (index * 2 + 1))
    elif k > t[index] and hasRightChild(index, t):
        return findKeyHelper(k, t, (index * 2 + 2))
    return None

def findKeyIndex(k, t):
    if not verifyTree(t):
        return
    if not verifyKey(k):
        return
    if len(t) == 0:
        raise LookupError("not␣in␣tree")
    else:
        index = findKeyHelper(k, t, 0)
        return index

def findKey(k,t):
    if not verifyTree(t):
        return
    if not verifyKey(k):
        return
    if len(t) == 0:
        raise LookupError("not␣in␣tree")
    else:
        index = findKeyHelper(k, t, 0)
        if index is None:
            raise LookupError("not␣in␣tree")
            return None
        else:
            return index

def extendTree(toIndex, t):
    if toIndex >= len(t):
        t += [None] * (toIndex - len(t) + 1)

def addKeyHelper(k, t, index):
    if index >= len(t):
        extendTree(index, t)
    if t[index] is None:
        t[index] = k
        return t
    elif k < t[index]:
        if hasLeftChild(index, t):
            return addKeyHelper(k, t, index * 2 + 1)
        else:
            extendTree(index * 2 + 1, t)
            t[index * 2 + 1] = k
            return t
    else:
        if hasRightChild(index, t):
            return addKeyHelper(k, t, index * 2 + 2)
        else:
            extendTree(index * 2 + 2, t)
            t[index * 2 + 2] = k
            return t

def addKey(k,t):
    if not verifyKey(k):
        return
    if not verifyTree(t):
        return
    if len(t) == 0:
        extendTree(2, t)
        t[0]  = k
        return t
    if findKeyIndex(k, t) is not None:
        return t
    else:
        newT = addKeyHelper(k, t, 0)
        return newT

def _iOILeft(n, t):  # Code taken from provided functions in lab instructions
    i = prev = n
    while (i < len(t)) and (t[i] is not None):
        prev = i
        i = (i * 2) + 1
    return prev if (prev != n) else None

def deleteKeyHelper(index, t):
    if t[index] is None:  # k has been successfully removed
        return t
    if not hasLeftChild(index, t) and not hasRightChild(index, t):  # Node is a leaf
        t[index] = None
        return t
    elif hasLeftChild(index, t) and not rightChildIsValid(index, t):  # Only has a nonNull left child
        leftChildIndex = index * 2 + 1
        t[index] = t[leftChildIndex]
        return deleteKeyHelper(leftChildIndex, t)
    elif not hasLeftChild(index, t) and hasRightChild(index, t):  # Only has nonNull right child
        rightChildIndex = index * 2 + 2
        t[index] = t[rightChildIndex]
        return deleteKeyHelper(rightChildIndex, t)
    else:  # Has two children
        successorIndex = _iOILeft(index, t)
        t[index] = t[successorIndex]
        return deleteKeyHelper(successorIndex, t)

def deleteKey(k, t):
    if not verifyKey(k):
        return
    if not verifyTree(t):
        return
    if len(t) == 0:
        return t
    else:
        indexToDelete = findKeyIndex(k, t)
        if indexToDelete is None:
            return t
        else:
            if(
                indexToDelete == 0
                and not hasLeftChild(indexToDelete, t)
                and not hasRightChild(indexToDelete, t)
            ):
                return []
            else:
                return deleteKeyHelper(indexToDelete, t)