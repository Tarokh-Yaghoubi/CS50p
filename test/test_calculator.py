from calculator import square

'''

    A test for the calculator program , square() function

'''

def test_positive():        
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9 
    
def test_zero():     
    assert square(0) == 0
