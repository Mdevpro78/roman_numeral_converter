import re
from typing import ClassVar
from itertools import pairwise

from src.conversion import (
	ConfigDict,
	BaseModel,
	field_validator,
)
from src.conversion import (
	InvalidRomanNumeralValueError,
)


class RomanNumeral(BaseModel):
	"""
	Roman numeral value object responsible for
	validating and representing a Roman numeral.
	"""

	roman: str
	ROMAN_REGEX: ClassVar[re.Pattern] = re.compile(
		r"^M{0,3}(?:CM|CD|D?C{0,3})(?:XC|XL|L?X{0,3})(?:IX|IV|V?I{0,3})$",
	)
	ROMAN_TO_INT_MAP: ClassVar[dict] = {
		"I": 1,
		"V": 5,
		"X": 10,
		"L": 50,
		"C": 100,
		"D": 500,
		"M": 1000,
	}

	model_config = ConfigDict(frozen=True)

	@field_validator("roman")
	@classmethod
	def validate_roman(
		cls: type["RomanNumeral"],
		roman: str,
	) -> str:
		"""Ensures the input is a valid Roman numeral."""
		roman = roman.strip().upper()
		if not (roman.isalpha() and cls.ROMAN_REGEX.match(roman)):
			raise InvalidRomanNumeralValueError(
				"Input contains invalid Roman numeral characters or sequences.",
			)

		return roman

	def to_integer(self) -> int:
		"""
		Converts the Roman numeral value object
		into its corresponding integer value.
		"""
		# Convert each Roman numeral character to
		# its integer value
		roman_values = [
			self.ROMAN_TO_INT_MAP[char] for char in self.roman
		]

		# Create pairs of adjacent values
		adjacent_value_pairs = pairwise(roman_values)
		last_value = roman_values[-1]

		# Calculate the total value using Roman numeral rules:
		# If a smaller value comes before a larger value,
		# subtract it, otherwise add it to the total
		total = (
			sum(
				-current if current < next_value else current
				for current, next_value in adjacent_value_pairs
			)
			+ last_value
		)

		return total
