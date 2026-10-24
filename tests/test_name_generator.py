import pytest
from name_generator import *
from data.drow_name_data import drow

def test_make_name_combines_prefix_and_suffix():
    result = make_name("Zil", "ra")

    assert result == "Zilra"


def test_get_dic_choice_returns_valid_prefix():
    result = get_dic_choice(drow, "female", "prefixes")

    assert result in drow["female"]["prefixes"]


def test_get_dic_choice_returns_valid_suffix():
    result = get_dic_choice(drow, "female", "suffixes")

    assert result in drow["female"]["suffixes"]


def test_make_definition_returns_correct_meanings():
    result = make_definition(
        drow, "female", "prefixes", "Akor"
    )

    assert result == ["beloved", "best", "first"]


def test_get_dic_choice_rejects_invalid_category():
    with pytest.raises(KeyError):
        get_dic_choice(drow, "female", "invalid_category")
