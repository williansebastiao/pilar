import pytest
from fastapi.exceptions import HTTPException
from pydantic import ValidationError
from src.helpers.enums import StatusCode
from src.schemas.words_schema import SortSchema
from src.services.word_services import WordServices


def test_should_return_total_all_vowel():
    my_list = ["batman", "robin", "coringa"]
    total_vowel = {"batman": 2, "robin": 2, "coringa": 3}

    service = WordServices()
    response = service.vowel_count(my_list)
    assert response == total_vowel


def test_should_return_exception_if_have_int():
    my_list = ["batman", "robin", 1]

    service = WordServices()

    with pytest.raises(HTTPException) as error:
        service.vowel_count(my_list)

    assert error.value.detail == "Not a valid word"
    assert error.value.status_code == StatusCode.UNPROCESSABLE_ENTITY


def test_should_return_exception_if_not_have_data():
    my_list = []

    service = WordServices()

    with pytest.raises(HTTPException) as error:
        service.vowel_count(my_list)

    assert error.value.detail == "Dict is empty"
    assert error.value.status_code == StatusCode.UNPROCESSABLE_ENTITY


def test_should_return_list_sorted_as_asc():
    my_dict = SortSchema(words=["batman", "robin", "coringa"], order="asc")
    sorted_dict = ["batman", "coringa", "robin"]

    service = WordServices()
    response = service.sort(my_dict)
    assert response == sorted_dict


def test_should_return_list_sorted_as_desc():
    my_dict = SortSchema(words=["batman", "robin", "coringa"], order="desc")
    sorted_dict = ["robin", "coringa", "batman"]

    service = WordServices()
    response = service.sort(my_dict)
    assert response == sorted_dict

def test_not_should_return_list_sorted_if_has_int():
    my_dict = {"words": ["batman", "robin", "coringa", 1], "order": "asc"}

    with pytest.raises(ValidationError) as error:
        SortSchema(**my_dict)

    assert "Input should be a valid string" in str(error.value)


def test_not_should_return_exception_if_has_not_data_in_sort():
    my_dict = {"words": [], "order": "asc"}

    with pytest.raises(ValidationError) as error:
        SortSchema(**my_dict)

    assert "Value error, words must not be empty" in str(error.value)
