fruit = {'apple':5, 'banana':8,'grape':7,'orange':3,'peach':10}

# print(fruit.keys())

# print(fruit.values())

# print(fruit.items())

# for i in fruit.items():
#     print(i)

# dictionary sort
def f1(x):
    return x[0]

def f2(x):
    return x[1]

sorted1 = sorted(fruit.items(), key=f1, reverse=True)
print(sorted1)

sorted2 = sorted(fruit.items(), key=f2, reverse=True)
print(sorted2)
