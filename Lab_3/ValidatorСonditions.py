import re


class ValidatorСonditions:
    """Класс валидации словаря, имеет поле словаря"""

    dictionary: dict

    def __init__(self, d) -> None:
        """конструктор, принимает на вход словарь"""

        self.dictionary = d.copy()

    def check_telephone(self) -> bool:
        """Функция проверки номера телефона на валидность"""

        pattern = "\\+(7)\\-\\(\\d{3}\\)\\-\\d{3}\\-\\d{2}\\-\\d{2}$"
        if re.match(pattern, self.dictionary["telephone"]):
            return True
        return False

    def check_weight(self) -> bool:
        """Функция проверки веса человека на валидность"""

        if isinstance(self.dictionary["weight"], int):
            if 20 < self.dictionary["weight"] < 200:
                return True
        return False

    def get_weight(self) -> int:
        if isinstance(self.dictionary["weight"], int):
            return int(self.dictionary["weight"])

    def check_snils(self) -> bool:
        """Функция проверки СНИЛСа на валидность"""

        pattern = "^\\d{11}$"
        if re.match(pattern, self.dictionary["snils"]):
            return True
        return False

    def check_passport_number(self) -> bool:
        """Функция проверки номера паспорта на валидность"""

        if isinstance(self.dictionary["passport_number"], int):
            if 100000 <= self.dictionary["passport_number"] < 1000000:
                return True
        return False

    def check_occupation(self) -> bool:
        """Функция проверки названия профессии на валидность"""

        pattern = "^([а-яА-Я]|-| ){3,}$"
        if re.match(pattern, self.dictionary["occupation"]):
            return True
        return False

    def check_age(self) -> bool:
        """Функция проверки возраста человека на валидность"""

        if isinstance(self.dictionary["age"], int):
            if 0 <= self.dictionary["age"] < 130:
                return True
        return False

    def check_academic_degree(self) -> bool:
        """Функция проверки академического разряда на валидность"""

        pattern = "Бакалавр|Кандидат наук|Специалист|Магистр|Доктор наук|"
        if re.match(pattern, self.dictionary["academic_degree"]):
            return True
        return False

    def check_worldview(self) -> bool:
        """Функция проверки вероисповедания на валидность"""

        pattern = "^.+(?:изм|анство)$"
        if re.match(pattern, self.dictionary["worldview"]):
            return True
        return False

    def check_address(self) -> bool:
        """Функция проверки адреса проживания на валидность"""

        pattern = "(?:ул\\.|Аллея) (?:им[\\.\\s]|)[^\\s]+ [^\\s]*(?:\\s|)\\d+"
        if re.match(pattern, self.dictionary["address"]):
            return True
        return False
