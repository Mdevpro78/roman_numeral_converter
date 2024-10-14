import roman
import pytest
from fastapi.testclient import TestClient

from src.main import app  # Assuming you have a FastAPI app defined

client = TestClient(app)

_endpoint = "/api/v1/convert"


# Test valid Roman numerals
@pytest.mark.parametrize("roman, expected", [(roman.toRoman(_int), {"integer_value": _int}) for _int in range(1, 3999)])
def test_valid_roman_numerals(roman, expected) -> None:
	"""Test the conversion of valid Roman numerals to integers."""
	response = client.post(_endpoint, json={"roman_numeral": roman})  # Adjust endpoint as necessary
	assert response.status_code == 200
	assert response.json() == expected
