import sys
import os
# Always run from unit_testing_best_practice/test
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from sample import *

def test_answer():
    assert func(3) == 4