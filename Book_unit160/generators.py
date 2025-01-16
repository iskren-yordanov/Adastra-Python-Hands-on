def my_list(n): 
    i = 0 
    l = []
    while i <n: 
        l.append(i) 
        i += 1
    return l

# We can change this function# into a generator function
def my_gen(n): 
    i = 0
    while i < n: 
        yield i 
        i += 1

g = my_gen(25)
print(type(g))

for x in range(23): 
    print(next(g))

print(next(g))
print(next(g))



# in genrators if we exceed we get an Expection of StopIteration
# FOR loops handle this automatically

#print('pause')
#print(next(g))

# we got 0 and 1 using NEXT, and the rest using FOR cycle
for x in g:
    print(x)


# example of a generator withot a Generator

class OneTwoThree: 
    def __iter__(self): 
        value = 0

        class OneTwoThreeIterator: 
            def __next__(self): 
                nonlocal value 
                value += 1 
                if value > 3: 
                    raise StopIteration() 
                return value

        return OneTwoThreeIterator()

x = OneTwoThree()
for i in x: 
    print(i) # prints 1 then 2 then 3

# this creates in memory so its slow if this is a big list
#bad = [x*x for x in range(10**9)]

# this generates a generator that is used only when called (no inmemory usage)
good = (x*x for x in range(10*9))
print(next(good))
print(sum(good)) # we can use agregates on a generator 'list'

# print current work directory
import os
print(os.getcwd())

with open('sells.log', 'r') as file:
    pizza_col = (line.split()[3] for line in file)
    per_hour = (int(x) for x in pizza_col if x!= 'N/A')
    print("Total pizzas sold = ", sum(per_hour))

# TODO: check if todo tree works
