import pytest
import csv
from pwd_functions import set_len
from file_functions import add_pwd

# Tests the set_len() function, where user input is 6, expectation: set_len returns 6.
def test_set_len_valid(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 6)
    assert set_len() == 6

# Tests the set_len() function, where user input is a string "abc", expectation: ValueError and SystemExit (after looping of invalid_attempts is complete)
def test_set_len_invalid(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "abc")
    with pytest.raises(SystemExit):
        with pytest.raises(ValueError):
            set_len()

# Tests the add_pwd() function, where user input "Password1" is added to the test_pwd_history.csv file, expectation: "Password1" added/appended to test_pwd_history.csv
test_pwd_filename = "test/test_pwd_history.csv"

def test_add_pwd_valid(monkeypatch):
    original_length = 0
    with open(test_pwd_filename) as test_pwd_file:
        reader = csv.reader(test_pwd_file)
        original_length = sum(1 for row in reader)
    monkeypatch.setattr('builtins.input', lambda _: "Password1")
    add_pwd("Password1", "Test1", test_pwd_filename)
    with open(test_pwd_filename) as test_pwd_file:
        reader = csv.reader(test_pwd_file)
        new_length = sum(1 for row in reader)
    assert new_length == original_length + 1