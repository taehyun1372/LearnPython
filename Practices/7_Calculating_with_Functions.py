def zero(func=None): return 0 if func is None else func(func(), 0) #your code here
def one(func=None): return 1 if func is None else func(func(), 1) #your code here
def two(func=None): return 2 if func is None else func(func(), 2) #your code here
def three(func=None): return 3 if func is None else func(func(), 3) #your code here
def four(func=None): return 4 if func is None else func(func(), 4) #your code here
def five(func=None): return 5 if func is None else func(func(), 5) #your code here
def six(func=None): return 6 if func is None else func(func(), 6) #your code here
def seven(func=None): return 7 if func is None else func(func(), 7) #your code here
def eight(func=None): return 8 if func is None else func(func(), 8) #your code here
def nine(func=None): return 9 if func is None else func(func(), 9) #your code here

def plus(right, left=None): return right if left is None else left + right #your code here
def minus(right, left=None): return right if left is None else left - right #your code here
def times(right, left=None): return right if left is None else left * right #your code here
def divided_by(right, left=None): return right if left is None else left / right #your code here

print(seven(times(five())))
print(seven(times(five())))
print(seven(times(five())))
