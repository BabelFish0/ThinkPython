# %% [markdown]
# chapter 5
# ex 5-1
# %%
import time

def convert(conversion, value):
    return value // conversion

seconds = time.time() % 60
minutes = convert(60, time.time()) % 60
hours = convert(60*60, time.time()) % 24
days = convert(60*60*24, time.time())
# %%
print(days + " days, " + hours + " hours, " + days + " days " + " seconds since the epoch.")