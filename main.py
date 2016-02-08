# vowel removal

sentence = "List Comprehensions are the Greatest!".lower()

vowels = ['a', 'e', 'i', 'o', 'u']


def kill_vowels(sentence):
    return [letter for letter in sentence if letter not in vowels]

print(kill_vowels(sentence))

# list of water temps by day

with open("dataset.txt") as my_file:
    contents = my_file.readlines()


def water_and_date(item):
    return [line.split(',')[-2:] for line in item]

# from string to float

last_two = water_and_date(contents)
print(last_two)


def water_list(data):
    return [float(flt[0]) for flt in data[1:]]

# from C to F in int form

water_data_list = water_list(last_two)
print(water_data_list)


def c_to_f(data):
    return [int((temp * 1.8) + 32) for temp in data]

print(c_to_f(water_data_list))
