from bank import check

def test_options():
    assert check("hello Tarokh") == "$0"
    assert check("hey Tarokh") == "$20"
    assert check("Jesus Tarokh") == "$100"
    assert check("Hello Tarokh") == "$0"