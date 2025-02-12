sampletup1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#del sampletup1

#print(sampletup1) # NameError: name 'sampletup1' is not defined

tuple1 = (0, 1, 2, 3, 4, 5)

sample_list = list(tuple1)
sample_list.remove(3)

tuple1 = tuple(sample_list)
print(tuple1)