from fizz import fizzBuzz


def test_fizz_1():
    result = fizzBuzz(1) #input

    assert result == 1  #expected output is 1


def test_fizz_2():
    result = fizzBuzz(2)

    assert result == 2


def test_fizz_3():
    result = fizzBuzz(3)

    assert result == "Fizz"


def test_fizz_6():
    result = fizzBuzz(6)

    assert result == "Fizz"


# write a test for input of numbers 1 -> 15