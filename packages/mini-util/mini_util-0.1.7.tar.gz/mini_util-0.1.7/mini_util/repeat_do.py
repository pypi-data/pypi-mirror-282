"""This module contains a decorator function that repeats a function n times."""

from typing import Callable, List


def repeat_do(n: int = 1) -> Callable:
    """
    Decorator function that repeats a function n times.

    Args:
        n (int): The number of times to repeat the function. Defaults to 1.

    Returns:
        Callable: A wrapper function that can be used to repeat the decorated function.
    """

    def inner(f: Callable) -> Callable:
        """
        Wrapper function that repeats the decorated function n times.

        Args:
            f (Callable): The function to be repeated.

        Returns:
            Callable: A wrapper function that repeats the decorated function n times.
        """

        def wrapper(*args, **kwargs) -> List:
            """
            Wrapper function that repeats the decorated function n times and returns
            the results in a list.

            Args:
                *args: Positional arguments to pass to the decorated function.
                **kwargs: Keyword arguments to pass to the decorated function.

            Returns:
                List: A list containing the results of repeating the decorated function n times.
            """
            ret = [None] * n
            for i in range(n):
                ret[i] = f(*args, **kwargs)
            return ret

        return wrapper

    return inner
