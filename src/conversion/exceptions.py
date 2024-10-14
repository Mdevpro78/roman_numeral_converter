class RomanNumeralError(Exception):
	"""Base exception for Roman numeral conversion errors."""

	pass


class InvalidRomanNumeralValueError(RomanNumeralError, ValueError):
	"""Raised when the input string contains invalid Roman numeral characters."""

	def __init__(self, message: str = "Input contains invalid Roman numeral characters.") -> None:  # noqa: D107
		self.message = message
		super().__init__(self.message)
