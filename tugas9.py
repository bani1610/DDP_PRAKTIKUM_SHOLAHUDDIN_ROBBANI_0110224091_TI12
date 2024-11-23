#nomer 1
print('NOMER 1')
def celcius_ke_fahrenheit(celcius):
    fahrenheit = (9/5) * celcius + 32
    return fahrenheit

print(celcius_ke_fahrenheit(0))
print(celcius_ke_fahrenheit(100))

print()

#Nomer 2
print('NOMER 2')
def ganjil_genap(bilangan):
    return bilangan % 2 == 0
print(ganjil_genap(4))
print(ganjil_genap(7))

print()
print('NOMER 3')
#nomer 3
def nilai(hasil):
    if hasil >= 60:
        return "lulus"
    else:
        return "gagal"
    
print(nilai(80))
print(nilai(60))
print(nilai(59))

print()
#nomer 4
print('NOMER 4')
def bilangan(n):
    return [i for i in range(1, n, 2)]
print(bilangan(20))