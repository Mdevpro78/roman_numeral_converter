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

	ROMAN_TO_INT_MAP: ClassVar[dict] = {
		"I": 1,
		"V": 5,
		"X": 10,
		"L": 50,
		"C": 100,
		"D": 500,
		"M": 1000,
	}
	NON_REPEATING: ClassVar[set] = {"V", "L", "D"}
	VALID_SUBTRACTIVE_COMBINATIONS: ClassVar[set] = {
		"IV",
		"IX",
		"XL",
		"XC",
		"CD",
		"CM",
	}
	model_config = ConfigDict(frozen=True)

	@field_validator("roman")
	@classmethod
	def validate_roman(
		cls: type["RomanNumeral"],
		roman: str,
	) -> str:
		"""Ensures the input is a valid Roman numeral."""
		roman = roman.upper()
		if not cls._is_valid_roman(roman):
			raise InvalidRomanNumeralValueError(
				"Input contains invalid Roman numeral characters or sequences.",
			)
		return roman

	@classmethod
	def _is_valid_roman(
		cls: type["RomanNumeral"],
		roman: str,
	) -> bool:
		"""Validates the Roman numeral string."""
		return (
			roman.isalpha()
			and all(c in cls.ROMAN_TO_INT_MAP for c in roman)
			and not cls._has_invalid_repetitions(
				roman,
			)
			and not cls._has_invalid_subtractive_combinations(
				roman,
			)
		)

	@staticmethod
	def _has_invalid_repetitions(
		roman: str,
	) -> bool:
		"""
		Checks for invalid repetitions in
		the Roman numeral string.
		"""
		if any(
			char * 2 in roman
			for char in RomanNumeral.NON_REPEATING
		):
			return True
		return any(char * 4 in roman for char in "IXCM")

	@staticmethod
	def _has_invalid_subtractive_combinations(
		roman: str,
	) -> bool:
		"""
		Checks for invalid subtractive combinations and
		ordering.
		"""
		max_repeats = {
			"I": 3,
			"X": 3,
			"C": 3,
			"M": 3,
			"V": 1,
			"L": 1,
			"D": 1,
		}
		repeat_count, prev_char = 0, ""

		for current, next_char in pairwise(roman):
			# Check for invalid ordering and repetition limits
			if current == prev_char:
				repeat_count += 1
				if repeat_count > max_repeats.get(
					current,
					1,
				):
					return True
			else:
				repeat_count = 1

			# Check for invalid subtractive combinations
			if RomanNumeral.ROMAN_TO_INT_MAP[
				current
			] < RomanNumeral.ROMAN_TO_INT_MAP[next_char] and (
				current + next_char
				not in RomanNumeral.VALID_SUBTRACTIVE_COMBINATIONS
				or repeat_count > 1
			):
				return True

			prev_char = current

		return False

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
