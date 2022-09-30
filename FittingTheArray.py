# Method 1
# l1 = [67, 35, 29, 2, 22, 58, 69, 67, 93, 56, 11, 42, 29]
# l2 = [73, 21, 19, 84, 37, 98, 24, 15, 70, 13, 26, 91, 80]
def is_fit(l1,l2,n):
    l1.sort()
    l2.sort()
    l3 = list(zip(l1,l2))
    result = []
    for i in l3:
        if i[0] <= i[1]:
            result.append('yes')
        else:
            result.append('no')
    print(result)
    if "no" in result:
        return('no')
    else:
        return('yes')
l1 = [7, 5, 3, 2]
l2 = [5, 4, 8, 7]
n = len(l1)
print(is_fit(l1,l2,n))
