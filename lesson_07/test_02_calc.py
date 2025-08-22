from selenium import webdriver
from code_calc import Calc


def test_calc():
    browser = webdriver.Chrome()
    calc = Calc(browser)
    calc.time_delay(45)
    calc.select_summ()
    calc_res = calc.find_res()
    calc.quit()
    assert calc_res == '15', "Где-то ошибка"
