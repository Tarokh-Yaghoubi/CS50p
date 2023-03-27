from hello import hello

'''
    A test for the hello() function 

'''

def test_hello_david():
    assert hello("David") == "Hello David"
    
def test_hello_tarokh():
    assert hello("Tarokh") == "Hello Tarokh"
    assert hello("tarokh") == "Hello tarokh"
    
def test_hello_default():
    assert hello() == "Hello Someone"
        