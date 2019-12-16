import pytest
from data.preprocessing_helpers import convert_to_int

def test_convert_to_int(): 
    assert convert_to_int("2,081") == 2081
	

