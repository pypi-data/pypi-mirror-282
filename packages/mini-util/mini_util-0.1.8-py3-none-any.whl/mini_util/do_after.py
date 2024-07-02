"""This module contains functions that can be used to do some actions after some time."""

from time import sleep
from typing import Any, Callable


def do_after(n: int = 0) -> Callable:
    """
    do_after(n) returns a function that executes f n seconds after the function

    Args:
        n (int): number of seconds to sleep. Default is 0

    Returns:
        Callable: a function that executes f n seconds after the function
    """

    def inner(f: Callable) -> Callable:
        """
        inner(f) executes f n seconds after the function

        Args:
            f (Callable): function to execute

        Returns:
            Callable: a function that executes f n seconds after the function
        """

        def wrapper(*args, **kwargs) -> Any:
            """
            wrapper(*args, **kwargs) executes f n seconds after the function
            """
            sleep(n)
            ret = f(*args, **kwargs)
            return ret

        return wrapper

    return inner
