#10-1
def nestedSum(intitialList:list) -> int:
    '''
    ### input:
    list containing nested lists of ints.

    ### returns:
    sum of all int elements within nested lists.
    '''
    total = 0
    for element in intitialList:
        if not isinstance(element, int):
            total += nestedSum(element)
        else:
            return sum(intitialList) #base case
    return total

#10-2
def cumulativeSum(initialList:list) -> int:
    '''
    ### input:
    list of ints

    ### returns:
    list where the `i`th element is the cumulative sum of all elements up to the `i`th.
    '''
    cumulativeSumList = []
    for i in range(len(initialList)):
        cumulativeSumList.append(sum(initialList[:i+1]))
    return cumulativeSumList

#10-3
def excludeOuterValues(initialList:list) -> list:
    '''
    ### input:
    list

    ### returns:
    list excluding the 0th and -1th elements.
    '''
    return initialList[1:-1]

#10-4
def chop(initialList:list) -> None:
    '''
    ### input:
    list

    ### modifies:
    list excluding the 0th and -1th elements.
    '''
    del initialList[0]
    del initialList[-1]

#10-5
def is_sorted(initialList:list) -> bool:
    '''
    ### input:
    list

    ### returns:
    `True` if list is in ascending order and `False` if not.
    '''
    return initialList == sorted(initialList)

#10-6
def is_anagram(list1:list, list2:list) -> bool:
    '''
    ### input:
    two lists

    ### returns:
    `True` if lists are anagrams of each other.
    '''
    return set(list1) == set(list2)

def tests():
    print('Test input for 10-1: ', nestedSum([[1, 2], [3], [4, 5, 6]]))
    print('Test input for 10-2: ', cumulativeSum([1, 2, 3, 4]))
    print('Test input for 10-3: ', excludeOuterValues([1, 2, 3, 4]))
    t = [1, 2, 3, 4]
    print('Test input for 10-4: ', t)
    chop(t)
    print('Test output for 10-4: ', t)
    print('Test input for 10-5: ', is_sorted([1, 2, 3]), is_sorted(['b', 'a']))
    print('Test input for 10-6: ', is_anagram([1, 1, 3, 1], [1, 3, 1]))

if __name__ == '__main__':
    tests()