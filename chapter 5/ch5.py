# %% [markdown]
# chapter 5
# ex 5-1
# %%
import time

def convert(conversion, value):
    return value // conversion

seconds = str(time.time() % 60)
minutes = str(convert(60, time.time()) % 60)
hours = str(convert(60*60, time.time()) % 24)
days = str(convert(60*60*24, time.time()))
# %%
#print(days + " days, " + hours + " hours, " + minutes + " minutes and " + seconds + " seconds since the epoch.")
# %% [markdown]
# ex 5-2
# %%
def check_fermat(a, b, c, n):
    if n > 2 and a^n + b^n == c^n:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work.")
# %%
#check_fermat(int(input('a\n')), int(input('b\n')), int(input('c\n')), int(input('n\n')))
# %% [markdown]
# ex 5-3
# %%
def is_triangle(a, b, c):
    if a>b+c or b>a+c or c>a+b:
        print('No')
    else:
        print('Yes')
# %%
#is_triangle(int(input('a\n')), int(input('b\n')), int(input('c\n')))
# %% [markdown]
# ex 5-4
# __main__
# recurse n -> n, s -> s
# recurse n -> n-1, s -> n+s
# recurse n -> n-2, s -> n-1+2s
# (1) Base case would never be reached and the function would recurse infinitely
# (2) ''' 'recurse' takes args: n, positive integer which determines number of recursions; s, any number which gets added to n - (recursion number) each recursion'''
# %% [markdown]
# ex 5-5
# a semi-fractal tree shape of some sort
# %%
def draw(t, length, n):
    if n==0:
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)
# %%
import turtle
turt = turtle.Turtle()
draw(turt, 50, 5)
