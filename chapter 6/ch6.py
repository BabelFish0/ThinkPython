# %% [markdown]
# ch6
# p62
# %%
def compare(x, y):
    if x>y:
        return 1
    if x<y:
        return -1
    else:
        return 0
# %% [markdown]
# p66
# %%
def is_between(x, y, z):
    return x <= y <= z
# %% [markdown]
# ex 6-2
# %%
# Ackermann function A(m, n)
# https://en.wikipedia.org/wiki/Ackermann_function
def ack(m, n):
    if m < 0 or n < 0:
        print("for positive integers only")
        return None
    if not (isinstance(n, int) or isinstance(m, int)):
        print("for positive integers only")
        return None
    if m == 0:
        return n+1
    if m > 0 and n == 0:
        return ack(m-1, 1)
    if m > 0 and n > 0:
        return ack(m-1, ack(m, n-1))
# %%
def ack2(m, n):
    '''more compact version of ack() - after looking at https://github.com/AllenDowney/ThinkPython2/blob/master/code/ackermann.py'''
    if m < 0 or n < 0:
        print("for positive integers only")
        return None
    if not (isinstance(n, int) or isinstance(m, int)):
        print("for positive integers only")
        return None
    if m == 0:
        return n+1
    if n == 0:
        return ack2(m-1, 1)
    return ack2(m-1, ack2(m, n-1))
# %%
#print(ack2(3, 5))
# %% [markdown]
# extension look at ex 6-2
# %%
import matplotlib.pyplot as plt
import numpy

lim = 4

Z = numpy.zeros((lim, lim))
for x in range(lim):
    for y in range(lim):
        Z[x][y] = numpy.log(ack2(x, y))

fig, ax = plt.subplots()
c = ax.pcolor(Z)
fig.colorbar(c, ax=ax)
#plt.show()
# %% [markdown]
# ex 6-3
# %%
def first(word):
    return word[0]
def last(word):
    return word[-1]
def middle(word):
    return word[1:-1]
def is_palindrome(word):
    for letter in range(len(word)):
        if not(word[letter] == word[len(word)-letter-1]):
            return False
    return True
print(is_palindrome('dammitimmad'))