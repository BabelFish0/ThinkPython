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
for line in fin:
    if has_no_e(line.strip()):
        print(line.strip())