def is_odd(number):
#write your code here...
    if number % 2 == 0:
        return False
    else:
        return True

#DO NOT remove lines below here, this is designed to test your code.
def test_is_odd():
    assert is_odd(2) == False
    assert is_odd(3) == True
    assert is_odd(8) == False
    assert is_odd(100) == False
    assert is_odd(101) == True
    print("YOUR CODE IS CORRECT!")
    
test_is_odd()