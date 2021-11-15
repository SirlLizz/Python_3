from tqdm import tqdm


class Validator:
    """Класс валидатора, производящий анализ данных на валидность, имеет поле массива"""
    value: list

    def __init__(self, array) -> None:
        """Конструктор класса, на вход принимает массив"""

        self.value = array

    def validation(self, index) -> dict:
        """Функция анализа и записи корректности данных, возвращает словарь"""

        result = {"telephone": self.value[index].check_telephone(),
                  "weight": self.value[index].check_weight(),
                  "snils": self.value[index].check_snils(),
                  "passport_number": self.value[index].check_passport_number(),
                  "occupation": self.value[index].check_occupation(),
                  "age": self.value[index].check_age(),
                  "academic_degree": self.value[index].check_academic_degree(),
                  "worldview": self.value[index].check_worldview(),
                  "adress": self.value[index].check_address()}
        return result.copy()

    def count_valid_records(self) -> int:
        """Функция проверки массива на количество корректных записей, возвращает их колисество"""

        count_correct = 0
        for i in tqdm(range(len(self.value)),
                      desc="Подсчёт корректных записей",
                      ncols=100):
            if not (False in self.validation(i).values()):
                count_correct += 1
        return count_correct

    def count_invalid_records(self) -> int:
        """Функция проверки массива на количество некорректных записей, возвращает их колисество"""

        count_incorrect = 0
        for i in tqdm(range(len(self.value)),
                      desc="Подсчёт некорректных записей",
                      ncols=100):
            if False in self.validation(i).values():
                count_incorrect += 1
        return count_incorrect

    def count_invalid_arguments(self):
        """Функция проверки массива на количество некорректных записей в словарях, возвращаетмассив с их колисеством"""

        rezult = []
        count_inv_telephone = 0
        count_inv_weight = 0
        count_inv_snils = 0
        count_inv_passport_number = 0
        count_inv_occupation = 0
        count_inv_age = 0
        count_inv_academic_degree = 0
        count_inv_worldview = 0
        count_inv_address = 0
        for i in tqdm(range(len(self.value)),
                      desc="Подсчёт некорректных записей  данных",
                      ncols=100):
            if not self.value[i].check_telephone():
                count_inv_telephone += 1
            if not self.value[i].check_weight():
                count_inv_weight += 1
            if not self.value[i].check_snils():
                count_inv_snils += 1
            if not self.value[i].check_passport_number():
                count_inv_passport_number += 1
            if not self.value[i].check_occupation():
                count_inv_occupation += 1
            if not self.value[i].check_age():
                count_inv_age += 1
            if not self.value[i].check_academic_degree():
                count_inv_academic_degree += 1
            if not self.value[i].check_worldview():
                count_inv_worldview += 1
            if not self.value[i].check_address():
                count_inv_address += 1
        rezult.append(count_inv_telephone)
        rezult.append(count_inv_weight)
        rezult.append(count_inv_snils)
        rezult.append(count_inv_passport_number)
        rezult.append(count_inv_occupation)
        rezult.append(count_inv_age)
        rezult.append(count_inv_academic_degree)
        rezult.append(count_inv_worldview)
        rezult.append(count_inv_address)
        return rezult

    def valid_array(self) -> list:
        correct = []
        for i in tqdm(range(len(self.value)),
                      desc="Создание файла корректных записей",
                      ncols=100):
            if not (False in self.validation(i).values()):
                correct.append(self.value[i])
        correct = Validator(correct)
        return correct


    def sort(self) -> list:
        max_num = 0;
        for i in tqdm(range(len(self.value)), desc="Сортировка корректных записей",ncols=100):
            if self.value[i].get_weight() > max_num:
                max_num = self.value[i].get_weight()

        bucket = [0] * (max_num + 1)
        for i in range(len(self.value)):
            if bucket[self.value[i].get_weight()] == 0:
                bucket[self.value[i].get_weight()] = []
            bucket[self.value[i].get_weight()].append(self.value[i])
        sort_nums = []
        for j in range(len(bucket)):
            if bucket[j] != 0:
                for y in range(len(bucket[j])):
                    sort_nums.append(bucket[j][y])
        sort_nums = Validator(sort_nums)
        return sort_nums
