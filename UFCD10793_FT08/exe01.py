xs = {1, 2, 3}
aux = 1 in xs
print(aux)
a = set('abracadabra')
print(a)
b = set('alacazam')
print(b)
c = a - b
print(c)
c = a | b
print(c)
c = a & b
print(c)
c = a ^ b
print(c)

thisset = {"apple", "banana", "cherry"}
print(thisset)

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

print(len(thisset))

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

set1 = {"abc", 34, True, 40, "male"}

myset = {"apple", "banana", "cherry"}
print(type(myset))

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

student_id = {112, 114, 116, 118, 115}
print('Student ID:', student_id)

vowel_letters = {'a', 'e', 'i', 'o', 'u'}
print('Vowel Letters:', vowel_letters)

mixed_set = {'Hello', 101, -2, 'Bye'}
print('Set of mixed data types:', mixed_set)

empty_set = set()

empty_dictionary = {}

print('Data type of empty_set:', type(empty_set))

numbers = {2, 4, 6, 6, 2, 8}
print(numbers)

numbers = {21, 34, 54, 12}

print('Initial set:', numbers)

numbers.add(32)

print('Updated set:', numbers)

companies = {'Lacoste', 'Ralph Lauren'}
tech_companies = {'apple', 'google', 'apple'}

companies.update(tech_companies)

print(companies)

languages = {'Swift', 'Python', 'Java'}

print('Initial set:', languages)

removedValue = languages.discard('Java')

print('Set after remove():', languages)

fruits = {"Apple", "Peach", "Mango"}

for fruit in fruits:
    print(fruit)

even_numbers = {2,4,6,8}
print('Set:', even_numbers)

print('Total Elements:', len(even_numbers))

A = {1, 3, 5}
B = {0, 2, 4}

print('Union using |:', A | B)

print('Union using union():', A.union(B))

A = {1, 3, 5}
B = {1, 2, 3}

print('Intersection using &:', A & B)
print('Intersection using intersection():', A.intersection(B))

A = {2, 3, 5}
B = {1, 2, 6}

print('Difference using &:', A - B)
print('Difference using difference():', A.difference(B))

A = {2, 3, 5}
B = {1, 2, 6}

print('using ^:', A ^ B)
print('using symmetric_difference():', A.symmetric_difference(B))

A = {1, 3, 5}
B = {3, 5, 1}

if A == B:
    print('A and B are equal sets')
else:
    print('A and B are not equal sets')