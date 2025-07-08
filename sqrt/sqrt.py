def average(a: float, b: float) -> float:
    return (a + b) / 2

def square(x:float)-> float:
    return x*x

def sqrt(x: float) -> float:

    def is_good_enough(guess: float) -> bool:
        return abs(square(guess) - x) < 0.001

    def improve(guess: float) -> float:
        return average(guess, x / guess)

    def sqrt_iter(guess: float) -> float:
        if is_good_enough(guess):
            return guess
        else:
            return sqrt_iter(improve(guess))

    return sqrt_iter(1.0)

if __name__ == "__main__":
    print(sqrt(1234))
