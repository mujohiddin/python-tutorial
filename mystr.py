#berilgan satrdagiistakgan so' o'zgartirish 
satr = input('Matn kiriting:')
print(satr)
satr_eski=input("Eski so'z:")
satr_yangi=input("Yangi so'z")
satr_uzunligi = len(satr_eski) 
while satr.find(satr_eski) > 0:
    i = satr.find(satr_eski)
    satr = satr[:i] + satr_yangi + satr[i+satr_uzunligi:] 
    print('')
print(satr) 
matn = ['mening matnim']
print(matn[0:5])

#dastur uz for sikl bo'yichq 2-misol

son1 = int(input("1-sonni kiriting:"))
son2 =int(input("2-sonni kiriting:"))
for i in range(son1,son2+1):
    print(i)
print("2 son orasidagi sonlar sanogi:", abs(son1-son2))

    