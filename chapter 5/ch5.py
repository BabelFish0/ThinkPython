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
print(days + " days, " + hours + " hours, " + minutes + " minutes and " + seconds + " seconds since the epoch.")
# %% [markdown]
# ex 5-2
# %%
def check_fermat(a, b, c, n):
    if n > 2 and a^n + b^n == c^n:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work.")
# %%
check_fermat(int(input('a\n')), int(input('b\n')), int(input('c\n')), int(input('n\n')))
# %% [markdown]
# ex 5-3
# %%
