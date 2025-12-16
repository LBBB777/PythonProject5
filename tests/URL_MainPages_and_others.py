import time  #  импорт модуля time
import requests
from bs4 import BeautifulSoup
from datetime import datetime
#############
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import TestSetup     #  слева имя файла (без расширения .py)   справа - имя класса внутри этого файла
import unittest.result

# Предназначение  кейса тестов.
# Служит для мониторинга доступности URL главной страницы ( тест 1) и других страниц, на которые осуществляется пекреход с главной страницы.
#  (Тест 2) URL страницы Вакансии, на которую осуществляется переход с главной страницы кликом по кнопке "Актуальные вакансии".
#  (Тест 3) URL страницы Junior IOS-разработчик, на которую осуществлоятся переход с главной страницы  кликом по кнопке "QA Engineer".
#  (Тест 4) URL страницы Junior Android-разработчик, на которую осуществлоятся переход с главной страницы  кликом по кнопке  "Android Developer".
#  (Тест 5) URL страницы Junior DevOps-инженер, на которую осуществлоятся переход с главной страницы  кликом по кнопке "DevOps Engineer".
#  (Тест 6) URL страницы Junior Системный аналитик, на которую осуществлоятся переход с главной страницы  кликом по кнопке  "Аналитик".
#  (Тест 7) URL страницы Junior Project Manager, на которую осуществлоятся переход с главной страницы  кликом по кнопке  "Project Manager".
#  (Тест 8) URL страницы Вакансии!! , на которую ВРЕМЕННО осуществлоятся переход с главной страницы  кликом по кнопке "Project Manager", т.к. страница находится в разработке


class WebsiteUrlTests(unittest.TestCase):

    def __init__(self,methodName='runTest'):
        super().__init__(methodName)   # Обязательно вызываем родительский конструктор
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 OPR/122.0.0.0 Edg/135.0.0.0'
        }
    # def setUp(self):
    #     self.setup = TestSetup.TestSetup()  # Создаем объект TestSetup
    #     self.driver = self.setup.driver  # Получаем драйвер из объекта
    #     self.driver.get("https://www.effective-mobile.ru/")

        # def tearDown(self):
        #     print(
        #         "lkl/jk!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        #     self.driver.quit()

    def print_test_start(self, message):

        print("\n" + "-" * 60)  # Добавляем разделитель сверху
        print(f"## {message} ##")  # Форматируем сообщение
        print("-" * 60)  # Добавляем разделитель снизу

        #################  Тестируется URL главной страницы  #################
    def test_01_URL_main_page(self):

        url = "https://www.effective-mobile.ru/"
        self.print_test_start("Тестируется URL главной страницы")

        report = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "url": url,
            "title_expected": 'Effective Mobile: Аутстафф и трудоустройство IT-специалистов',
            "title_actuale": None,
            "status_code": None,
            "expected_code": 200,
            "content_type": 'Не указан',
            "server": 'Не указан',
            "content_length": 'Не указан',
            "headers": {},
            "response_time": 'None'   # Поле для времени отклика
        }
        try:
            start_time = time.time()   # Засекаем время начала запроса
            # Отправляем запрос
            response = requests.get(url, timeout=10)

            end_time = time.time()  # Засекаем время окончания запроса
            report["response_time"] = f"{end_time - start_time:.5f} секунд"   # Вычисляем и сохраняем время отклика

            # Парсим HTML для получения заголовка
            soup = BeautifulSoup(response.content, "html.parser")
            title = soup.title.string if soup.title else 'Заголовок не найден'
            report["title_actuale"] = title

            # Заполняем отчет данными в  report
            report["status_code"] = response.status_code
            report["headers"] = dict(response.headers)
            report["content_type"] = response.headers.get('Content-Type', 'Не указан')
            report["server"] = response.headers.get('Server', 'Не указан')
            report["content_length"] = response.headers.get('Content-Length', 'Не указан')

            # Проверяем статус
            self.assertEqual (
                response.status_code, 200,
                f"Ошибка! Статус ответа не соответствует ожидаемому:\n"
                f"Ожидаемый код: 200\n"
                f"Полученный код: {response.status_code}\n"
                f"URL: {url}\n"
                f"Тип контента: {report['content_type']}\n"
                f"Сервер: {report['server']}\n"
                f"Длина содержимого: {report['content_length']}\n"
                f"Время отклика: {report['response_time']}\n"
                f"Ожидаемый заголовок: {report['title_expected']}\n"
                f"Фактический заголовок: {report['title_actuale']}\n"
                f"Заголовки ответа: {report['headers']}"
            )

            # Форматируем вывод отчета
            print("\nПроверка прошла успешно!\nПодробный отчет:")
            print("-" * 60)
            for key, value in report.items():
                if value is not None:  # Фильтруем пустые значения
                    print(f"  {key:<40}: {value}")
            print("-" * 60)

        except requests.exceptions.RequestException as e:  #  проверка сетевых ошибок
            # При сетевой ошибке заполняем отчет информацией об ошибке
            report["error"] = str(e)    #  Выполняется функция обработки ошибки, когда возникает сетевая ошибка при выполнении запроса.  в  словарь добавляется строка "error":
            print("Произошла сетевая ошибка при запросе! Подробный отчет об ошибке:")
            for key, value in report.items():
                if value is not None:
                    print(f"{key}: {value}")
            #print(f"Описание ошибки: {str(e)}")

        except AssertionError as e:           #  проверка статуса кода
            print("Ошибка проверки статуса:")
            print(str(e))
            print("Подробный отчет:")
            for key, value in report.items():
                print(f"{key}: {value}")

# #
# #
# if __name__ == "__main__":
#     unittest.main()
#




     #################  Тестируется URL страницы Вакансии  #################
    def test_02_URL_main_page(self):

        url = "https://ai-hunt.ru/vacancies/"

        self.print_test_start("Тестируется URL страницы Вакансии//\nКнопка перехода с главной страницы -  Актуальные вакансии")

        report = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "url": url,
            "title_expected": 'Вакансии',
            "title_actual": None,
            "status_code": None,
            "expected_code": 200,
            "content_type": 'Не указан',
            "server": 'Не указан',
            "content_length": 'Не указан',
            "headers": {},
            "response_time": 'None'  # Поле для времени отклика
        }
        try:
            start_time = time.time()  # Засекаем время начала запроса
            # Отправляем запрос
            response = requests.get(url, timeout=10)

            end_time = time.time()  # Засекаем время окончания запроса
            report["response_time"] = f"{end_time - start_time:.5f} секунд"  # Вычисляем и сохраняем время отклика

            # Парсим HTML для получения заголовка
            soup = BeautifulSoup(response.content, "html.parser")
            title = soup.title.string if soup.title else 'Заголовок не найден'
            report["title_actual"] = title  # Сохранение фактического заголовка

            # Заполняем отчет данными в  report
            report["status_code"] = response.status_code
            report["headers"] = dict(response.headers)
            report["content_type"] = response.headers.get('Content-Type', 'Не указан')
            report["server"] = response.headers.get('Server', 'Не указан')
            report["content_length"] = response.headers.get('Content-Length', 'Не указан')

            # Проверяем статус
            self.assertEqual(
                response.status_code, 200,
                f"Ошибка! Статус ответа не соответствует ожидаемому:\n"
                f"Ожидаемый код: 200\n"
                f"Полученный код: {response.status_code}\n"
                f"URL: {url}\n"
                f"Тип контента: {report['content_type']}\n"
                f"Сервер: {report['server']}\n"
                f"Длина содержимого: {report['content_length']}\n"
                f"Время отклика: {report['response_time']}\n"
                f"Ожидаемый заголовок: {report['title_expected']}\n"  # Вывод ожидаемого
                f"Фактический заголовок: {report['title_actual']}\n"  # Вывод фактического
                f"Заголовки ответа: {report['headers']}"
        )
            # Форматируем вывод отчета
            #print("\n1.Тестируется URL главной страницы сайта ")
            print("\nПроверка прошла успешно!\nПодробный отчет:")
            print("-" * 60)
            for key, value in report.items():
                if value is not None:  # Фильтруем пустые значения
                    print(f"  {key:<40}: {value}")
            print("-" * 60)

        except requests.exceptions.RequestException as e:  # проверка сетевых ошибок
            # При сетевой ошибке заполняем отчет информацией об ошибке
            report["error"] = str(e)  # Выполняется функция обработки ошибки, когда возникает сетевая ошибка при выполнении запроса.  в  словарь добавляется строка "error":
            print("Произошла сетевая ошибка при запросе! Подробный отчет об ошибке:")
            print("-" * 60)
            for key, value in report.items():
                if value is not None:
                    print(f"{key}: {value}")
            print("-" * 60)

        except AssertionError as e:  # проверка статуса кода
            print("\nОшибка проверки статуса:")
            print(str(e))
            print("Подробный отчет:")
            print("-" * 60)
            for key, value in report.items():
                print(f"{key}: {value}")
            print("-" * 60)



# ################  Раздел Кого мы ищем #####################

    #############  Junior IOS-разработчик####  кнопка QA Engineer  главной страницы ######

    def test_03_URL_main_page(self):

        url = "https://ai-hunt.ru/vacancies/IOS"

        self.print_test_start("Тестируется URL страницы Junior IOS-разработчик// \nКнопка перехода с главной страницы QA Engineer ")

        report = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "url": url,
            "title_expected": 'Junior IOS-разработчик',
            "title_actual": None,  # Фактический заголовок
            "status_code": None,
            "expected_code": 200,
            "content_type": 'Не указан',
            "server": 'Не указан',
            "content_length": 'Не указан',
            "headers": {},
            "response_time": 'None'  # Поле для времени отклика
        }
        try:
            start_time = time.time()  # Засекаем время начала запроса
            # Отправляем запрос
            response = requests.get(url, timeout=10)

            end_time = time.time()  # Засекаем время окончания запроса
            report["response_time"] = f"{end_time - start_time:.5f} секунд"  # Вычисляем и сохраняем время отклика

            # Парсим HTML для получения заголовка
            soup = BeautifulSoup(response.content, "html.parser")
            title = soup.title.string if soup.title else 'Заголовок не найден'
            report["title_actual"] = title  # Сохранение фактического заголовка


            # Заполняем отчет данными в  report
            report["status_code"] = response.status_code
            report["headers"] = dict(response.headers)
            report["content_type"] = response.headers.get('Content-Type', 'Не указан')
            report["server"] = response.headers.get('Server', 'Не указан')
            report["content_length"] = response.headers.get('Content-Length', 'Не указан')

            # Проверяем статус
            self.assertEqual(
                response.status_code, 200,
                f"Ошибка! Статус ответа не соответствует ожидаемому:\n"
                f"Ожидаемый код: 200\n"
                f"Полученный код: {response.status_code}\n"
                f"URL: {url}\n"
                f"Тип контента: {report['content_type']}\n"
                f"Сервер: {report['server']}\n"
                f"Длина содержимого: {report['content_length']}\n"
                f"Время отклика: {report['response_time']}\n"
                f"Ожидаемый заголовок: {report['title_expected']}\n"  # Вывод ожидаемого
                f"Фактический заголовок: {report['title_actual']}\n"  # Вывод фактического
                f"Заголовки ответа: {report['headers']}"
        )

            # Форматируем вывод отчета
            #print("\n1.Тестируется URL главной страницы сайта ")
            print("\nПроверка прошла успешно!\nПодробный отчет:")
            print("-" * 60)
            for key, value in report.items():
                if value is not None:  # Фильтруем пустые значения
                    print(f"  {key:<40}: {value}")
            print("-" * 60)

        except requests.exceptions.RequestException as e:  # проверка сетевых ошибок
            # При сетевой ошибке заполняем отчет информацией об ошибке
            report["error"] = str(e)  # Выполняется функция обработки ошибки, когда возникает сетевая ошибка при выполнении запроса.  в  словарь добавляется строка "error":
            print("Произошла сетевая ошибка при запросе! Подробный отчет об ошибке:")
            print("-" * 60)
            for key, value in report.items():
                if value is not None:
                    print(f"{key}: {value}")
            print("-" * 60)

        except AssertionError as e:  # проверка статуса кода
            print("\nОшибка проверки статуса:")
            print(str(e))
            print("Подробный отчет:")
            print("-" * 60)
            for key, value in report.items():
                print(f"{key}: {value}")
            print("-" * 60)



    #############  Junior Android-разработчик  ####  кнопка Android Developer  ######

    def test_04_URL_main_page(self):

        url = "https://ai-hunt.ru/vacancies/ANDROID"

        self.print_test_start("Тестируется URL страницы Junior Android-разработчик// \nКнопка перехода с главной страницы  Android Developer ")

        report = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "url": url,
            "title_expected": 'Junior Android-разработчик',
            "title_actual": None,  # Фактический заголовок
            "status_code": None,
            "expected_code": 200,
            "content_type": 'Не указан',
            "server": 'Не указан',
            "content_length": 'Не указан',
            "headers": {},
            "response_time": 'None'  # Поле для времени отклика
        }
        try:
            start_time = time.time()  # Засекаем время начала запроса
            # Отправляем запрос
            response = requests.get(url, timeout=10)

            end_time = time.time()  # Засекаем время окончания запроса
            report["response_time"] = f"{end_time - start_time:.5f} секунд"  # Вычисляем и сохраняем время отклика

            # Парсим HTML для получения заголовка
            soup = BeautifulSoup(response.content, "html.parser")
            title = soup.title.string if soup.title else 'Заголовок не найден'
            report["title_actual"] = title  # Сохранение фактического заголовка

            # Заполняем отчет данными в  report
            report["status_code"] = response.status_code
            report["headers"] = dict(response.headers)
            report["content_type"] = response.headers.get('Content-Type', 'Не указан')
            report["server"] = response.headers.get('Server', 'Не указан')
            report["content_length"] = response.headers.get('Content-Length', 'Не указан')

            # Проверяем статус
            self.assertEqual(
                response.status_code, 200,
                f"Ошибка! Статус ответа не соответствует ожидаемому:\n"
                f"Ожидаемый код: 200\n"
                f"Полученный код: {response.status_code}\n"
                f"URL: {url}\n"
                f"Тип контента: {report['content_type']}\n"
                f"Сервер: {report['server']}\n"
                f"Длина содержимого: {report['content_length']}\n"
                f"Время отклика: {report['response_time']}\n"
                f"Ожидаемый заголовок: {report['title_expected']}\n"  # Вывод ожидаемого
                f"Фактический заголовок: {report['title_actual']}\n"  # Вывод фактического
                f"Заголовки ответа: {report['headers']}"
            )

            # Форматируем вывод отчета
            # print("\n1.Тестируется URL главной страницы сайта ")
            print("\nПроверка прошла успешно!\nПодробный отчет:")
            print("-" * 60)
            for key, value in report.items():
                if value is not None:  # Фильтруем пустые значения
                    print(f"  {key:<40}: {value}")
            print("-" * 60)

        except requests.exceptions.RequestException as e:  # проверка сетевых ошибок
            # При сетевой ошибке заполняем отчет информацией об ошибке
            report["error"] = str(
                e)  # Выполняется функция обработки ошибки, когда возникает сетевая ошибка при выполнении запроса.  в  словарь добавляется строка "error":
            print("Произошла сетевая ошибка при запросе! Подробный отчет об ошибке:")
            print("-" * 60)
            for key, value in report.items():
                if value is not None:
                    print(f"{key}: {value}")
            print("-" * 60)

        except AssertionError as e:  # проверка статуса кода
            print("\nОшибка проверки статуса:")
            print(str(e))
            print("Подробный отчет:")
            print("-" * 60)
            for key, value in report.items():
                print(f"{key}: {value}")
            print("-" * 60)


##########################
    #############  unior DevOps-инженерк  ####  кнопка yf главной страницы  DevOps Engineer ######

    def test_05_URL_main_page(self):

        url = "https://ai-hunt.ru/vacancies/DEVOPS"

        self.print_test_start("Тестируется URL страницы Junior DevOps-инженер// \nКнопка перехода с главной страницы  DevOps Engineer ")

        report = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "url": url,
            "title_expected": 'Junior DevOps-инженер',
            "title_actual": None,  # Фактический заголовок
            "status_code": None,
            "expected_code": 200,
            "content_type": 'Не указан',
            "server": 'Не указан',
            "content_length": 'Не указан',
            "headers": {},
            "response_time": 'None'  # Поле для времени отклика
        }
        try:
            start_time = time.time()  # Засекаем время начала запроса
            # Отправляем запрос
            response = requests.get(url, timeout=10)

            end_time = time.time()  # Засекаем время окончания запроса
            report["response_time"] = f"{end_time - start_time:.5f} секунд"  # Вычисляем и сохраняем время отклика

            # Парсим HTML для получения заголовка
            soup = BeautifulSoup(response.content, "html.parser")
            title = soup.title.string if soup.title else 'Заголовок не найден'
            report["title_actual"] = title  # Сохранение фактического заголовка

            # Заполняем отчет данными в  report
            report["status_code"] = response.status_code
            report["headers"] = dict(response.headers)
            report["content_type"] = response.headers.get('Content-Type', 'Не указан')
            report["server"] = response.headers.get('Server', 'Не указан')
            report["content_length"] = response.headers.get('Content-Length', 'Не указан')

            # Проверяем статус
            self.assertEqual(
                response.status_code, 200,
                f"Ошибка! Статус ответа не соответствует ожидаемому:\n"
                f"Ожидаемый код: 200\n"
                f"Полученный код: {response.status_code}\n"
                f"URL: {url}\n"
                f"Тип контента: {report['content_type']}\n"
                f"Сервер: {report['server']}\n"
                f"Длина содержимого: {report['content_length']}\n"
                f"Время отклика: {report['response_time']}\n"
                f"Ожидаемый заголовок: {report['title_expected']}\n"  # Вывод ожидаемого
                f"Фактический заголовок: {report['title_actual']}\n"  # Вывод фактического
                f"Заголовки ответа: {report['headers']}"
            )

            # Форматируем вывод отчета
            # print("\n1.Тестируется URL главной страницы сайта ")
            print("\nПроверка прошла успешно!\nПодробный отчет:")
            print("-" * 60)
            for key, value in report.items():
                if value is not None:  # Фильтруем пустые значения
                    print(f"  {key:<40}: {value}")
            print("-" * 60)

        except requests.exceptions.RequestException as e:  # проверка сетевых ошибок
            # При сетевой ошибке заполняем отчет информацией об ошибке
            report["error"] = str(
                e)  # Выполняется функция обработки ошибки, когда возникает сетевая ошибка при выполнении запроса.  в  словарь добавляется строка "error":
            print("Произошла сетевая ошибка при запросе! Подробный отчет об ошибке:")
            print("-" * 60)
            for key, value in report.items():
                if value is not None:
                    print(f"{key}: {value}")
            print("-" * 60)

        except AssertionError as e:  # проверка статуса кода
            print("\nОшибка проверки статуса:")
            print(str(e))
            print("Подробный отчет:")
            print("-" * 60)
            for key, value in report.items():
                print(f"{key}: {value}")
            print("-" * 60)


 ##############################
#  ############################

#############  unior DevOps-инженерк  ####  кнопка на главной страницы  Аналитик ######

    def test_06_URL_main_page(self):
        url = "https://ai-hunt.ru/vacancies/SA"

        self.print_test_start(
            "Тестируется URL страницы Junior Системный аналитик// \nКнопка перехода на главной странице  Аналитик ")

        report = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "url": url,
            "title_expected": 'Junior Системный аналитик',
            "title_actual": None,  # Фактический заголовок
            "status_code": None,
            "expected_code": 200,
            "content_type": 'Не указан',
            "server": 'Не указан',
            "content_length": 'Не указан',
            "headers": {},
            "response_time": 'None'  # Поле для времени отклика
        }
        try:
            start_time = time.time()  # Засекаем время начала запроса
            # Отправляем запрос
            response = requests.get(url, timeout=10)

            end_time = time.time()  # Засекаем время окончания запроса
            report["response_time"] = f"{end_time - start_time:.5f} секунд"  # Вычисляем и сохраняем время отклика

            # Парсим HTML для получения заголовка
            soup = BeautifulSoup(response.content, "html.parser")
            title = soup.title.string if soup.title else 'Заголовок не найден'
            report["title_actual"] = title  # Сохранение фактического заголовка

            # Заполняем отчет данными в  report
            report["status_code"] = response.status_code
            report["headers"] = dict(response.headers)
            report["content_type"] = response.headers.get('Content-Type', 'Не указан')
            report["server"] = response.headers.get('Server', 'Не указан')
            report["content_length"] = response.headers.get('Content-Length', 'Не указан')

            # Проверяем статус
            self.assertEqual(
                response.status_code, 200,
                f"Ошибка! Статус ответа не соответствует ожидаемому:\n"
                f"Ожидаемый код: 200\n"
                f"Полученный код: {response.status_code}\n"
                f"URL: {url}\n"
                f"Тип контента: {report['content_type']}\n"
                f"Сервер: {report['server']}\n"
                f"Длина содержимого: {report['content_length']}\n"
                f"Время отклика: {report['response_time']}\n"
                f"Ожидаемый заголовок: {report['title_expected']}\n"  # Вывод ожидаемого
                f"Фактический заголовок: {report['title_actual']}\n"  # Вывод фактического
                f"Заголовки ответа: {report['headers']}"
            )

            # Форматируем вывод отчета
            # print("\n1.Тестируется URL главной страницы сайта ")
            print("\nПроверка прошла успешно!\nПодробный отчет:")
            print("-" * 60)
            for key, value in report.items():
                if value is not None:  # Фильтруем пустые значения
                    print(f"  {key:<40}: {value}")
            print("-" * 60)

        except requests.exceptions.RequestException as e:  # проверка сетевых ошибок
            # При сетевой ошибке заполняем отчет информацией об ошибке
            report["error"] = str(
                e)  # Выполняется функция обработки ошибки, когда возникает сетевая ошибка при выполнении запроса.  в  словарь добавляется строка "error":
            print("Произошла сетевая ошибка при запросе! Подробный отчет об ошибке:")
            print("-" * 60)
            for key, value in report.items():
                if value is not None:
                    print(f"{key}: {value}")
            print("-" * 60)

        except AssertionError as e:  # проверка статуса кода
            print("\nОшибка проверки статуса:")
            print(str(e))
            print("Подробный отчет:")
            print("-" * 60)
            for key, value in report.items():
                print(f"{key}: {value}")
            print("-" * 60)


# if __name__ == "__main__":
#     unittest.main()




#############  Junior Project Manager  ####  кнопка на главной страницы  Project Manager ######

    def test_07_URL_main_page(self):
        url = "https://ai-hunt.ru/vacancies/PM"

        self.print_test_start(
            "Тестируется URL страницы Junior Project Manager// \nКнопка перехода на главной странице  Project Manager ")

        report = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "url": url,
            "title_expected": 'Junior Project Manager',
            "title_actual": None,  # Фактический заголовок
            "status_code": None,
            "expected_code": 200,
            "content_type": 'Не указан',
            "server": 'Не указан',
            "content_length": 'Не указан',
            "headers": {},
            "response_time": 'None'  # Поле для времени отклика
        }
        try:
            start_time = time.time()  # Засекаем время начала запроса
            # Отправляем запрос
            response = requests.get(url, timeout=10)

            end_time = time.time()  # Засекаем время окончания запроса
            report["response_time"] = f"{end_time - start_time:.5f} секунд"  # Вычисляем и сохраняем время отклика

            # Парсим HTML для получения заголовка
            soup = BeautifulSoup(response.content, "html.parser")
            title = soup.title.string if soup.title else 'Заголовок не найден'
            report["title_actual"] = title  # Сохранение фактического заголовка

            # Заполняем отчет данными в  report
            report["status_code"] = response.status_code
            report["headers"] = dict(response.headers)
            report["content_type"] = response.headers.get('Content-Type', 'Не указан')
            report["server"] = response.headers.get('Server', 'Не указан')
            report["content_length"] = response.headers.get('Content-Length', 'Не указан')

            # Проверяем статус
            self.assertEqual(
                response.status_code, 200,
                f"Ошибка! Статус ответа не соответствует ожидаемому:\n"
                f"Ожидаемый код: 200\n"
                f"Полученный код: {response.status_code}\n"
                f"URL: {url}\n"
                f"Тип контента: {report['content_type']}\n"
                f"Сервер: {report['server']}\n"
                f"Длина содержимого: {report['content_length']}\n"
                f"Время отклика: {report['response_time']}\n"
                f"Ожидаемый заголовок: {report['title_expected']}\n"  # Вывод ожидаемого
                f"Фактический заголовок: {report['title_actual']}\n"  # Вывод фактического
                f"Заголовки ответа: {report['headers']}"
            )

            # Форматируем вывод отчета
            # print("\n1.Тестируется URL главной страницы сайта ")
            print("\nПроверка прошла успешно!\nПодробный отчет:")
            print("-" * 60)
            for key, value in report.items():
                if value is not None:  # Фильтруем пустые значения
                    print(f"  {key:<40}: {value}")
            print("-" * 60)

        except requests.exceptions.RequestException as e:  # проверка сетевых ошибок
            # При сетевой ошибке заполняем отчет информацией об ошибке
            report["error"] = str(
                e)  # Выполняется функция обработки ошибки, когда возникает сетевая ошибка при выполнении запроса.  в  словарь добавляется строка "error":
            print("Произошла сетевая ошибка при запросе! Подробный отчет об ошибке:")
            print("-" * 60)
            for key, value in report.items():
                if value is not None:
                    print(f"{key}: {value}")
            print("-" * 60)

        except AssertionError as e:  # проверка статуса кода
            print("\nОшибка проверки статуса:")
            print(str(e))
            print("Подробный отчет:")
            print("-" * 60)
            for key, value in report.items():
                print(f"{key}: {value}")
            print("-" * 60)

#############################
############################

############  Junior Project Manager  ####  кнопка на главной странице  Unity Developer ######

    def test_08_URL_main_page(self):
        url = "https://ai-hunt.ru/vacancies/"

        self.print_test_start(
            "Кнопка перехода на главной странице - Project Manager// тестируется URL  на который осуществляется переход// \n"
            "Страница в разработке, URL пока завязана на страницу Вакансии!!//  ")

        report = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "url": url,
            "title_expected": 'Вакансии- временное название, стр. в разработке',
            "title_actual": None,  # Фактический заголовок
            "status_code": None,
            "expected_code": 200,
            "content_type": 'Не указан',
            "server": 'Не указан',
            "content_length": 'Не указан',
            "headers": {},
            "response_time": 'None'  # Поле для времени отклика
        }
        try:
            start_time = time.time()  # Засекаем время начала запроса
            # Отправляем запрос
            response = requests.get(url, timeout=10)

            end_time = time.time()  # Засекаем время окончания запроса
            report["response_time"] = f"{end_time - start_time:.5f} секунд"  # Вычисляем и сохраняем время отклика

            # Парсим HTML для получения заголовка
            soup = BeautifulSoup(response.content, "html.parser")
            title = soup.title.string if soup.title else 'Заголовок не найден'
            report["title_actual"] = title  # Сохранение фактического заголовка

            # Заполняем отчет данными в  report
            report["status_code"] = response.status_code
            report["headers"] = dict(response.headers)
            report["content_type"] = response.headers.get('Content-Type', 'Не указан')
            report["server"] = response.headers.get('Server', 'Не указан')
            report["content_length"] = response.headers.get('Content-Length', 'Не указан')

            # Проверяем статус
            self.assertEqual(
                response.status_code, 200,
                f"Ошибка! Статус ответа не соответствует ожидаемому:\n"
                f"Ожидаемый код: 200\n"
                f"Полученный код: {response.status_code}\n"
                f"URL: {url}\n"
                f"Тип контента: {report['content_type']}\n"
                f"Сервер: {report['server']}\n"
                f"Длина содержимого: {report['content_length']}\n"
                f"Время отклика: {report['response_time']}\n"
                f"Ожидаемый заголовок: {report['title_expected']}\n"  # Вывод ожидаемого
                f"Фактический заголовок: {report['title_actual']}\n"  # Вывод фактического
                f"Заголовки ответа: {report['headers']}"
            )

            # Форматируем вывод отчета
            # print("\n1.Тестируется URL главной страницы сайта ")
            print("\nПроверка прошла успешно!\nПодробный отчет:")
            print("-" * 60)
            for key, value in report.items():
                if value is not None:  # Фильтруем пустые значения
                    print(f"  {key:<40}: {value}")
            print("-" * 60)

        except requests.exceptions.RequestException as e:  # проверка сетевых ошибок
            # При сетевой ошибке заполняем отчет информацией об ошибке
            report["error"] = str(
                e)  # Выполняется функция обработки ошибки, когда возникает сетевая ошибка при выполнении запроса.  в  словарь добавляется строка "error":
            print("Произошла сетевая ошибка при запросе! Подробный отчет об ошибке:")
            print("-" * 60)
            for key, value in report.items():
                if value is not None:
                    print(f"{key}: {value}")
            print("-" * 60)

        except AssertionError as e:  # проверка статуса кода
            print("\nОшибка проверки статуса:")
            print(str(e))
            print("Подробный отчет:")
            print("-" * 60)
            for key, value in report.items():
                print(f"{key}: {value}")
            print("-" * 60)





if __name__ == "__main__":
    unittest.main()


#
#
# ####################################
#####################################
