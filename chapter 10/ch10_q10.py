def in_bisect(targetValue:str, sortedList:list) -> bool:
    '''
    ## binary search

    ### inputs
    
    `targetValue`: str

    `sortedList`: list

    ### output
    
    returns True/False as to whether `targetValue` is in `sortedList`.
    '''
    if len(sortedList) == 1: #base case
        return sortedList == [targetValue]
    
    middleIndex = len(sortedList)//2 #if len(sortedList) is odd, this is the index of the median.
                                     #if len(sortedList) is even, this is the index of the first element in the second half of the list.
    
    if targetValue >= sortedList[middleIndex]:
        return in_bisect(targetValue, sortedList[middleIndex:])
    if targetValue < sortedList[middleIndex]:
        return in_bisect(targetValue, sortedList[:middleIndex])

def main():
    '''run tests'''
    print('test output: ', in_bisect('e', ['a', 'b', 'c', 'd', 'e', 'f', 'g']))

if __name__ == '__main__':
    main()