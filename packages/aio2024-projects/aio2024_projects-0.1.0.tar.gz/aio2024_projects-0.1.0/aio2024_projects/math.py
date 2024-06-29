class MyMath:
    def __init__(self, value: int) -> None:
        self._value = value
    def factorial(self) -> int:
        if self._value == 0:
            return 1
        else:
            return self._value * MyMath(self._value - 1).factorial()


n = 4
fact_n = MyMath(n).factorial()
print(f"Factorial of {n} is {fact_n}")
