def right_justify(string:str, n:int) -> str:
    '''justify given string to the nth column from the left'''
    return ' '*(n - len(string)) + string

print(right_justify('test', 10))