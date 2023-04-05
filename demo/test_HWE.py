import pytest

@pytest.fixture()
def setup():
    print("this runs before every method")

def test_def1():
    print("Hello world")
