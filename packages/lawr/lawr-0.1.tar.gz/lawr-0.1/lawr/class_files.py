import json  # Для работы с форматом JSON
import pathlib  # Для создания папки
import shutil  # Для удаления папки
import os  # Для удаления файлов

# ---- Ш П А Р Г А Л К А (Режимы файла) ----
# r — открывает файл только для чтения
# w — открывает файл только для записи
#      (Удаляет содержимое файла, если файл существует; если файл не существует, создает новый файл для записи)
# w+ — открывает файл для чтения и записи
#      (Удаляет содержимое файла, если файл существует; если файл не существует, создает новый файл для чтения и записи)
# a+ - открывает файл для чтения и записи
#      (Информация добавляется в конец файла)
# b - открытие в двоичном режиме

# ---- Ш П А Р Г А Л К А (Пути к файлам) ----
# Абсолютный путь (path) - показывает точное местоположение файла
#   Пример: C:\Users\st\PycharmProjects\CoursePythonIT\Lesson12\lesson12.py
# Относительный путь (path) - показывает путь к файлу относительно какой-либо "отправной точки"
#   Пример: Lesson12\lesson12.py

# ---- Ш П А Р Г А Л К А (JSON) ----
# JSON — текстовый формат обмена данными, основанный на JavaScript (похож на словарь Python)
# Выровнять формат JSON - ctrl + alt + L


# Класс для работы с файлами
class File:

    # Записать текст из "text" в файл по пути "path", на перезапись влияет "overwriting"
    @staticmethod
    def write_text(text: str, path: str, overwriting=True):
        if overwriting:
            # Открыть файл как объект и временно поместить его в переменную "file"
            with open(path, mode="w", encoding="utf8") as file:
                # Объект файл будет жить только в этом теле и по окончанию закроется и сохранится
                file.write(text)
        if not overwriting:
            # Открыть файл как объект и временно поместить его в переменную "file"
            with open(path, mode="a+", encoding="utf8") as file:
                # Объект файл будет жить только в этом теле и по окончанию закроется и сохранится
                file.write(text)

    # Прочитать текст из файла по пути "path"
    @staticmethod
    def read_text(path: str):
        # Открыть файл как объект и временно поместить его в переменную "file"
        with open(path, mode="r", encoding="utf8") as file:
            # Объект файл будет жить только в этом теле и по окончанию закроется и сохранится
            return file.read()

    # Записать словарь/список из "data" в файл по пути "path"
    @staticmethod
    def write_json(data: dict or list, path: str):
        with open(path, mode="w", encoding="utf8") as file:
            json.dump(data, file, ensure_ascii=False)  # ensure_ascii=False - Для хорошего вывода русских символов

    # Прочитать словарь из файла по пути "path"
    @staticmethod
    def read_json(path: str):
        with open(path, mode="r", encoding="utf8") as file:
            return json.load(file)

    # Создание папки и всех не хватающих папок в переданном пути. Указываем полный путь в "path"
    @staticmethod
    def create_folder(path: str):
        pathlib.Path(path).mkdir(parents=True, exist_ok=True)

    # Удаление папки и всех данных в ней по пути "path" (будь это другие файлы или папки)
    @staticmethod
    def delete_folder(path: str):
        shutil.rmtree(path, ignore_errors=True)

    # Удаление файла если он есть по пути "path"
    @staticmethod
    def delete_file(path: str):
        try:
            os.remove(path)
        except FileNotFoundError:
            pass
