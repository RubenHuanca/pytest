# pip install -U pytest
# pytest testing.py
def func(x):
    return x+1

# Testing
def test_func():
    assert func(3) == 5
    # assert func(3) == 4
