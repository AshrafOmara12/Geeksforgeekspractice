test_list = [5, 6, [], 3, [], [], 9]

# Method 1

l = []

for i in test_list:
    if i == []:
        continue
    else:
        l.append(i)

# print(l)

# method 2

l1 = [i for i in test_list if i !=[] ]
# print(x)

# method 3

l2 = list(filter(None,test_list))
# print(l2)

# method 4

while [] in test_list:
    test_list.remove([])

# print(test_list)

# print(help(map))

x = list(map(str, test_list))
y="".join(x)
y=list(map(int,y))
# print(y)