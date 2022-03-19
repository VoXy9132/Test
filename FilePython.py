def generator(arg1, arg2):
    return (temp for i in range(arg1, arg2))
print(list(generator(1, 10)))
