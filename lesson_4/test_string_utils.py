import pytest
from string_utils import StringUtils

string_utils = StringUtils()

@pytest.mark.parametrize('string,result',[('skypro','Skypro'), ('123','123'), ('hi mi name is natali','Hi mi name is natali'),('',''), (' ',' '), ('123456опана','123456опана')])
def test_first_capital_letter(string, result):
   string_utils = StringUtils()
   res =  string_utils.capitilize(string)
   assert res == result 

@pytest.mark.parametrize('string,result',[('  skypro','skypro'), ('   123','123'), ('  hi my friend','hi my friend'), ('','')])
def test_remove_start_line(string, result):
    string_utils = StringUtils()
    res = string_utils.trim(string)
    assert res == result

@pytest.mark.xfail()
def test_trim_in_number():
    string_utils = StringUtils()
    res = string_utils.trim(123456)
    assert res == '123456'

@pytest.mark.xfail()
def test_trim_with_spaces_output():
    string_utils = StringUtils()
    res = string_utils.trim('  happy  ')
    assert res == '  happy  '

@pytest.mark.parametrize('string, divider, result',[('яблоко,банан,апельсин',',',['яблоко', 'банан', 'апельсин']), ('1,2,3,4,5',',',['1', '2', '3', '4', '5']), ('!@@@#@$@%','@',['!', '@', '#', '$', '%']), ('',None,[]), ('1,2,3,4,5', None, ['1', '2', '3', '4', '5'])])
def test_divider_to_list(string, divider, result):
   string_utils = StringUtils() 
   if divider is None:
       res = string_utils.to_list(string)
   else:
       res = string_utils.to_list(string, divider)
       res == result
       
@pytest.mark.parametrize('string, symbol, result', [('банан','б',True), ('хорошо','ш',True), ('диван-кровать','-',True), ('банан','б',True),('','', True), ('привет','з',False), ('hello','б',False),('123456','б',False)])
def test_contains(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.contains(string, symbol)
    assert res == result

@pytest.mark.parametrize('string, symbol, result', [('банан','б','анан'), ('хорошо','ш','хороо'), ('диван-кровать','-','диванкровать'), ('', '', ''), ('привет','з','привет'), ('hello','б','hello'),('123456','б','123456')])
def test_delete_symbol(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.delete_symbol(string, symbol)
    assert res == result

@pytest.mark.parametrize('string, symbol, result', [('банан','б',True), ('Хорошо','Х',True), ('Hello','H',True), ('','', True), ('привет','П',False), ('hello','H',False),('123456','б',False)])
def test_stars_with(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.starts_with(string, symbol)
    assert res == result

@pytest.mark.parametrize('string, symbol, result', [('банан','н',True), ('ХорошО','О',True), ('Hello','o',True), ('','', True), ('привет','Т',False), ('hello','l',False),('123456','#',False)])
def test_ends_with(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.end_with(string, symbol)
    assert res == result

@pytest.mark.parametrize('string,result',[('',True), (' ',True), ('   ',True), ('не пустая строка',False),('не пустая строка с пробелом',False),('123',False)])
def test_is_empty(string, result):
    string_utils = StringUtils()
    res = string_utils.is_empty(string)
    assert res == result

@pytest.mark.parametrize ('list, joiner, result',[(['О','О','О'],',','О,О,О'), ([1,2,3,4,5], None, '1, 2, 3, 4, 5'), (['Первый','Второй'],'-','Первый-Второй'), ([],None,''), ([],'-',''), ([],'крот','')])
def test_list_to_string(list, joiner, result):
    string_utils = StringUtils()
    if joiner == None:
        res = string_utils.list_to_string(list)
    else:
        res = string_utils.list_to_string(list, joiner)
    assert res == result
