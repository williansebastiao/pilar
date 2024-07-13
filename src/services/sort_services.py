from src.schemas.sort_schema import SortSchema
from src.helpers.filters import Filters
class SortServices:


    @staticmethod
    def sort(data=SortSchema) -> dict:
        body = data.words
        order_by = data.order.value

        reversed = True
        if order_by == Filters.ASCENDING.value:
            reversed = False

        body.sort(reverse=reversed)
        return body
