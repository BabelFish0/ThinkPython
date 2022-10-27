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
