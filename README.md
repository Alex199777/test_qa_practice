# test_qa_practice
UI Automation Framework for qa-practice.com using Python, Selenium, and Pytest (Page Object Model)
# Стек технологий
  - Python 3.12
  - Selenium
  - Pytest
  - Pattern Page object model (POM)
  - CI/CD: ручной запуск автотестов

# Структура проекта
  - pages/ - классы страниц с локаторами и методы взаимодействия с тестами
  - tests/ - тестовые сценарии
  - conftest.py - настройка драйвера
  - .github/workflows - сценарий запуска тестов на github


# Запуск
  - Клонировать репозиторий: git clone https://github.com/Alex199777/test_qa_practice.git
  - Установить зависимости: pip install -r requirements.txt
  - Запуск всех тестов: pytest

# Запуск в облаке
    - Перейти в Actions нажать  Run workflow
