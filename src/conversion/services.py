from src.conversion import RomanNumeral


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
		return roman_numeral.to_integer()
