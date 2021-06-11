def foo():
    global x,y
    x = 3
    y = 5

    def bar():
        x = 5
        return

    bar()
    print(x)
    return

x = 2
foo()
print(y)
