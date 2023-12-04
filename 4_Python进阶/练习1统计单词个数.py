s='hello tank tank say hello sb sb'

l = s.split()
dict = {}

for item in l:
    if item in dict:
        dict[item] += 1
    else:
        dict[item] = 1

print(dict)