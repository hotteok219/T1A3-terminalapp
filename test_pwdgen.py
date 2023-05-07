import csv
import pytest
from menu_functions import main_menu, req_menu
from pwd_functions import set_len
from file_functions import add_pwd


# Tests the main_menu() function, where user input is 1, expectation: returns 1.
def test_main_menu_valid(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 1)
    assert main_menu() == 1

# Tests the main_menu() function, where user input is 8, expectation: ValueError.
def test_main_menu_invalid(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 8)
    with pytest.raises(ValueError):
        main_menu()


# Tests the set_len() function, where user input is 6, expectation: returns 6.
def test_set_len_valid(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 6)
    assert set_len() == 6


# Tests set_len() function, where user input is a string "abc", expectation: 
# ValueError and SystemExit (upon completion of looping invalid_attempts)
def test_set_len_invalid(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "abc")
    with pytest.raises(SystemExit):
        with pytest.raises(ValueError):
            set_len()

# Tests the req_menu() function, where user input is 1, expectation: returns 1.
def test_main_menu_valid(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 3)
    assert req_menu() == 3

# Tests the req_menu() function, where user input is 8, expectation: ValueError.
def test_main_menu_invalid(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 7)
    with pytest.raises(ValueError):
        req_menu()

# Tests add_pwd() function, where user input "Password1" is added to the test
# password file, expectation: "Password1" appended to test_pwd_history.csv
test_pwd_filename = "test/test_pwd_history.csv"

def test_add_pwd_valid(monkeypatch):
    original_length = 0
    with open(test_pwd_filename) as test_pf:
        reader = csv.reader(test_pf)
        original_length = sum(1 for row in reader)
    monkeypatch.setattr('builtins.input', lambda _: "Password1")
    add_pwd("Test1", "Password1", test_pwd_filename)
    with open(test_pwd_filename) as test_pf:
        reader = csv.reader(test_pf)
        new_length = sum(1 for row in reader)
    assert new_length == original_length + 1