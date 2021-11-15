class Sort:

    def __init__(self, new_lst) -> None:
        """Конструктор класса, на вход принимает массив"""
        self.lst = new_lst

    def bucketSort(self) -> list:
        max_num = max(self.lst)
        bucket = [0] * (max_num + 1)
        for i in self.lst:
            bucket[i] += 1
        sort_nums = []
        for j in range(len(bucket)):
            if bucket[j] != 0:
                for y in range(bucket[j]):
                    sort_nums.append(j)
        return sort_nums
