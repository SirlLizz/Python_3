import json

from ValidatorСonditions import ValidatorСonditions


class FileReader:
    """Класс для чтения из файла"""

    def __init__(self, file_path) -> None:
        """Конструктор класса, на вход принимает путь к файлу"""

        self.path = file_path

    def read_file(self) -> list:
        """Функция чтения из файла, возвращает массив считаных значений"""

        array: list = []
        data = json.load(open(self.path, encoding="windows-1251"))
        for i in data:
            array.append(ValidatorСonditions(i.copy()))
        return array
