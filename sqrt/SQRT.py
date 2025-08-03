class SQRT:

    def __init__(self, error: float = 0.001) -> None:
        self._x = 0
        self.error = error

    def _is_good_enough(self, guess: float) -> bool:
        return abs(guess * guess - self._x) < self.error

    def _average(self, a: float, b: float) -> float:
        return (a + b) / 2.0

    def _improve(self, guess: float) -> float:
        return self._average(guess, self._x / guess)

    def _sqrt_iter(self, guess: float) -> float:
        if self._is_good_enough(guess):
            return guess
        else:
            return self._sqrt_iter(self._improve(guess))

    def sqrt(self, x):
        self._x = x
        return self._sqrt_iter(1.0)

if __name__ == "__main__":
    demo = SQRT()
    for num in [4, 2, 10, 1234]:
        print(f"√{num:-4d} ≈ {demo.sqrt(num):7.4f}")
