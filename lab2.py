def verifyTree(t):
    if t == None:
        raise ValueError("no_tree")
        return False
    return True

def verifyKey(k):
    if k == None:
        raise ValueError("null_key")
        return False
    return True

def computeHeight(t):
    #takes in the treeList and computes height of the tree
    #each key has 0-2 children, find the deppest number of children
    #can use recursion to visit children nodes
    return

    
def hasLeftChild(index, t):
    if ((index * 2) + 1) < len(t):
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


def findKey(k,t):
    if not verifyTree(t):
        return
    if not verifyKey(k):
        return
    if len(t) == 0:
        raise LookupError("not_in_tree")
    else:
        index = findKeyHelper(k, t, 0)
        if index == None:
            raise LookupError("not_in_tree")
        else:
            return index

def addKeyHelper(k, t):
    if findKey(k, t) != None:
        return t
    else:
         # Find where key should go, but isn't, and add it, recursively fixing children pointers
         # Return t

def addKey(k,t):  # Return the updated tree, maintain binary search properties
    if not verifyKey(k):
        return
    if not verifyTree(t):
        return
    if len(t) == 0:
        return t
    else:
        newT = addKeyHelper(k,t)
        return newT

def deleteKeyHelper(k, t):
    index = findKey(k, t)
    if index == None:  # Key is not in tree
        return 
    else:
        # Remove key at index, recursively fixing children pointers
        # Return new tree

def deleteKey(k,t):  # Return the updated tree, maintain binary search properties
    if not verifyKey(k):
        return
    if not verifyTree(t):
        return
    if len(t) == 0:  # Tree is empty
        return
    #if all keys are gone, return an empty tree
    return
