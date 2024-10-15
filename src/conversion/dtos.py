from src.conversion import BaseModel


class RomanRequestDTO(BaseModel):
	"""DTO for Roman numeral input data."""

	roman_numeral: str


class RomanResponseDTO(BaseModel):
	"""
	DTO for representing the integer value of
	a Roman numeral conversion.
	"""

	integer_value: int
