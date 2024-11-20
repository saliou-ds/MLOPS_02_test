import sys
import os
# Always run from unit_testing_best_practice/test
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from unit_testing import validate_username, validate_password, validate_email

def test_validate_username():
    assert validate_username("saliou123") == True
    assert validate_username("") == False
    assert validate_username("saliou 123") == False

def test_validate_password():
    assert validate_password("Password1!") == True
    assert validate_password("short1!") == False
    assert validate_password("n0specialchar") == False
    assert validate_password("NoNumber!") == False
    assert validate_password("12345678!") == False

def test_validate_email():
    assert validate_email("saliou123@gmail.com") == True
    assert validate_email("saliou123gmail.com") == False
    assert validate_email("saliou123@gmailcom") == False