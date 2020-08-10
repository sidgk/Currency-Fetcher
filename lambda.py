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

matrix = [[0, 0, 0],[1, 1, 1],[2, 2, 2]]


