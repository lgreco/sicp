def expt_recursive(b: float, n: int) -> float:
    """Recursive computation of b^b = b * ^(n-1) with base
    case b^0 = 1

    Args:
        b (float): base to exponentiate
        n (int): exponent

    Returns:
        float: b^n
    """
    if n == 0:
        # base case, b^0 = 1
        return 1
    else:
        # recurse b*b^(n-1)
        return b * expt_recursive(b, n - 1)
    # end method expt


def expt_tail_recursive(b: float, counter: int, product: float) -> float:
    """Tail recursion for b^n"""
    if counter == 0:
        return product
    else:
        return expt_tail_recursive(b, counter - 1, b * product)
    # end method expt_iterative


def expt_tail_helper(b: float, n: int) -> float:
    """Helper method to kick start tail recursion"""
    return expt_tail_recursive(b, n, 1)
    # end method expt_tail_helper


def expt_iter(b: float, n: int) -> float:
    product = 1
    for i in range(n):
        product *= b
    return product
    # end method expt_iter


def square(x: float) -> float:
    return x * x


def is_even(n: int) -> bool:
    return n % 2 == 0


def expt_fast(b: float, n: int) -> float:
    if n == 0:
        return 1
    else:
        return square(expt_fast(b, n // 2)) if is_even(n) else b * expt_fast(b, n - 1)
