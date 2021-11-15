from FileReader import FileReader
from FileWriter import FileWriter
from Validator import Validator
from BucketSort import Sort
from SerialaizeWriter import SerialaizeWriter
from SerialaizeReader import SerialaizeReader
import argparse

parser = argparse.ArgumentParser("Input & output parser")
parser.add_argument(
    "-input",
    type=str,
    default="Lab_3\\26.txt",
    help="Input path")
parser.add_argument(
    "-output",
    type=str,
    default="Lab_3\\output.txt",
    help="Output path")
pars = parser.parse_args()



read = FileReader(pars.input)
array = Validator(read.read_file())
valid = array.count_valid_records()
invalid = array.count_invalid_records()
result = array.count_invalid_arguments()
res = array.valid_array()
res = res.sort()
writer = SerialaizeWriter('data.pickle')
writer.write_file(res)
read_ser = SerialaizeReader('data.pickle')
array_ser = read_ser.read_file()
valid_ser = array_ser.count_valid_records()
writer = FileWriter(pars.output)
writer.write_file(array_ser)


print("Валидных записей:", valid)
print("Невалидных записей:", invalid)
print("Ошибка в написании номера телефона: ", result[0])
print("Ошибка в написании веса: ", result[1])
print("Ошибка в написании СНИЛСа: ", result[2])
print("Ошибка в написании номера паспорта: ", result[3])
print("Ошибка в написании профессии: ", result[4])
print("Ошибка в написании возраста: ", result[5])
print("Ошибка в написании академического разряда: ", result[6])
print("Ошибка в написании вероисповедания: ", result[7])
print("Ошибка в написании адреса: ", result[8])
print("Валидных записей после сериализации:", valid_ser)

