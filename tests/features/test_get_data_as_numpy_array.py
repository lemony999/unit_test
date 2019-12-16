import numpy as np
import pytest
from features.as_numpy import get_data_as_numpy_array
# @pytest.mark.xfail
def test_on_clean_file():
  expected = np.array([[2081.0, 314942.0],
                       [1059.0, 186606.0],
  					           [1148.0, 206186.0]
                       ]
                      )
  actual = get_data_as_numpy_array("data/clean/example_clean_data.txt", num_columns=2)
  # Complete your test
  message = ("get_data_as_numpy_array('data/clean/example_clean_data.txt', num_columns=2) return {0} instead of {1}".format(actual, expected))
  assert actual == pytest.approx(expected), message