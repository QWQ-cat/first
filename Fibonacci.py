list_a = []
list_a.append(1)
list_a.append(1)
list_a.append(2)
k = 0
n = int(input("type a number"))
# list_a.append(list_a[0]+list_a[1])
for i in range(1, n+1):
    k = list_a[i]+list_a[i+1]
    list_a.append(k)
print(list_a)
