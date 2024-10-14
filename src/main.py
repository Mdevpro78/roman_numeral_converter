from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from src.conversion import router as conversion_router
from src.conversion import InvalidRomanNumeralValueError

app = FastAPI()


@app.exception_handler(InvalidRomanNumeralValueError)
async def roman_conversion_exception_handler(request: Request, exc: InvalidRomanNumeralValueError) -> JSONResponse:  # noqa: ARG001
	"""Handles exceptions for invalid Roman numeral values."""
	return JSONResponse(
		status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
		content={"detail": "Please enter valid Roman Numeral"},
	)


# Include conversion router under a common prefix
app.include_router(conversion_router, prefix="/api/v1")
