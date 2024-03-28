from dumb_code import addition

def test_2():
    result = addition(5, -3)
    print(f"Результат додавання: {result}")
    assert result == 2

if __name__ == "__main__":
    test_2()