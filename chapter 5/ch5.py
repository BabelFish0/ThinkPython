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