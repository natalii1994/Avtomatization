from calculator import Calculator

calculator = Calculator()

res = calculator.sum(4, 5)
assert res == 9

res = calculator.sum(-2, -7)
assert res == -9

res = calculator.sum(2, -7)
assert res == -5

res = calculator.sum(2.5, 0.75)
assert res == 3.25

res = calculator.sum(2, 0)
assert res == 2

res = calculator.div(10, 2)
assert res == 5

