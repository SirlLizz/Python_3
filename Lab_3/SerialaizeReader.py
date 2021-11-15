import pickle

from ValidatorСonditions import ValidatorСonditions


class SerialaizeReader:
    """Класс для чтения из файла"""

    def __init__(self, file_path) -> None:
        """Конструктор класса, на вход принимает путь к файлу"""

        self.path = file_path

    def read_file(self) -> list:
        """Функция чтения из файла, возвращает массив считаных значений"""

        with open(self.path, 'rb') as read_file:
            return pickle.load(read_file)
