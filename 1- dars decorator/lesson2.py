def my_decorator(func):
    def inner():

        print("Decorator ishlayabdi")
        func()
        print("Decorator to'xtadi")

    return inner



def my_function():
    print("Function ishlayabdi")


deco = my_decorator(my_function)

deco()