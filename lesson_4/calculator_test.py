from calculator import Calculator

calculator = Calculator()

def test_sum_positive_nums():
    calculator = Calculator()
    res = calculator.sum(4, 5)
    assert res == 9

def test_sum_negative_nums():
    calculator = Calculator()
    res = calculator.sum(-2, -7)
    assert res == -9

def test_sum_positive_and_negative_nums():
    calculator = Calculator()
    res = calculator.sum(2, -7)
    assert res == -5

def test_sum_float_nums():
    calculator = Calculator()
    res = calculator.sum(2.5, 0.75)
    assert res == 3.25

def test_sum_zero_nums():
    calculator = Calculator()
    res = calculator.sum(2, 0)
    assert res == 2

def test_div_positive():
    calculator = Calculator()
    res = calculator.div(10, 2)
    assert res == 5

def test_div_by_zero():
    calculator = Calculator()
    res = calculator.div(10, 0)
    assert res == None

def test_avg_empty_list():
    calculator = Calculator()
    numbers =[]
    res = calculator.avg(numbers)
    assert res == 0

def test_avg_positive():
    calculator = Calculator()
    numbers =[1,2,3,4,5,6,7,8,9,5]
    res = calculator.avg(numbers)
    assert res == 5
