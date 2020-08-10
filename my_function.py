matn = 'salom hammaga!'
print(matn[0:8])
print(matn[-1])
print(matn[:5])
print(matn[6:])
print(matn[::2])
print(matn[::-1])
print(matn[:5]+matn[6:])

#funksiyalar
def summa(a,b):
    print(a+b)

a = float(input('1-son'))
b = float(input('2-son'))
summa(a,b)