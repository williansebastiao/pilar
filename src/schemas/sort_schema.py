from pydantic import BaseModel
from typing import List

from src.schemas.vowel_count_schema import VowelCountSchema
from src.helpers.filters import Filters


class SortSchema(VowelCountSchema):
    order: Filters
