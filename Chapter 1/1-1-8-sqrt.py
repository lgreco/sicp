class SQRT:
    """Class to compute square root using Newton's method using
    recursion instead of loops."""

    _DEFAULT_ERROR = 0.001

    def __init__(self, error: float = _DEFAULT_ERROR) -> None:
        """Initialize the SQRT instance with a specified error tolerance.
        If no error is provided, a default value is used."""
        self._x = 0
        self.error = error

    def _is_good_enough(self, guess: float) -> bool:
        """Check if the current guess is within the acceptable error range."""
        return abs(guess * guess - self._x) < self.error

    def _average(self, a: float, b: float) -> float:
        """Compute the average of two numbers. This is central to
        Newton's method for finding square roots. Explain that
        the denominator below is not a magic number, but rather
        a value from a mathematical formula. Revisit this when
        we cover array to show that even the denominator can be
        parameterized as the length of an array whose elements
        are being averaged."""
        return (a + b) / 2.0

    def _improve(self, guess: float) -> float:
        """Improve the current guess using the average of the guess
        and the value of x / guess."""
        return self._average(guess, self._x / guess)

    def _sqrt_iter(self, guess: float) -> float:
        """Recursively improve the guess until it is good enough.
        This is the core of the recursive algorithm. This process
        is often implemented with a loop, but here we use
        recursion to illustrate the concept. Use of multiple
        returns here is gratuitous, but it does make the
        logic a bit clearer."""
        if self._is_good_enough(guess):
            # Base case: guess is good enough, we are done!
            return guess
        else:
            # Make an improved guess and try again.
            return self._sqrt_iter(self._improve(guess))

    def sqrt(self, x: float) -> float:
        """Public method to compute the square root of x."""
        self._x = x
        # Start the iteration with an initial guess of 1.0
        return self._sqrt_iter(1.0)


# Simple demonstration and test of the SQRT class.
if __name__ == "__main__":
    demo = SQRT()
    print("\033[2J", end="")
    print("\nTest       Newton's         Actual")
    print("   x       sqrt(x)          sqrt(x)")
    print("-" * 40)
    for num in [4, 2, 10, 1234]:
        print(f"{num:-4d}      {demo.sqrt(num):9.6f}       {num**0.5:9.6f}")
    print("-" * 40, end="\n\n")