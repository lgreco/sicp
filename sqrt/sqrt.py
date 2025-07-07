def sqrt(x: float) -> float:

    def is_good_enough(guess: float) -> bool:
        return abs(guess * guess - x) < 0.001

    def average(a, b):
        return (a + b) / 2

    def improve(guess):
        return average(guess, x / guess)

    def sqrt_iter(guess):
        if is_good_enough(guess):
            return guess
        else:
            return sqrt_iter(improve(guess))

    return sqrt_iter(1.0)


if __name__ == "__main__":
    print(sqrt(1234))
