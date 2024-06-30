from asimplepypackageformmik import greet

def test_greet():
    assert greet("World") == "Hello, World!"

def test_greet_name():
    assert greet("Alice") == "Hello, Alice!"
