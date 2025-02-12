nested_tuple = ((20, 40, 60), (10, 30, 50), "Python")

print(nested_tuple[2][0])

for i in nested_tuple:
    print("tuple", i, "elements")
    for j in i:
        print(j, end=", ")
    print("\n")

