N = int(input("Введите количество слов: "))
c = ""
for i in range (1,N+1):
    a = input("Введите слово - ")
    c = str(c)+" "+str(a)
print("Результат: ",c)

