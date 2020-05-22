import time
"""Python supports function decoration using decorators, which look like annotations on functions. Python also treats functions as first class citizens
which means they can be treated like variables and passed to functions and assigned to references.

Below are two examples, one which harnesses pythons ability to pass a function into a function as an argument, and the other using pythons
out of the box decorator syntax.
"""
def add(a, b):
    return a + b

def add_with_logging(add_func, a, b):
    now = time.time()
    print("[INFO] About to start calculation")
    value = add_func(a, b)
    print("[INFO] Calculation complete")
    after = now = time.time()
    print(f"[INFO] Took {after - now} seconds")

    return value

def add_with_logging_decorator(f):
    def inner(*args):
        now = time.time()
        print("[INFO] About to start calculation")
        value = f(*args)
        print("[INFO] Calculation complete")
        after = now = time.time()
        print(f"[INFO] Took {after - now} seconds")
    
        return value
    return inner

@add_with_logging_decorator
def add_to_decorate(a, b):
    return a + b

if __name__ == "__main__":
    value = add(10, 20)
    print(value, end="\n\n")

    value = add_with_logging(add, 100, 200)
    print(value, end="\n\n")

    value = add_to_decorate(1000, 2000)
    print(value, end="\n\n")