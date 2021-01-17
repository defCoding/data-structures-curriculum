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

###########################################
# Complete the functions below.
# Once you've done so, write tests to check
# the runtime.
###########################################
def rm_dups_1(ls):
    """
    Removes duplicates from a list in O(n^2) time.
    Method: Check if the item already exists in the list.

    Params:
    ls ([Any]): The list to remove duplicates from.

    Return:
    [Any]: The new list with all duplicates removed.
    """
    pass

def rm_dups_2(ls):
    """
    Removes duplicates from a list in O(nlogn) time.
    Method: Sort the list, then remove duplicates.

    Params:
    ls ([Any]): The list to remove duplicates from.

    Return:
    [Any]: The new list with all duplicates removed.
    """
    pass

def rm_dups_3(ls):
    """
    Removes duplicates from a list in O(n) time.
    Method: Use Python sets.

    Params:
    ls ([Any]): The list to remove duplicates from.

    Return:
    [Any]: The new list with all duplicates removed.
    """
    pass
