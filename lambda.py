#list comprehension
# new_list = [expression for member in iterable]
squares = [i * i for i in range(10)]

#new_list = [expression for member in iterable (if conditional)]
sentence = 'the rocket came back from mars'
vowels = [i for i in sentence if i in 'aeiou']

#new_list = [expression (if conditional) for member in iterable]
original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
prices = [i if i > 0 else 0 for i in original_prices]

# walrus operator --> :=
cities = ['Austin', 'Tacoma', 'Topeka', 'Sacramento', 'Charlotte']
temps = {city: [0 for _ in range(7)] for city in cities}

numbersList = [1, 2, 3]
str_list = ['one', 'two']
numbers_tuple = ('ONE', 'TWO', 'THREE', 'FOUR')

# Notice, the size of numbersList and numbers_tuple is different
result = zip(numbersList, numbers_tuple)
{(1, 'ONE'), (2, 'TWO'), (3, 'THREE')}
# Converting to set
result_set = set(result)
result = zip(numbersList, str_list, numbers_tuple)
{(1, 'one', 'ONE'), (2, 'two', 'TWO')}

name = ['raj','rajesh','john','tom']
marks = [83,85,96]

record2 = dict()
for i,j in list(zip(name,marks)):
    record2.update({i: j})

#3 how to get Tom with 0 marks?
#{'raj': 83, 'rajesh': 85, 'john': 96,'tom':0}

record3 = {i:j for i,j in zip(name,marks)}

print(record3)

mydict = {'a':1,'b':2,'c':3,'d':4}
record4 = {i:j**2 for i,j in mydict.items()}
print(record4)
