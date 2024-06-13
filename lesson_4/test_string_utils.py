import pytest
from string_utils import StringUtils

string_utils = StringUtils()

@pytest.mark.parametrize('string,result',('skypro','Skypro'), ('123','123'), ('hi mi name is Natali','Hi mi name is Natali'),('',''), (' ',' '), ('123456опана','123456опана'))
def first_capital_letter(string, result):
   string_utils = StringUtils()
   res =  string_utils.capitalize(string)
   assert res == result 

@pytest.mark.parametrize('string,result',('  skypro','skypro'))
def remove_start_line(string, result):
    string_utils = StringUtils()
    res = string_utils.trim(string)
    assert res == result

@pytest.mark.xfail()
def trim_in_number():
    string_utils = StringUtils()
    res = string_utils.trim(123456)
    assert res == '123456'

@pytest.mark.xfail()
def trim_with_spaces_output():
    string_utils = StringUtils()
    res = string_utils.trim('  happy  ')
    assert res == '  happy  '
