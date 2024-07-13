from pydantic import BaseModel
from typing import List

from src.schemas.vowel_count_schema import VowelCountSchema


class SortSchema(VowelCountSchema):
    order: str = 'asc'
