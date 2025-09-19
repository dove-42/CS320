def verifyTree(t):
    if t == None:
        raise ValueError("no_tree")
        return False
    return True

def computeHeight(t):
    #takes in the treeList and computes height of the tree
    #each key has 0-2 children, find teh deppest number of children
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


def findKey(k,t):  # Return the index in t which holds the value k
    if len(t) == 0:
        raise LookupError("not_in_tree")
    else:
        index = findKeyHelper(k, t, 0)
        if index == None:
            raise LookupError("not_in_tree")
        else:
            return index

    if t.size() == 0:  # Tree is empty
        raise LookupError("not_in_tree")
        return None
    #if k not in t: raise LookupError("not_in_tree")
    #leftChild of key i is at index [(i*2)+1], rightChild at index [(i*2)+2]
    return

def addKey(k,t):  # Return the updated tree, maintain binary search properties
    if k == None:
        raise ValueError("null_key")
    if t.size() == 0:  # Tree is empty
        t += [k]
        return
    return

def deleteKey(k,t):  # Return the updated tree, maintain binary search properties
    if t.size() == 0:  # Tree is empty
        return
    #if all keys are gone, return an empty tree
    return

#Code must work with empty trees