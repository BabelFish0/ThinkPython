def is_n_ways_interlocked(n:int, testWord:str, wordList:list) -> bool:
    '''
    General answer to Q10-12.

    inputs:
    ------
    `testWord`: string to test if it is comprised of alternating letters from multiple words.

    `n`: number of interlocking words to test.

    `wordList`: reference list of valid words. It is assumed that `testWord` is considered valid.

    output:
    ------
    `True` if the theoretical constituent words do exist in the reference list, `False` if not.
    '''
    import ch10_q10 as finder
    
    if len(testWord) < n:
        return False

    for wordNum in range(n):
        componentWord = testWord[wordNum::n]
        if not finder.in_bisect(componentWord, wordList):
            return False
    
    return True

def main(n) -> list:
    interlockedWords = []
    with open("/Users/jude/Documents/Python/think_python/ThinkPython/chapter 9/resources/words.txt") as fin:
        words = [word.strip() for word in fin]
    for word in words:
        if is_n_ways_interlocked(n, word, words):
            interlockedWords += [[word[wordNum::n] for wordNum in range(n)]]
    return interlockedWords

if __name__ == '__main__':
    print(main(4))