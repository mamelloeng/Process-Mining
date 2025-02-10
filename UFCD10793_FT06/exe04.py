nums=[10, 2.5, 7, 11, 7.9, "Python", True,6, 5.8 , "Listas"]

#print(type(nums[0]))
a=0;b=0;c=0;d=0
for i in nums:
    if type(i) == int:
        a+=1
    if type(i) == float:
        b+=1
    if type(i) == str:
        c+=1
    if type(i) == bool:
        d+=1
print("Inteiros: ",a)
print("Reais: ",b)
print("Strings: ",c)
print("Booleanos: ",d)

