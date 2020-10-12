var_str = "Это строка" # str() не изменяемый тип итерируемый
var_str[0] # обращение по индексу
var_str[-1] # последний символ в строке
len(var_str) # длина строки
var_str[1:5] #срез строки
var_str[:5] # от нуля до пятого
var_str[::2] # шаг 2

var_int = 22 # Int неизменяемый тип
var_float = 2.33 #float неизменяемое число

var_list = [1, 2, 3, 4, 5, [1,2,3], True, 'Hello', 0.23]  # список это коллекция изменяемый тип итерируемая коллекция
list('hello')
var_list.append('test') # добавить новый элемент
var_list.insert(0,'new insert') #вставить элемент на 0 индекс
var_list.pop() #вернуть последний элемент () индекс

var_tuple = (1,2,3,4, True) #кортеж tuple неизменяемая коллекция

var_set = {1, 2, 3, 4, 5, 6, } # set множество изменяемый не индексируемый итерируемый
# a | b , a & b, a.difference(a), a.add

var_dict = {'key': 'HELLO', 1: 22, (1, 2): 33} # словарь dict изменяем итерируемый
var_dict.get('help', 'Not help')

i =0
while i < len(var_str):
    print(var_str[i])
    i += 1


for char in var_str:
    print(char)

for key, value in var_dict.items():
    print(key, value)

