import re
from pydantic import BaseModel, Field, field_validator

class Feedback(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    message: str = Field(min_length=10, max_length=500)

    @field_validator("message")
    @classmethod
    def validateBadWords(cls, values: str) -> str:
        badWords = ["редиск", "бяк", "козявк"]
        for wordBase in badWords:
            if re.search(rf"\b{wordBase}[а-я]*\b", values):
                raise ValueError("Использование недопустимых слов")
        return values
