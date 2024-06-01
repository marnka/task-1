import pytest
from dumb_code import addition

@pytest.mark.parametrize(
    "a, b, expected_result", [
        (5, 3, 8),
        (5, -3, 2),
        (-5, -3, -8),
    ]
)
def test_addition(a, b, expected_result):
    result = addition(a, b)
    print(f"Результат додавання: {result}")
    assert result == expected_result
