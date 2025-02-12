tuple1 = (0, 1, 2, 3, 4, 5)

tuple2 = tuple1
print(tuple2)

sample_list = list(tuple2)
sample_list.append(6)

tuple2 = tuple(sample_list)

print(tuple1)

print(tuple2)