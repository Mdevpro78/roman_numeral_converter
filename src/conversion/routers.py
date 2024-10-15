from fastapi import Depends
from src.conversion import APIRouter

from src.conversion import RomanToIntegerService
from src.conversion import (
	RomanRequestDTO,
	RomanResponseDTO,
)
from src.conversion import RomanNumeral
from src.conversion import (
	InvalidRomanNumeralValueError,
)


router = APIRouter()


# Dependency to get the RomanToIntegerService
def get_roman_to_integer_service() -> RomanToIntegerService:
	"""Instantiate and return the RomanToIntegerService."""
	return RomanToIntegerService()


@router.post(
	"/convert",
	response_model=RomanResponseDTO,
)
async def convert_roman_to_integer(
	request: RomanRequestDTO,
	service: RomanToIntegerService = Depends(
		get_roman_to_integer_service,
	),
) -> RomanResponseDTO:
	"""Convert a Roman numeral to an integer.

	Args:
	request (RomanRequestDTO):
	The request containing the Roman numeral.

	service (RomanToIntegerService):
	The service to perform the conversion.

	Returns:
	RomanResponseDTO:
	The response containing the integer value.

	"""
	try:
		result = service.convert(
			RomanNumeral(
				roman=request.roman_numeral,
			),
		)
		return RomanResponseDTO(
			integer_value=result,
		)
	except ValueError as e:
		raise InvalidRomanNumeralValueError(
			message=str(e),
		)
