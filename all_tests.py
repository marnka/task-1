import pytest
from dumb_code import addition

def test_1():
  result = addition(5, 3)
  print(f"Результат додавання: {result}")
  assert result == 8


if __name__ == "__main__":
  test_1()

def test_2():
  result = addition(5, -3)
  print(f"Результат додавання: {result}")
  assert result == 2

if __name__ == "__main__":
  test_2()


def test_3():
  result = addition(-5, -3)
  print(f"Результат додавання: {result}")
  assert result == -8

if __name__ == "__main__":
  test_3()
