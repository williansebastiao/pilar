from src.helpers.enums import Filters
from src.schemas.words_schema import SortSchema


class WordServices:
    """WordsService class"""

    @staticmethod
    def vowel_count(words=dict) -> dict:
        """Counts the number of vowels in a given string"""
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

        reversed = True
        if order_by == Filters.ASCENDING.value:
            reversed = False

        body.sort(reverse=reversed)
        return body
