import re
from pydantic import BaseModel, EmailStr, Field, field_validator

class Contact(BaseModel):
    email: EmailStr
    phone: str = Field(None, min_length=7, max_length=15)

    @field_validator("phone")
    @classmethod
    def validatePhoneNumber(cls, value: str) -> str:
        if value is not None:
            if not value.isdigit():
                raise ValueError("Номер телефона должен состоят только из цифр")
        return value
    
class Feedback(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    message: str = Field(min_length=10, max_length=500)
    contact: Contact

    @field_validator("message")
    @classmethod
    def validateBadWords(cls, values: str) -> str:
        badWords = ["редиск", "бяк", "козявк"]
        for wordBase in badWords:
            if re.search(rf"\b{wordBase}[а-я]*\b", values):
                raise ValueError("Использованы недопустимые слова")
        return values
    