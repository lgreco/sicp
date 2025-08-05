def cube(x: float) -> float:
    """Returns the cube of x. Superfluous, really, since it's used only once
    but I keep it here for consistency with the code in SICP.
    """
    return x * x * x
    # end method cube


def p(x: float) -> float:
    """Kernel for the trigonometric identity
    sin(x) = 3*sin(x/3)-4*sin^3(x/3).
    Also superfluous, but here for consistency with SICP.
    """
    return 3 * x - 4 * cube(x)
    # end method px


def sine(angle: float) -> float:
    """Computes the sine of a value using the approximation
    sin(x) = x when x <= 0.1 radians

    For values of x > 0.1, the following identity is applied repeatedly
    (recursively) until x is reduced to a value below 0.1 radians.

    sin(x) = 3*sin(x/3)-4*sin^3(x/3)

    This requires approximately x/log3 divisions, so we can write
    that the method is in \Theta(x).
    """
    if abs(angle) > 0.1:
        return p(sine(angle / 3))
    else:
        return angle
    # end method sine


import math  # for testing

test_angle = 12.5
print(sine(test_angle))  # our approximation
print(math.sin(test_angle))  # python's built-in sin
