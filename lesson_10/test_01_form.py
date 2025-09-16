import pytest
from selenium import webdriver
from lesson_10.form_page import FormPage
import allure


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.
    """
    driver = webdriver.ChromiumEdge()
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Тестирование заполнения формы")
@allure.description("Тест проверяет наличие уведомления об ошибке "
                    "при не заполненом поле")
@allure.feature("Форма")
@allure.severity(allure.severity_level.CRITICAL)
def test_form(driver):
    """
    Тест проверяет корректность отображения не заполненных полей.

    :param driver: WebDriver — объект драйвера, переданный фикстурой.
    """
    form = FormPage(driver)

    with allure.step("Открытие страницы формы"):
        form.open()
    with allure.step("Заполенние страницы формы"):
        form.fill_form()
    with allure.step("Нажатие кнопки 'submitt'"):
        form.submitt()
    with allure.step("Полуение атрибута элемента zip-code"):
        zip_color = form.zip_code()
    with allure.step("Получение значений атрибутов заполненных полей"):
        other_color = form.success_fields()
    with allure.step("Проверка результатов"):
        assert zip_color == 'rgba(248, 215, 218, 1)', "Zip не красный"
        assert other_color is True
