from collections.abc import Collection
from math import e, modf, floor, sqrt
from itertools import filterfalse, chain
from copy import copy
import unittest


# DO NOT CHANGE ANY CODE BETWEEN LINE X AND LINE Y
# ******* THIS IS LINE X ******************

GOLDEN = (1.0 + 5.0 * 0.5) / 2.0


def swap(a, b):
    return b, a


# ***************************************************
# why do we inherit from Collection rather than Set?
# because Set requires too many methods to be defined


class CuckooSet(Collection):

    # *** course helper routines *******
    def _hash2_(self, obj, table_size):
        try:
            h = hash(obj)  # may raise exception
        except Exception:
            raise TypeError("unhashable key")

        h %= table_size

        f1, _ = modf(h * e)
        f2, _ = modf(h * GOLDEN)
        h1 = floor(table_size * f1)
        h2 = floor(table_size * f2)
        if h1 == h2:
            h2 = (h2 + 7) % table_size
        return h1, h2

    def _members_(self, tab):  # returns iterator
        return filterfalse((lambda x: x is None), tab)

    def _allmembers_(self):
        return chain(self._members_(self.htab1), self._members_(self.htab2))

    # ** course methods ****

    def __init__(self, iter=[], *, s=128):
        if s < 4:
            raise ValueError("set size too small")
        self._size_ = s
        self._MAXSWAPS_ = floor(s * 0.6)
        self.htab1 = [None] * s
        self.htab2 = [None] * s
        for i in iter:
            self.add(i)

    def __len__(self):
        count1 = len(list(self._members_(self.htab1)))
        count2 = len(list(self._members_(self.htab2)))
        return count1 + count2

    def _resize_(self):
        oldself = copy(self)
        self.__init__(oldself, s=oldself._size_ * 2)

    def __str__(self):
        fstr = ""
        for v in self._allmembers_():
            if len(fstr):
                fstr += ", "
            fstr += str(v)
        return fstr

    def __iter__(self):
        return self._allmembers_()
# ******* THIS IS LINE Y ******************

    def isHashable(self, x):
        try:
            hash(x)
        except TypeError:
            return False
        return True


    def __contains__(self, x):
        if x is None:
            raise ValueError("key may not be None")
        try:
            hash1, hash2 = self._hash2_(x, self._size_)
        except TypeError:
            return False
        return self.htab1[hash1] == x or self.htab2[hash2] == x


    def add(self, x):
        if x is None:
            raise ValueError("key may not be None")
        if self.isHashable(x):
            counter = 0
            while counter < self._MAXSWAPS_:
                hash1, hash2 = self._hash2_(x, self._size_)

                if self.htab1[hash1] is None:
                    self.htab1[hash1] = x
                    return True

                oldVal = self.htab1[hash1]
                self.htab1[hash1] = x

                newHash1, newHash2 = self._hash2_(oldVal, self._size_)

                if self.htab2[newHash2] is None:
                    self.htab2[newHash2] = oldVal
                    return True

                x = self.htab2[newHash2]
                self.htab2[newHash2] = oldVal
                counter += 1
            self._resize_()
            return self.add(x)
        else:
            raise TypeError("unhashable key")


    def remove(self, x):  # Raises Exception if x is not in the tables
        if x is None:
            raise ValueError("key may not be None")
        try:
            hash1, hash2 = self._hash2_(x, self._size_)
        except TypeError:
            return
        if self.htab1[hash1] == x:
            self.htab1[hash1] = None
            return
        elif self.htab2[hash2] == x:
            self.htab2[hash2] = None
            return
        else:
            raise Exception


    def discard(self, x):  # Silently returns if x is not in the tables
        if x is None:
            raise ValueError("key may not be None")
        try:
            hash1, hash2 = self._hash2_(x, self._size_)
        except TypeError:
            return
        if self.htab1[hash1] == x:
            self.htab1[hash1] = None
        elif self.htab2[hash2] == x:
            self.htab2[hash2] = None
        return
