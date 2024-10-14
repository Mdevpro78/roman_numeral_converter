from src.conversion import BaseModel


# Request DTO: Defines the expected structure of the input data (Roman numeral)
class RomanRequestDTO(BaseModel):
	"""DTO for Roman numeral input data."""

	roman_numeral: str


# Response DTO: Defines the output of the conversion (integer value corresponding to the Roman numeral)
class RomanResponseDTO(BaseModel):
	"""DTO for representing the integer value of a Roman numeral conversion."""

	integer_value: int
