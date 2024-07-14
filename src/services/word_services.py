from src.helpers.enums import Filters
from src.schemas.words_schema import SortSchema
from fastapi.exceptions import HTTPException
from src.helpers.enums import StatusCode


class WordServices:
    """WordsService class"""

    @staticmethod
    def vowel_count(words: dict = None) -> dict:
        """Counts the number of vowels in a given string"""

        if WordServices.__contains_non_string(words):
            raise HTTPException(detail="Not a valid word", status_code=StatusCode.UNPROCESSABLE_ENTITY)

        if len(words) == 0:
            raise HTTPException(detail="Dict is empty", status_code=StatusCode.UNPROCESSABLE_ENTITY)

        response = dict()
        vowels = set('aeiouAEIOU')
        for word in words:
            counter = 0
            for i in range(len(word)):
                if word[i] in vowels:
                    counter += 1
                    response[word] = counter
        return response

    @staticmethod
    def sort(data=SortSchema) -> dict:
        """Sort given data by alphabetical order"""

        body = data.words
        order_by = data.order.value

        if WordServices.__contains_non_string(body):
            raise HTTPException(detail="Not a valid word", status_code=StatusCode.UNPROCESSABLE_ENTITY)

        if len(body) == 0:
            raise HTTPException(detail="Dict is empty", status_code=StatusCode.UNPROCESSABLE_ENTITY)

        reversed = True
        if order_by == Filters.ASCENDING.value:
            reversed = False

        body.sort(reverse=reversed)
        return body


    @staticmethod
    def __contains_non_string(values):
        return any(not isinstance(value, str) for value in values)
