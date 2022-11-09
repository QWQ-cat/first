
from random import randint
a = int(input("輸入一個數字"))
b = int(input("輸入一個數字"))
c = int(input("輸入一個數字"))
sum = a+b+c
print("sum=%d" % sum)


d = float(input("輸入一個數字"))
e = float(input("輸入一個數字"))
ave = round((d+e)/2, 2)
print("ave=%f" % ave)


f = float(input("輸入作業成績"))
g = float(input("輸入測驗成績"))
h = float(input("輸入平時成績"))
grade = f*0.4+g*0.4+h*0.2
if grade >= 60:
    print("本學期成績為%f\n本學期成績及格" % grade)
else:
    print("本學期成績為%f\n本學期成績不及格" % grade)


n = int(input("輸入一個數字"))
total = 0
for i in range(1, n+1):
    total = total+i
print("1+2+3+...+%d的值為%d" % (n, total))


code = 8176
for j in range(1, 4):
    check_wait = input("請輸入密碼")
    if int(check_wait) == int(code):
        print("密碼正確")
        break
    else:
        print("密碼錯誤，可再重複輸入%d次" % (3-j))
        while (3-j == 0):
            print("帳號已被鎖定")
            break


num = int(input("輸入一個數字"))
list_1 = []
k = 1
while (k <= num):
    r = num % k
    if r == 0:
        list_1.append(k)
    k = k+1
print(list_1)


list_2 = []
p = int(input("請輸入參加人數"))
x = int(input("請輸入中獎人數"))
for m in range(1, p+1):
    list_2.insert(randint(1, m+1), m)
# print(list_2)
for q in range(x):
    print("中獎號碼:%d" % list_2[q])
