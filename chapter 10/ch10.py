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

def tests():
    print('Test input for 10-1: ', nestedSum([[1, 2], [3], [4, 5, 6]]))
    print('Test input for 10-2: ', cumulativeSum([1, 2, 3, 4]))
    print('Test input for 10-3: ', excludeOuterValues([1, 2, 3, 4]))

if __name__ == '__main__':
    tests()