import pytest
from Task014 import task14, string1
from Task015 import task15, string2
from Task016 import task16, string3
from Task017 import task17, string4
from Task018 import task18, date
def test_func():
    assert task14(string1) == ['aaaac', 'aaad', 'ae', 'ad']
def test_func1():
    assert task15(string2) == ['aaacccbbbb', 'aaacccccbb', 'aaaaabb']
def test_func2():
    assert task16(string3) == ['00:59', '03:15', '04:20', '18:30']
def test_func3():
    assert task17(string4) == ['ООО', 'ИП', 'НИИ МАНАНАЗЭМ', 'ООН', 'ИТИС КФУ']
def test_func4():
    assert task18(date) == ['30-04-2022']
pytest.main()



