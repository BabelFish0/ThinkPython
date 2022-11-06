# %% [markdown]
# ch9
# 9-1
# %%
fin = open("C:\\Users\\Jude Young\\Documents\\Coding\\DofE Project Gold\\ThinkPython\\chapter 9\\resources\\words.txt")
for line in fin:
    if len(line.strip()) > 20:
        print(line.strip())