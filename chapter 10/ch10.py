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
    list2_copy = list2
    for element in list1:
        if element not in list2_copy:
            return False
        list2_copy.remove(element)
    return True

#10-7
def has_duplicates(initialList:list) -> bool:
    for i in range(len(initialList)):
        if initialList[i] in initialList[:i] + initialList[i+1:]:
            return True
    return False

#10-8
import random
def random_bdays(n):
    birthdays = []
    for i in range(n):
        birthdays.append(random.randint(1, 365))
    return birthdays

def count_matches(nStudents, nSims):
    count = 0
    for i in range(nSims):
        t = random_bdays(nStudents)
        if has_duplicates(t):
            count += 1
    return count

#10-9
import time
def run_9(): #test speed of array methods
    fin = open("/Users/jude/Documents/Python/think_python/ThinkPython/chapter 9/resources/words.txt") #C:\\Users\\Jude Young\\Documents\\Coding\\DofE Project Gold\\ThinkPython\\chapter 9\\resources\\words.txt
    l = []
    t1 = time.time()
    print('starting test for append method')
    for line in fin:
        l.append(line)
    t2 = time.time()
    print(f'test 1 complete, time = {t2-t1}\nstarting test for add')
    t1 = time.time()
    for line in fin:
        l = l + [line]
    t2 = time.time()
    print(f'test 2 complete, time = {t2-t1}')
    fin.close()

#10-10
def bin_search(targetVal):
    import ch10_q10
    with open("/Users/jude/Documents/Python/think_python/ThinkPython/chapter 9/resources/words.txt") as fin:
        wordList = [word.strip() for word in fin]
        return ch10_q10.in_bisect(targetVal, wordList)

#10-11 in separate file

#10-12 in separate file

def tests():
    print('Test input for 10-1: ', nestedSum([[1, 2], [3], [4, 5, 6]]))
    print('Test input for 10-2: ', cumulativeSum([1, 2, 3, 4]))
    print('Test input for 10-3: ', excludeOuterValues([1, 2, 3, 4]))
    t = [1, 2, 3, 4]
    print('Test input for 10-4: ', t)
    chop(t)
    print('Test output for 10-4: ', t)
    print('Test input for 10-5: ', is_sorted([1, 2, 3]), is_sorted(['b', 'a']))
    print('Test input for 10-6: ', is_anagram([1, 1, 3], [1, 3, 1]))
    print('Test input for 10-7: ', has_duplicates([1, 2, 4, 4]))
    print('Test input for 10-8: ', count_matches(23, 100))
    print('Test run for 10-9: ')
    run_9()
    print('Test input for 10-10: ', bin_search('egg'))

if __name__ == '__main__':
    tests()