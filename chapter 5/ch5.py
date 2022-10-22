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
#draw(turt, 50, 5)
# %% [markdown]
# ex 5-6
# %%
import random
bound = 0
def koch(t, x):
    if x >= 3:
        koch(t, x/3)
        t.lt(60 + random.uniform(-bound, bound))
        koch(t, x/3)
        t.rt(120 + random.uniform(-bound, bound))
        koch(t, x/3)
        t.lt(60 + random.uniform(-bound, bound))
        koch(t, x/3)
    else:
        t.fd(x)
# %%
#koch(turt, 200)
#turtle.mainloop()
# %%
def snowflake(t, x):
    for edge in range(3):
        koch(t, x)
        t.rt(120)
# %%
#turt.speed(0)
#snowflake(turt, 200)
#turtle.mainloop()
# %% [markdown]
# partially generalise koch curve
# %%
def gen_koch(t, x, s, operator):
    '''
    generate koch curve using:
    recursion count * min segment length 'x',
    min segment length 's'
    turtle object 't',
    and the angle to turn each time 360 / 'operator'.
    '''
    if x >= s:
        gen_koch(t, x/3, s, operator)
        t.lt(180-360/operator)
        for n in range(operator-1):
            gen_koch(t, x/3, s, operator)
            t.rt(360/operator)
        t.lt(180)
        gen_koch(t, x/3, s, operator)
    else:
        t.fd(x)
# %%
turt.speed(0)
turt.color('black')
gen_koch(turt, 250, 5, 5)
turt.penup()
turt.goto(0, 0)
turt.pendown()
turt.color('red')
gen_koch(turt, 250, 150, 5)
turtle.mainloop()
