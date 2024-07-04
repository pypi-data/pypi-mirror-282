from datetime import datetime
from time import sleep


# Возвращает текущее время
def tm(milliseconds=False, date=False):
    if date:
        if milliseconds:
            return datetime.now().strftime("%d.%m.%Y %H:%M:%S.%f")
        if not milliseconds:
            return datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    if not date:
        if milliseconds:
            return datetime.now().strftime("%H:%M:%S.%f")
        if not milliseconds:
            return str(datetime.now()).split(" ")[1].split(".")[0]


# Возвращает строку с табуляцией (count - число пробелов)
def tb(count=4):
    return " " * count
