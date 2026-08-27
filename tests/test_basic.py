from test_with_zoe import hello


def test_hello_default():
    assert hello() == "Hello, world!"


def test_hello_name():
    assert hello("Zoe") == "Hello, Zoe!"
