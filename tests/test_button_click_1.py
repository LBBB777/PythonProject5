from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import TestSetup     #  слева имя файла (без расширения .py)   справа - имя класса внутри этого файла
import unittest.result
import time
import allure
#from datetime import time

#
class ButtonLocators(unittest.TestCase):
    test_results = {}  #  словарь для хранения результатов

    def setUp(self):
        self.setup = TestSetup.TestSetup()  # Создаем объект TestSetup
        self.driver = self.setup.driver  # Получаем драйвер из объекта
        self.driver.get("https://www.effective-mobile.ru/")
        # try:
        #     # Добавляем явное ожидание загрузки страницы
        #     self.driver.get("https://www.effective-mobile.ru/")
        #     WebDriverWait(self.driver, 10).until(
        #         EC.title_is("Effective Mobile")  # Замените на актуальный заголовок
        #     )
        #     print("Страница успешно загружена")
        # except Exception as e:
        #     print(f"Ошибка при загрузке страницы: {str(e)}")
        #     self.driver.quit()
        #     raise

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

        ##########################################
    #####################  ТЕСТ РАБОЧИЙ  #####################
    @allure.feature('Тестирование функционала страницы авторизации')
    @allure.story('Авторизация с валидными данными')
    def test_1_button_vacancies_click(self):
        test_number: str = "1"  # Номер теста
        test_file = "test_button_click_1.py"  # Имя файла

        current_window = None       # Инициализируем переменную в которую  сохраним текущий URL

        # Заголовок теста
        print("\n")
        print("========================= ТЕСТ №{} из файла {} ========================".format(test_number, test_file))
        print("ЦЕЛЬ ПРОВЕРКИ:")
        print("Тестируется кликабельность кнопки 'Актуальные вакансии' - переход на страницу Вакансии(заголовок). Название страницы: 'Наши Junior вакансии'")

        try:

            # Ждем появления кнопки
            button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//a[contains(text(), 'Актуальные вакансии') and @href='https://ai-hunt.ru/vacancies/']")
                )
            )

            # Проверяем видимость кнопки
            self.assertTrue(button.is_displayed(), "Кнопка 'Актуальные вакансии' не видна на странице")

            # Сохраняем текущий URL
            current_window = self.driver.current_window_handle
            # ДОБАВЛЕНЫ ОТЛАДОЧНЫЕ ПРИНТЫ
            print("Текущий URL до клика:", self.driver.current_url)
            print("Ожидаемый URL : https://ai-hunt.ru/vacancies/")

            # Кликаем по кнопке
            button.click()

            # Ждем открытия новой вкладки
            WebDriverWait(self.driver, 20).until(EC.number_of_windows_to_be(2))

            # ### ИЗМЕНЕНО: Добавлена проверка всех доступных вкладок
            print("Доступные handles:", self.driver.window_handles)  # Отладочный вывод

            # ### ИЗМЕНЕНО: Добавлено ожидание полной загрузки новой страницы
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )

            # Переключаемся на новую вкладку
            for window in self.driver.window_handles:
                if window != current_window:
                    self.driver.switch_to.window(window)
                    break
            #  ОТЛАДОЧНЫЙ ПРИНТ
            print("URL после перехода:", self.driver.current_url)


            # Проверяем URL новой страницы
            expected_url = "https://ai-hunt.ru/vacancies/"
            actual_url = self.driver.current_url

            self.assertEqual(actual_url, expected_url, f"Неверный URL. Ожидалось: {expected_url}, получено: {actual_url}")

            # Проверяем заголовок страницы
            expected_title = "Вакансии"
            actual_title = self.driver.title

            #  ОТЛАДОЧНЫЙ ПРИНТ
            print("Заголовок страницы:", actual_title)

            self.assertTrue(expected_title in actual_title, f"Неверный заголовок страницы. Ожидалось: {expected_title}")

            # Записываем успешный результат
            self.test_results[f'Тест {test_number}'] = 'Успешно'
            print("Переход на страницу вакансий выполнен успешно")

        except Exception as e:
            self.test_results[f'Тест {test_number}'] = 'Провал'
            self.fail(f'Ошибка при проверке перехода: {str(e)}')

        finally:
            # Закрываем новую вкладку и возвращаемся на главную
            if  current_window:
                self.driver.close()
                self.driver.switch_to.window(current_window)
            self.print_test_footer(test_number, test_file)
            print("================== Завершен тест №{} из файла {} ========================".format(test_number, test_file))

# if __name__ == "__main__":
#     unittest.main()

    #######################################################
    ##########################  ТЕСТ РАБОЧИЙ ##################################
    @allure.feature('Тестирование функционала страницы авторизации')
    @allure.story('Авторизация с валидными данными')
    def test_2_button_vacancies_click(self):
        test_number: str = "2"  # Номер теста
        test_file = "test_button_click_1.py"  # Имя файла

        # Ожидаемый текст заголовка
        expected_text = 'Форматы сотрудничества'  # Добавляем определение переменной

        # Заголовок теста
        print("\n")
        print("========================= ТЕСТ №{} из файла {} ========================".format(test_number,
                                                                                               test_file))
        print("ЦЕЛЬ ПРОВЕРКИ:")
        print(
            "Проверка клика по кнопке 'Узнать больше' (главной страницы) и отображения раздела 'Формы сотрудничества' на той же странице")
        print("Ожидаемый заголовок раздела главной страницы: 'Форматы сотрудничества'")

        try:
            # Ждем появления кнопки
            button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//button[text()='Узнать больше' and @data-slot='button']")
                )
            )

            # Проверяем видимость кнопки
            self.assertTrue(button.is_displayed(), "Кнопка 'Узнать больше' не видна на странице")

            # Сохраняем текущий URL
            current_url = self.driver.current_url
            print("Текущий URL:", current_url)

            # Кликаем по кнопке
            button.click()

            # Сначала ждем появления элемента
            header = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//section[@id='services']//h2")
                )
            )

            # Затем ждем появления нужного текста в элементе
            WebDriverWait(self.driver, 10).until(
                EC.text_to_be_present_in_element(
                    (By.XPATH, "//section[@id='services']//h2"),
                    "Форматы сотрудничества"
                )
            )
            # Проверяем видимость
            self.assertTrue(header.is_displayed(), "Заголовок не виден на странице")

            # Получаем текст и очищаем от пробелов
            actual_text = header.text.strip()
            print(f"Актуальный заголовок: {actual_text}")

            # Сравниваем
            self.assertEqual(actual_text, expected_text,
                             f"Неверный текст заголовка. Ожидалось: {expected_text}, получено: {actual_text}")

        except Exception as e:
            self.test_results[f'Тест {test_number}'] = 'Провал'
            self.fail(f'Ошибка при проверке перехода: {str(e)}')

        finally:
            self.print_test_footer(test_number, test_file)
            self.driver.quit()  # Закрываем браузер после теста
            print(
                "================== Завершен тест №{} из файла {} ========================".format(test_number, test_file))

# if __name__ == "__main__":
#     unittest.main()

        ################################ ТЕСТ РАБОЧИЙ   ##########################
    @allure.feature('Тестирование функционала страницы авторизации')
    @allure.story('Авторизация с валидными данными')
    def test_3_button_vacancies_click(self):
        test_number: str = "3"  # Номер теста
        test_file = "test_button_click_1.py"  # Имя файла

        # Ожидаемый текст заголовка
        expected_text = 'Свяжитесь с нами'  # Добавляем определение переменной

        # Заголовок теста
        print("\n")
        print("========================= ТЕСТ №{} из файла {} ========================".format(test_number,
                                                                                               test_file))
        print("ЦЕЛЬ ПРОВЕРКИ:")
        print(
            "Проверка клика по кнопке 'Свяжитесь с нами'(главная страница) и отображения раздела 'Свяжитесь с нами' на той же странице")
        print("Ожидаемый заголовок раздела главной страницы: 'Свяжитесь с нами'")

        try:
            # Ждем появления кнопки
            button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//button[@data-slot='button'and contains(., 'Оставить заявку')]")
                )
            )
            # Проверяем видимость кнопки
            self.assertTrue(button.is_displayed(), "Кнопка 'Оставить заявку' не видна на странице")

            # WebDriverWait(self.driver, 10).until(         #явное ожидание загрузки страницы
            #     EC.url_contains("effective-mobile.ru")
            # )


            # Сохраняем текущий URL
            current_url = self.driver.current_url
            print("Текущий URL:", current_url)

            # Кликаем по кнопке
            button.click()

            # Ждем появления раздела "Свяжитесь с нами"
            header = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//div[@class='text-center mb-16']//h2[text()='Свяжитесь с нами']")
                )
            )
            # Получаем текст и очищаем от пробелов
            actual_text = header.text.strip()
            print(f"Актуальный заголовок: {actual_text}")

            # Сравниваем
            self.assertEqual(actual_text, expected_text,
                             f"Неверный текст заголовка. Ожидалось: {expected_text}, получено: {actual_text}")

            # Проверяем, что URL не изменился
            self.assertEqual(self.driver.current_url, current_url,
                             "URL изменился после клика, что не соответствует требованиям")

        except Exception as e:
            self.test_results[f'Тест {test_number}'] = 'Провал'
            self.fail(f'Ошибка при проверке перехода: {str(e)}')

        finally:
            self.print_test_footer(test_number, test_file)
            self.driver.quit()  # Закрываем браузер после теста
            print(
                "================== Завершен тест №{} из файла {} ========================".format(test_number,
                                                                                                   test_file))

if __name__ == "__main__":
    unittest.main()

