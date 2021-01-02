# tests reduce bugs in existing code
# ensure that the bugs that are fixed, stay fixed
# ensure new features dont break old ones
# ensure that cleaning up code doesnt introduce new bugs
# red green refactor steps
# write a test that fails
# write minimal amount of code necessary to make test pass
# clean up the code while ensuring the tests still pass

#Assertions:
#assert accepts expresions and returns none if truth an assertion error if falsy
#accepts optioal error message as second argument

def add_positive_numbers(x,y):
    assert x > 0 and y > 0, "Both numbers are positive"
    return x + y
print(add_positive_numbers(1,1))
#add_positive_numbers(-1,2) # gets error
# cannot depend on assert all the time because of the -O flag

# DOctests:
# can write tests for functions inside docstring """ """

def add(a,b):
    """ 
    >>> add(2,3)
    5
    >>> add(100,200)
    300
    """
    return a + b
# testing always expects single quotes
# if theres white space in the expected value, it will cause an error
# order matters in doctests
if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
# for errors:
# Traceback (most recent call last):
#     ...
# TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
# unit testing, test smallest parts of applications
# individual classes, modules or functions
# bad unit testing: whole pplications, dependencies across several classes or modules
# built in moduleunittest
#unittest.TestCase

# class ActivityTests(unittest.TestCase):
#     def test_eat_healthy(self):
#         """ can put docstring for these testing functions"""
#         self.assertEqual(
#             eat("broccoli",is_healthy=True),
#             "I'm eating broccoli because my body is a temple"
#         )
#     def test_eat_unhealthy(self)    
#         self.assertEqual(
#             eat("pizza",is_healthy=False),
#             "I'm eating pizza because YOLO"
#         )
# if __name__ == "__main__":
#     unittest.main()
#assertFalse checks to see if it is false, checks for falsy 
# assertTrue checks for truthy, can have multiple tests in a single test function
# assert is(not) None
#assert(Not)Equal
#assertIn, use a tuple to see if any of the returns is one of the values in the tuple
# assertRaises(): put code underneath to test for the error case
# setUp used to reset the variable that you want to test
