sammy = {'username': 'sammy-shark', 'online': True, 'followers': 987}
jesse = {'username': 'JOctopus', 'online': False, 'points': 723}

print(sammy.values())
print(sammy.items())

for key, value in sammy.items():
    print(key, 'is the key for value', value)

for common_key in sammy.keys() & jesse.keys():
    print(sammy[common_key], jesse[common_key])

jesse.update({'followers': 481})
del jesse['points']
print(jesse)

keys = ['a', 'b', 'c']
values = [1, 2, 3]
dictionary = dict(zip(keys, values))
print(dictionary)