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