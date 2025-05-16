def test_first():
    """An initial test for the app."""
    assert 1 + 1 == 2


from chelseaguo.app import greeting
def test_name():
 assert greeting("Alice") == "Hello, Alice"
def test_empty():
 assert greeting("") == "Hello, stranger"
def test_brutus():
 assert greeting("Brutus") == "BeeWare the IDEs of Python!"
