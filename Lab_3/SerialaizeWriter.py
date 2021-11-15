import pickle
from tqdm import tqdm


class SerialaizeWriter:
    """Класс для записи в файл"""

    def __init__(self, file_path) -> None:
        """Конструктор класса, на вход принимает путь к файлу"""

        self.path = file_path

    def write_file(self, array) -> None:
        """Функция записи в файл, принимает на вход сам массив для записи"""
        with open(self.path, 'wb') as write_file:
            pickle.dump(array, write_file)

