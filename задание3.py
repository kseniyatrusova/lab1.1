a = int(input("Введите год: "))
if a%4 ==0 and not(a%100==0) or a%400==0:
    print ("Год ", a, "- високосный")
else:
    print("Это год не високосный")