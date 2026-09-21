import pytest

from src.python_basics import classify_score


def test_high_score():
      assert classify_score(85) == "High"


def test_medium_score():
      assert classify_score(72) == "Medium"


def test_low_score():
      assert classify_score(65) == "Low"


def test_invalid_score():
      with pytest.raises(ValueError):
          classify_score(101)