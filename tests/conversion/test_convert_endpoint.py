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


# Test invalid types (non-string input)
@pytest.mark.parametrize(
	"invalid_input",
	[
		123,  # Integer not allowed
		5.67,  # Float not allowed
		None,  # None not allowed
		[],  # List not allowed
		{},  # Dictionary not allowed
		("IV", "V"),  # Tuple not allowed
	],
)
def test_invalid_numeral_type(invalid_input) -> None:
	"""Test case for handling invalid numeral types, just string type is valid."""
	response = client.post(_endpoint, json={"roman_numeral": invalid_input})
	assert response.status_code == 422  # Unprocessable Entity for validation errors


# Test invalid Roman numeral characters
@pytest.mark.parametrize(
	"invalid_roman",
	[
		"IIII",  # Invalid repetition (although accepted in some systems)
		"VV",  # Invalid repetition of 'V'
		"VVIII",  # Invalid repetition and combination
		"A",  # Invalid character 'A'
		"IIX",  # Invalid ordering
		"IIIX",  # Invalid ordering
		"IOO",  # Invalid character 'O'
		"ABCD",  # Invalid character range
		"MMXYZ",  # Mixed valid and invalid chars
	],
)
def test_invalid_roman_numerals(invalid_roman) -> None:
	"""
	Test case for invalid Roman numeral inputs,
	in case of invalid ordering and repetition.
	"""
	response = client.post(_endpoint, json={"roman_numeral": invalid_roman})
	assert response.status_code == 422  # Unprocessable Entity for validation errors
