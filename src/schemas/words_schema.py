from pydantic import BaseModel, validator
from typing import List

from src.helpers.enums import Filters


class VowelCountSchema(BaseModel):
    words: List[str]

    @validator('words')
    def check_words(cls, v):
        if not v:
            raise ValueError('words must not be empty')
        for word in v:
            if not isinstance(word, str):
                raise TypeError(f'{word} is not a string')
            if len(word) == 0:
                raise ValueError('Words cannot be empty strings')
        return v


class SortSchema(VowelCountSchema):
    order: Filters
