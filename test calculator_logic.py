import calculator_logic as c



def test_add(): # тестируем программу
    assert c.add(10, 5)==15
    assert c.add(-1, 1)==0
    assert c.add(-2, -2)==-4


def test_subtract():
    assert c.subtract(10, 5)==5
    assert c.subtract(-1, 1)==-2
    assert c.subtract(-10, -10)==0


def test_multiply():
    assert  c.multiply(2,2)==4
    assert  c.multiply(5, -6)==-30
    assert  c.multiply(-1, -5)==5


def test_divide():
    assert c.divide(10, 2)==5
    assert c.divide(-10, 2)==-5
    assert c.divide(-10, -2)==5


test_add()
test_subtract()
test_multiply()
test_divide()
print("тесты пройдены успешно!")



