'''
Program to find all reverse pairs of words in `words.txt`.
'''

def main():
    import ch10_q10 as finder
    reverse_pairs = []

    with open("/Users/jude/Documents/Python/think_python/ThinkPython/chapter 9/resources/words.txt") as fin:
        words = [word.strip() for word in fin]
    
    for word in words:
        if finder.in_bisect(word[::-1], words):
            reverse_pairs.append((word, word[::-1]))
    
    return reverse_pairs

if __name__ == '__main__':
    print(main())