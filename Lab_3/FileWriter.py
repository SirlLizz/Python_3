import json
from tqdm import tqdm


class FileWriter:
    """Класс для записи в файл"""

    def __init__(self, file_path) -> None:
        """Конструктор класса, на вход принимает путь к файлу"""

        self.path = file_path

    def write_file(self, array) -> None:
        """Функция записи в файл, принимает на вход сам массив для записи"""

        tmp = []
        for i in tqdm(range(len(array.value)),
                      desc="Запись результата в файл",
                      ncols=100):
            if not (False in array.validation(i).values()):
                tmp.append(array.value[i].dictionary.copy())
        json.dump(
            tmp,
            open(
                self.path,
                "w",
                encoding="windows-1251"),
            ensure_ascii=False,
            sort_keys=False,
            indent=4)
