from setuptools import setup

setup(name='lawr',
      version='0.1',
      description='Удобный класс для работы с файлами.',
      packages=['lawr'],
      author_email='BusinessJson6@gmail.com',
      zip_safe=False)


# Официальный сайт репозитория - https://pypi.org/
# Полная инструкция (google): Как опубликовать модуль на "pypi.org"

# ПОДГОТОВКА:
# - Создать пустую папку "PyPi".
# - В ней создать ПАПКУ "lawr" с файлами (кодом) который хотим опубликовать.
# - В ней создать ФАЙЛ "setup.py" c СОДЕРЖИМЫМ об названии "class-files_x1" и версии.

# ВЫГРУЗКА:
# - Зарегистрироваться на "pypi.org"
# - Скачать Google Authenticator + Поставить 2FA
# - Установить: pip install twine | pip install setuptools
# - Войдите в директорию модуля - cd class_file
# - Команда №1 (Делает архив из кода) - python setup.py sdist
# - Команда №2 (Выгрузка архива в сеть) - twine upload dist/*
# - Ввод своего API token (смотреть в аккаунте)
# - УСПЕШНО когда надпись: "View at: ..."

# ИСПОЛЬЗОВАНИЕ
# pip install class-files-x1
from lawr.class_files import File