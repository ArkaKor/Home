import pytest
from selenium import webdriver
from code_form import Form_Page


@pytest.fixture
def driver():
    driver = webdriver.ChromiumEdge()
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_form(driver):
    form = Form_Page(driver)
    form.open()
    form.fill_form()
    form.submitt()
    zip_color = form.zip_code()
    other_color = form.success_fields()
    assert zip_color == 'rgba(248, 215, 218, 1)', "Zip не красный"
    assert other_color is True
