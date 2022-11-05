# %% [markdown]
# ch8
# p87
# %%
def reverse(string):
    index = -1
    while abs(index) <= len(string):
        print(string[index])
        index -= 1
#reverse('hello')
# %% [markdown]
# p89
# %%
def find(string, character, start):
    for index in range(len(string)):
        if string[(index+start)%len(string)] == character:
            return (index+start)%len(string)
    return -1
# %%
print(find('aa', 'a', 0))
# %% [markdown]
# p90
# %%
def count(target, string):
    counter = 0
    for char in string:
        if char == target:
            counter += 1
    return counter
# %%
#print(count('a', 'aaa'))
# %%
def count2(target, string):
    index = -1
    counter = 0
    while find(string, target, index+1) > index:
        counter += 1
        index = find(string, target, index+1)
    return counter
# %%
print(count2('a', 'banana'))
# %% [markdown]
# exercises
# 8-1 read
# 8-2
# %%
str = 'banana'
print(str.count('a'))
# %% [markdown]
# 8-3
# %%
def is_palindrome2(str):
    return True if str == str[::-1] else False
print(is_palindrome2('anna'))
# %% [markdown]
# 8-4
# 1) will return True/False for if the first character is lower case, but will instantly break as it returns
# 2) will always return True as it is just checking 'c' not c
# 3) will return True/False for if the last character is lower case
# 4) will return True if any character is lower case
# 5) will return True if any character is lower case
# 8-5
# %%
def rotate_letter(letter, shift):
    if letter.isupper():
        start = 'A'
    elif letter.islower():
        start = 'a'
    else:
        return letter
    return chr((ord(letter) - ord(start)  + shift) % (26) + ord(start))
def rotate_word(word, shift):
    output = ''
    for letter in word:
        output += rotate_letter(letter, shift)
    return output
print(rotate_word('zelda', 1))