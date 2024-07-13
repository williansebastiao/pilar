from typing import List

from pydantic import BaseModel, root_validator


class VowelCount(BaseModel):
    words: List[str]


    @root_validator(pre=True)
    def validate_words(cls, values):
        if values.get('words') is None:
            raise ValueError("'words' is a required property!!!!")
        # if not isinstance(values, str):
        #     raise ValueError("'words' is a required property")
        return values
