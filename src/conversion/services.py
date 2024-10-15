from src.conversion import RomanNumeral
from itertools import pairwise


class RomanToIntegerService:
	"""
	Service that converts a valid RomanNumeral object
	into its corresponding integer value.
	"""

	@staticmethod
	def convert(
		roman_numeral: RomanNumeral,
	) -> int:
		"""
		Converts the Roman numeral value object
		into its corresponding integer value.
		"""
		# Convert each Roman numeral character to
		# its integer value
		roman_values = [
			roman_numeral.ROMAN_TO_INT_MAP[char]
			for char in roman_numeral.roman
		]

		# Create pairs of adjacent values,
		# This allows us to compare
		# each value with the next one,
		# including the last value
		adjacent_value_pairs = pairwise(roman_values)
		last_value = roman_values[-1]

		# Calculate the total value using Roman numeral rules:
		# If a smaller value comes before a larger value,
		# subtract it Otherwise, add it to the total
		total = (
			sum(
				-current if current < next_value else current
				for current, next_value in adjacent_value_pairs
			)
			+ last_value
		)

		return total
