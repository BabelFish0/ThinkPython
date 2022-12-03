# %% [markdown]
# ch7
# p78
# %%
def print_n(s, n): #an iterative version of p52 func
    while n > 0:
        print(s)
        n -= 1
print_n('hello', 3)
# %% [markdown]
# ex 7-1
# %%
import math
def mysqrt(a):
    epsilon = 0.0000001
    y = 0
    x = 3
    while True:
        y = (x + a/x)/2
        if abs(x-y) < epsilon:
            return y
        x = y
# %%
def test_square_root(start, end):
    for test_value in range(int(start), int(end+1)):
        print(test_value, mysqrt(test_value), math.sqrt(test_value), abs(mysqrt(test_value)-math.sqrt(test_value)))
# %%
test_square_root(1.0, 9.0)
# %% [markdown]
# ex 7-2
def eval_loop():
    while True:
        string_in = input('>>> ')
        if string_in == 'done':
            break
        print(eval(string_in))
# %%
#eval_loop()
# %% [markdown]
# ex 7-3
# %%
def estimate_pi():
    k = 0
    total = 0
    factor = 2 * mysqrt(2) / 9801
    while True:
        fract = math.factorial(4*k) * (1103 + 26390*k) / (math.factorial(k)**4 * 396**(4*k))
        
        term = factor*fract
        total += fract
        
        if abs(term) < 1e-15:
            break
        k += 1
    
    return 1 / (factor*total)
# %%
print(estimate_pi())
    