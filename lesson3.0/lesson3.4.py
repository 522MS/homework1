def my_func(x, y):
    return x ** y

print(my_func(5, -2))

# 2й способ

def my_func1(x, y):
    for i in range(abs(y) - 1):
        x *= x
    return 1 / x

print(my_func1(5, -2))



