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

def leftChildIsValid(index, t):
    if t[index  * 2 + 1] != None:
        return True
    return False

def rightChildIsValid(index, t):
    if t[index * 2 + 2] != None:
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
    if findKey(k, t) != None:
        return t
    else:
        newT = addKeyHelper(k, t, 0)
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

def _iOILeft(n, t):
    i = prev = n
    while (i < len(t)) and (t[i] is not None):
    prev = i
    i = (i * 2) + 1
    return prev if (prev != n) else None

# left child -> parent
# right child -> leftmost of grandparent’s right
def _iOINext(n, t):
    r = (n * 2) + 2 # right
    if (r < len(t)) and (t[r] is not None):
# parent with right child
# move to leftmost child of right (or right
# if no child)
    if (n := _iOILeft(r, t)) is not None:
    return n
return r
elif n % 2:
# left leaf or left parent with no
# right child, go to parent
n = (n - 1) // 2 # left child -> parent
return n
else:
# at this point, right leaf with
# no right children. So node’s
# parent’s subtree is completed.
# so next is first ancestor
# above parent who is parent
# of a left node
p = (n - 2) // 2 # parent
leftp = p % 2
gp = (p - 1) // 2 # grandparent
while gp and (not leftp):
leftp = gp % 2
gp = (gp - 1) // 2
if leftp:
return gp
return -1
# this is a generator routine that
# returns successive elements in the
# inorder traversal
def _iOI(t):
# find leftmost child = start node
4
if (inorder := _iOILeft(0, t)) is None:
inorder = 0
while inorder >= 0:
yield t[inorder]
inorder = _iOINext(inorder, t)
