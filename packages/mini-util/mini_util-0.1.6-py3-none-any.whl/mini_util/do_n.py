def do_n(n: int):
    """
    Do function n times

    Args
        n (int): the number you want to repeat
    """
    def inner(f):
        def wrapper(*args, **kwargs):
            ret = [None] * n
            for i in range(n):
                ret[i] = f(*args, **kwargs)

        return wrapper

    return inner



class DoN:
    @staticmethod
    def do_n(n: int):
        """
        Do function n times

        Args
            n (int): the number you want to repeat
        """
        def inner(f):
            def wrapper(*args, **kwargs):
                ret = [None] * n
                for i in range(n):
                    ret[i] = f(*args, **kwargs)

            return wrapper

        return inner
