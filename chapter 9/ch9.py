# %% [markdown]
# ch9
# 9-1
# %%
fin = open("C:\\Users\\Jude Young\\Documents\\Coding\\DofE Project Gold\\ThinkPython\\chapter 9\\resources\\words.txt")
# for line in fin:
#     if len(line.strip()) > 20:
#         print(line.strip())
# %% [markdown]
# 9-2
# %%
def has_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
    return True
# for line in fin:
#     if has_no_e(line.strip()):
#         print(line.strip())
# %% [markdown]
# 9-3
# %%
def avoids(word, forbid):
    for letter in word:
        if letter in forbid:
            return False
    return True
def num_avoids():
    forbid = input('Enter forbidden letters\n')
    counter = 0
    for line in fin:
        if avoids(line.strip(), forbid):
            counter += 1
    return counter
# def combs(chars, choose):
#     for i in range(chars):
#         char = chars[i]
#         rem_chars = chars[i+1:]

#         for n in range(choose):
# %% [markdown]
# 9-4
# %%
def uses_only(str, word):
    for letter in word:
        if letter not in str:
            return False
    return True
def words_using_only(str):
    for line in fin:
        if uses_only(str, line.strip()):
            print(line.strip())
#words_using_only('acefhlo')
# %% [markdown]
# 9-5
# %%
def uses_all(str, word):
    for letter in str:
        if letter not in word:
            return False
    return True
def words_using_all(str):
    for line in fin:
        if uses_all(str, line.strip()):
            print(line.strip())
#words_using_all('aeiou')
# %%
# [markdown]
# 9-6
# %%
def is_abecedarian(word):
    for letter_index in range(0, len(word)-1): #start at 0, iterate to the penultimate letter so the last one is not checked against the first letter
        if word[letter_index] > word[letter_index+1]:
            return False
    return True
def all_isabc():
    for line in fin:
        if is_abecedarian(line.strip()):
            print(line.strip())
#all_isabc()
# %% [markdown]
# 9-7
# %%
def is_double(word):
    if len(word) <= 1: #base case 1
        return False
    if word[0] == word[1]: #base case 2
        return True
    return is_double(word[1:])
#print(is_double('hello'))
def is_tri_double(word):
    if len(word) <= 5: #base case 1
        return False
    if not is_double(word[0:2]):
        return is_tri_double(word[1:]) #recurse
    if is_double(word[0:2]) and is_double(word[2:4]) and is_double(word[4:6]):
        return True
    return False #base case 2
#print(is_tri_double('eeeeeef'))
def all_tri_double():
    for line in fin:
        if is_tri_double(line.strip()):
            print(line.strip())
#all_tri_double()
# %% [markdown]
# 9-8
# %%
def is_palindrome(word):
    return word == word[::-1]

def test_all_nums(start, end):
    for num in range(start, end):
        if is_palindrome(str(num)[2:]) and is_palindrome(str(num+1)[1:]) and is_palindrome(str(num+2)[1:5]) and is_palindrome(str(num+3)):
            print(num)
#test_all_nums(100000, 999999)
# %% [markdown]
# 9-9
# %%
def is_num_reversible(n1, n2):
    return str(n1).zfill(2) == str(n2).zfill(2)[::-1]

def test_nums(difference):
    counter = 0
    for n1 in range(difference, 120):
        if is_num_reversible(n1, n1-difference) or is_num_reversible(n1+1, n1-difference):
            counter += 1
    return counter

for difference in range(1, 50):
    if test_nums(difference) == 8:
        print(difference)