def test_to_str():
    assert to_str(True) == "true"
    assert to_str(False) == "false"
    assert to_str(None) == "null"
    assert to_str(123) == "123"
    assert to_str("hello") == "hello"
