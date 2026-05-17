def my_decorator(func):
    print('outer start')
    def wrapper():
        print("Before the function runs")
        func()
        print("After the function runs")
    print('outer end')
    return wrapper






@my_decorator
#say_hello = my_decorator(say_hello)

def say_hello():
    print("Hello, world!")


say_hello()
