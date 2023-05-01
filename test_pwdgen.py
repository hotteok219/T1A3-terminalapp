import pytest
import csv
from pwd_functions import set_len
from menu_functions import main_menu
from file_functions import add_pwd

def test_set_len_valid(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 6)
    assert set_len() == 6
    
def test_set_len_invalid1(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "abc")
    with pytest.raises(SystemExit):
        with pytest.raises(ValueError):
            set_len()
    
# def test_set_len_invalid2(monkeypatch):
#     monkeypatch.setattr('builtins.input', lambda _: "def")
#     with pytest.raises(ValueError):
#         with pytest.raises(SystemExit):
#             set_len()

    
def test_main_menu_valid(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 1)
    assert main_menu() == 1


def test_main_menu_invalid(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "abc")
    with pytest.raises(ValueError):
        main_menu()

# test_pwd_filename = "test/test_pwd_history.csv"

# def test_add_pwd(monkeypatch):
#     original_length = 0
#     with open(test_pwd_filename) as test_pwd_file:
#         reader = csv.reader(test_pwd_file)
#         original_length = sum(1 for row in reader)
#     monkeypatch.setattr('builtins.input', lambda _: "Password1")
#     add_pwd(test_pwd_file)
#     with open(test_pwd_filename) as test_pwd_file:
#         reader = csv.reader(test_pwd_file)
#         new_length = sum(1 for row in reader)
#     print(original_length)
#     print(new_length)
#     assert new_length == original_length + 1