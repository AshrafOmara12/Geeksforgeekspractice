test_list = ["Gfg", 3, "is", 8]
key_list = ["name", "id"]

# Method 1
res = []
for i in range(0,len(test_list),2):
    res.append({key_list[0] :test_list[i] ,key_list[1] : test_list[i+1]})

# print(res)


# Method 2

res_1 = [{key_list[0] :test_list[i] ,key_list[1] : test_list[i+1]}
                for i in range(0,len(test_list),2)]

print(res_1)