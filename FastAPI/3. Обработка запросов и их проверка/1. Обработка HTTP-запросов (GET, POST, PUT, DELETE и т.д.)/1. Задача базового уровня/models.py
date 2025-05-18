from pydantic import BaseModel, EmailStr, field_validator, Field

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: int = Field(None)
    is_subscribed: bool = Field(None)

    @field_validator("age")
    @classmethod
    def validateAge(cls, value: int) -> int:
        if value < 0:
            raise ValueError("Возраст должен быть положительным числом")
        return value
    