import time

def log_exec_func(func):
  #Implements and return wrapper function
    def wrapper(*args, **kwargs):
    #This function implements additional functionalities wrapping to original function
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"The execution time of {func.__name__} is {end - start}")
        return result
    return wrapper
@log_exec_func
def prepare_dish(name):
    print(f"cooking {name}")
    time.sleep(2)
    print(f"Dish {name} is prepared")

prepare_dish("Maggie")