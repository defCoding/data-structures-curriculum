import timeit

def time_function(func, *args):
    """
    Calculates the runtime of a function with the given arguments in milliseconds.

    Params:
    func (Function): The function to be timed.
    *args ([Any]): The list of arguments to be passed to the function.

    Return:
    Number: The number of milliseconds it took for the function to run.
    """
    return round(timeit.timeit(lambda: func(*args), number=1) * 1000, 3)

################################
# Assume that 'n' is a list.
################################
def linear(n):
    # Create a function that runs in linear time.
    # TODO

def polynomial(n):
    # Create a function that runs in polynomial (n^2) time.
    # TODO
    pass

def logarithmic(n):
    # Create a function that runs in logarithmic time.
    # TODO
    pass

def nlogn(n):
    # Create a function that runs in nlogn time.
    # TODO
    pass
