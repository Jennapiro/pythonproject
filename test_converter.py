#import pytest for using utilities
import pytest

#import the code to be tested
from converter import ftoin
from converter import intof
#test conversion from feet to inches
def test_ftoin():
	assert ftoin (1) == 12
	assert ftoin (2) == 24
	assert ftoin (3) ==  36
	assert ftoin (4) == 48
	assert ftoin (5) == 60
	assert ftoin (6) == 72 

#test conversion from inches to feet
def test_intof():
	assert intof (20) == pytest.approx(1.67, 0.1)
	assert intof (12) == 1
	assert intof (15) == 1.25
	assert intof (17) == pytest.approx (1.42, 0.1)
	assert intof (24) == 2
	assert intof (18) == 1.5













