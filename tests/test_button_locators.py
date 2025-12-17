from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import TestSetup  # слева имя файла (без расширения .py)   справа - имя класса внутри этого файла
import unittest
import unittest.result
import time
import allure
#from datetime import time
#
# def assertTrue(param, param1):
#     pass


class Button_locators(unittest.TestCase):
    test_results = {}  # словарьдля хранения результатов

    def setUp(self):
        self.setup = TestSetup.TestSetup()  # Создаем объект TestSetup
        self.driver = self.setup.driver  # Получаем драйвер из объекта
        self.driver.get("https://www.effective-mobile.ru/")

    def tearDown(self):
        try:
            print("Закрываем драйвер...")
            if self.driver:
                self.driver.quit()
                print("Драйвер успешно закрыт")
        except Exception as e:
            print(f"Ошибка при закрытии драйвера: {str(e)}")
        finally:
            # Добавляем задержку для корректного завершения процессов
            time.sleep(2)

    def print_test_footer(self, test_number, test_file):
        # Здесь реализация метода ВЫВЕДЕНИЯ ОТЧЕТА
        print(f"Завершение теста {test_number} из файла {test_file}")

    ##########Кнопка Актуальные вакансии  , проверка локаторов
    @allure.feature('Тестирование функционала страницы авторизации')
    @allure.story('Авторизация с валидными данными')
    def test_01_button_current_vacancies_ls_1(self):
        # Информация о тесте
        test_number: str = "1"  # Номер теста
        test_file = "test_button_locators.py"  # Имя файла

        # Заголовок теста
        print("\n")
        print("========================= ТЕСТ №{} из файла {} =========================".format(test_number, test_file))
        print("ЦЕЛЬ ПРОВЕРКИ:")
        print(
            "Проверка нахождения кнопки Актуальные вакансии' по XPath: //a[@data-slot='button' and @href='https://ai-hunt.ru/vacancies/']")

        try:
            # Ждем появления элемента
            button = WebDriverWait(self.driver, 10).until(  # Создаем ожидание для веб-драйвера
                EC.presence_of_element_located(
                    # Проверяем наличие элемента  //EC.presence_of_element_located — это метод из модуля Expected Conditions //
                    (By.XPATH, "//a[@data-slot='button' and @href='https://ai-hunt.ru/vacancies/']")
                    # Указываем локатор элемента
                )
            )

            self.assertTrue(button.is_displayed(), "Кнопка не найдена")  # Проверяем, что элемент виден на странице
            print(f'Кнопка: "{button.text}" найдена по заданному XPath')
            self.test_results[f'Тест {test_number}'] = 'Успешно'  # Добавляем эту строку

        except Exception as e:  # Если произошла ошибка
            self.test_results[f'Тест № {test_number}'] = 'Провал'  # Если тест упал
            self.fail(f'Ошибка при поиске кнопки: {str(e)} о заданному XPath')

        finally:
            self.print_test_footer(test_number, test_file)
            print("=========Завершен тест №{} из файла {} =========================".format(test_number, test_file))

    ############################################
    @allure.feature('Тестирование функционала страницы авторизации')
    @allure.story('Авторизация с валидными данными')
    def test_02_button_current_vacancies_ls_2(self):
        # Информация о тесте
        test_number: str = "2"  # Номер теста
        test_file = "test_button_locators.py"  # Имя файла

        # Заголовок теста
        print("\n")
        print("========================= ТЕСТ №{} из файла {} =========================".format(test_number, test_file))

        # obj = TestSetup.TestSetup()
        # obj.driver.get("https://www.effective-mobile.ru/")

        print("ЦЕЛЬ ПРОВЕРКИ:")
        print('Проверка нахождения кнопки Актуальные вакансии\' по XPath: //a[text()="Актуальные вакансии"]')

        try:
            # Ждем появления элемента
            button = WebDriverWait(self.driver, 10).until(  # Создаем ожидание для веб-драйвера
                EC.presence_of_element_located(
                    # Проверяем наличие элемента  //EC.presence_of_element_located — это метод из модуля Expected Conditions //
                    (By.XPATH, "//a[@data-slot='button' and @href='https://ai-hunt.ru/vacancies/']")
                    # Указываем локатор элемента
                )
            )

            self.assertTrue(button.is_displayed(), "Кнопка не найдена")  # Проверяем, что элемент виден на странице
            print(f'Кнопка: "{button.text}" найдена по заданному XPath')
            self.test_results[f'Тест {test_number}'] = 'Успешно'  # Добавляем эту строку

        except Exception as e:  # Если произошла ошибка
            self.test_results[f'Тест № {test_number}'] = 'Провал'  # Если тест упал
            self.fail(f'Ошибка при поиске кнопки: {str(e)} о заданному XPath')

        finally:
            self.print_test_footer(test_number, test_file)
            print("==============Завершен тест №{} из файла {} ========================".format(test_number, test_file))

    # ############################################
    @allure.feature('Тестирование функционала страницы авторизации')
    @allure.story('Авторизация с валидными данными')
    def test_03_button_applications_ls_1(self):  # Проверка локаторов кнопки "Оставить заявку" на главной странице
        # Информация о тесте
        test_number: str = "3"  # Номер теста
        test_file = "test_button_locators.py"  # Имя файла

        # Заголовок теста
        print("\n")
        print("========================= ТЕСТ №{} из файла {} =========================".format(test_number, test_file))
        print("ЦЕЛЬ ПРОВЕРКИ:")
        print(
            "Проверка нахождения кнопки  Оставить заявку на главной странице по CSS локатору  button[data-slot='button'][class*='bg-brand-primary']")

        try:
            # Ждем появления элемента
            button = WebDriverWait(self.driver, 10).until(  # Создаем ожидание для веб-драйвера
                EC.presence_of_element_located(
                    # Проверяем наличие элемента  //EC.presence_of_element_located — это метод из модуля Expected Conditions //
                    (By.CSS_SELECTOR, "button[data-slot='button'][class*='bg-brand-primary']")
                    # Указываем локатор элемента
                )
            )

            # Проверяем видимость
            self.assertTrue(button.is_displayed(), "Кнопка или не найдена в DOM или не видна")

            self.test_results[f'Тест {test_number}'] = 'Успешно'  # Добавляем эту строку
            print(f'Кнопка: "{button.text}" найдена по CSS локатору')

        except Exception as e:  # Если произошла ошибка
            self.test_results[f'Тест № {test_number}'] = 'Провал'  # Если тест упал
            self.fail(f'Ошибка при поиске кнопки: {str(e)} о заданному XPath')

        finally:
            self.print_test_footer(test_number, test_file)
            print("==========Завершен тест №{} из файла {} ========================".format(test_number, test_file))

    #   # ############################################
    @allure.feature('Тестирование функционала страницы авторизации')
    @allure.story('Авторизация с валидными данными')
    def test_04_button_ToLearnMore_ls_1(self):  # Проверка локаторов кнопки "Узнать больше" на главной странице
        # Информация о тесте
        test_number: str = "4"  # Номер теста
        test_file = "test_button_locators.py"  # Имя файла

        # Заголовок теста
        print("\n")
        print("========================= ТЕСТ №{} из файла {} =========================".format(test_number, test_file))
        print("ЦЕЛЬ ПРОВЕРКИ:")
        print(
            "Проверка нахождения кнопки  Узнать больше на главной странице по XPath-локатору 'button[text()='Узнать больше' and @data-slot='button']")

        try:
            # Ждем появления элемента
            button = WebDriverWait(self.driver, 10).until(  # Создаем ожидание для веб-драйвера
                EC.presence_of_element_located(
                    # Проверяем наличие элемента  //EC.presence_of_element_located — это метод из модуля Expected Conditions //
                    (By.XPATH, "//button[text()='Узнать больше' and @data-slot='button']")
                )
            )

            # Проверяем видимость
            self.assertTrue(button.is_displayed(), "Кнопка или не найдена в DOM или не видна")

            self.test_results[f'Тест {test_number}'] = 'Успешно'  # Добавляем эту строку
            print(f'Кнопка: "{button.text}" найдена XPath-локатору')

        except Exception as e:  # Если произошла ошибка
            self.test_results[f'Тест № {test_number}'] = 'Провал'  # Если тест упал
            self.fail(f'Ошибка при поиске кнопки: {str(e)} о заданному XPath')

        finally:
            self.print_test_footer(test_number, test_file)
            print("============ТЕСТ №{} из файла {} =========================".format(test_number, test_file))


if __name__ == "__main__":
    # # Запрашиваем у пользователя ввод
    # choice = input("Выберите тест (1 или 2) или нажмите Enter для запуска всех тестов: ")
    #
    # # Проверяем выбор пользователя
    # if choice == '1':
    #     # Запускаем только первый тест
    #     unittest.main(defaultTest='ButtonCurrentVacanciesTest_locators.test_button_current_vacancies_ls_1')
    # elif choice == '2':
    #     # Запускаем только второй тест
    #     unittest.main(defaultTest='ButtonCurrentVacanciesTest_locators.test_button_current_vacancies_ls_2')
    # else:
    #     # Если введено что-то другое или нажата Enter - запускаем все тесты
    #     unittest.main()
    unittest.main()
