# test_qa_practice
UI Automation Framework for qa-practice.com using Python, Selenium, and Pytest (Page Object Model),
API tests by requests
# Стек технологий
  - Python 3.12
  - Selenium
  - Pytest
  - Pattern Page Object Model (POM)
  - Requests
  - CI/CD: автоматизация запусков через GitHub Actions (CI)

# Структура проекта
  - pages/ - классы страниц с локаторами и методы взаимодействия с тестами
  - api_clients - классы для взаимодействия с api тестами
  - tests/ - тестовые сценарии
  - conftest.py - настройка драйвера для Selenium, базовый URL для api тестов
  - .github/workflows - сценарий запуска тестов на github


# Запуск
  - Клонировать репозиторий: git clone https://github.com/Alex199777/test_qa_practice.git
  - Установить зависимости: pip install -r requirements.txt
  - pytest/tests/ui    запуск ui тестов
  - pytest/tests/api   запуск api тестов
  - Запуск всех тестов: pytest

# Запуск в облаке
    - Перейти в Actions нажать  Run workflow
