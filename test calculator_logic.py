import calculator_logic as c
import pytest


def test_add(): # тестируем программу
    assert c.add(10, 5)==15
    assert c.add(-1, 1)==0
    assert c.add(-2, -2)==-4

    with pytest.raises(TypeError):# проработка исключений
        c.add("text", 5)
    with pytest.raises(TypeError):# проработка исключений
        c.add(3, "4")

def test_subtract():
    assert c.subtract(10, 5)==5
    assert c.subtract(-1, 1)==-2
    assert c.subtract(-10, -10)==0

    with pytest.raises(TypeError):# проработка исключений
        c.subtract("text", 5)
    with pytest.raises(TypeError):# проработка исключений
        c.subtract(3, "4")


def test_multiply():
    assert  c.multiply(2,2)==4
    assert  c.multiply(5, -6)==-30
    assert  c.multiply(-1, -5)==5

    #with pytest.raises(TypeError):# можно не прописывать исключение для умножения, т.к. умножать можно и текст на число и ошибки не возникнет
    #    c.multiply("text", 5)
    #with pytest.raises(TypeError):# проработка исключений
    #    c.multiply(3, "4")


def test_divide():
    assert c.divide(10, 2)==5
    assert c.divide(-10, 2)==-5
    assert c.divide(-10, -2)==5

    with pytest.raises(TypeError):# проработка исключений
        c.divide("text", 5)
    with pytest.raises(TypeError):# проработка исключений
        c.divide(3, "4")

    with pytest.raises(ZeroDivisionError):
        c.divide(10, 0)

test_add()
test_subtract()
test_multiply()
test_divide()
print("тесты пройдены успешно!")



