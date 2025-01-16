import math

mylist = [1,4,6,0]

# Create a lambda which returns the first item in a list.
x = lambda mylist: mylist[0]

print(x(mylist))

def x2(mylist):
    return mylist[1]

print(x2(mylist))

# another example

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))


# Map a lambda which applies the logistic functionto the list [-3, -5, 1, 4] . Round each number to 4 decimal places. (ermm…. that's two nested maps)

lst = [-3, -5, 1, 4]

mapped = list(map(lambda z: round(z,2), map(lambda x: 1 / (1 + pow(math.e, -x)), lst)))

print(lst)
print(mapped)

# examples

names = ['Carina', 'Iskren', 'Ivan','Sophia']
print(sum(list(map(len,names)))/len(names))
# map applied function len()

names = [{'Carina': 44}, {'Anna': 12}, {'Ivan': 35}, {'Sophia': 10}]

filtered_list = filter(lambda x: list(x.values())[0] > 18, names)
print(list(filtered_list))

sorted_list = sorted(names, key = lambda x: list(x.keys())[0])
print(sorted_list)
