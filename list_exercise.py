def nested_sum(t):
    """Computes the total of all numbers in a list of lists.
    t: list of list of numbers
    returns: number
    Expected output:
    >>> t = [[1, 2], [3], [4, 5, 6]]
    >>> nested_sum(t)
    21
    """
    """i know this works
t = [[1,2],[3],[4,5,6]]
a = sum(t[0])
b = sum(t[1])
c = sum(t[2])
print(a+b+c)
    """
    total = 0 #we are being asked to return something we store here
    t = [[1, 2], [3], [4, 5, 6]] #three lists
    for i in t:
        total += sum(i)
    return total 
    

def cumsum(t):
    """Computes the cumulative sum of the numbers in t.
    t: list of numbers
    returns: list of numbers
    Expected output:
    >>> t = [1, 2, 3]
    >>> cumsum(t)
    [1, 3, 6]
    """

    result =[]
    total = 0
    for i in t:
        total += i
        result.append(total)
    return result


def middle(t):
    """Returns all but the first and last elements of t.
    t: list
    returns: new list
    Expected output:
    >>> t = [1, 2, 3, 4]
    >>> middle(t)
    [2, 3]
    """
    t = [1,2,3,4]
    t = t[1:-1]
    return t


def chop(t):
    """Removes the first and last elements of t.
    t: list
    returns: None
    Expected output
    >>> t = [1, 2, 3, 4]
    >>> chop(t)
    >>> t
    [2, 3]
    """
    t = [1,2,3,4]
    del t[0]
    del t[-1]
    print(t)



def is_sorted(t):
    """Checks whether a list is sorted.
    t: list
    returns: boolean
    Expected output:
    >>> is_sorted([1, 2, 2])
    True
    >>> is_sorted(['b', 'a'])
    False
    """

    

    if t == sorted(t):
        return True
    else:
        return False
    
    print(is_sorted([1,2,2]))
    print(is_sorted(['a','b']))


def is_anagram(word1, word2):
    """Checks whether two words are anagrams
    Two words are anagrams if you can rearrange the letters from one to 
    spell the other.
    word1: string or list
    word2: string or list
    returns: boolean
    Expected output:
    >>> is_anagram('stop', 'pots')
    True
    >>> is_anagram('different', 'letters')
    False
    >>> is_anagram([1, 2, 2], [2, 1, 2])
    Ture
    """


def has_duplicates(s):
    """Returns True if any element appears more than once in a sequence.
    s: string or list
    returns: bool
    """
    for i in s:
        if s.count(i)>1:
            return True
        else:
            return False
print(has_duplicates('cba'))
print(has_duplicates('abba'))


def main():
    t = [[1, 2], [3], [4, 5, 6]]
    print(nested_sum(t))

    t = [1, 2, 3]
    print(cumsum(t))

    t = [1, 2, 3, 4]
    print(middle(t))
    chop(t)
    print(t)

    print(is_sorted([1, 2, 2]))
    print(is_sorted(['b', 'a']))

    print(is_anagram('stop', 'pots'))
    print(is_anagram('different', 'letters'))
    print(is_anagram([1, 2, 2], [2, 1, 2]))

    print(has_duplicates('cba'))
    print(has_duplicates('abba'))


if __name__ == '__main__':
    main()