print("Halo Python")






# ===== BAB 2: Variabel dan Tipe Data =====
x = 5
y = 3
print(x + y)              # 8

a = 7.5                   # float
print(a)

myFirstName = 'Rizqi'     # single quote
myLastName = "Maulana"    # double quote
myAge = "25"              # angka sebagai string
myHobby = """Hobi saya adalah
bersepeda dan bermain game.
"""
print(myFirstName + " " + myLastName)
print("Umur saya " + myAge)
print(myHobby)

isActive = True           # boolean harus True/False (huruf kapital)
isDone = False
print(isActive, isDone)
# c = true                # error: NameError






# ===== BAB 3: Operator pada Python =====
# Aritmatika
a = 4
b = 2
print(a + b)    # 6
print(a - b)    # 2
print(a * b)    # 8
print(a / b)    # 2.0
print(a % b)    # 0
print(a ** b)   # 16

# Perbandingan
a = 3
b = 5
print(a == b)   # False
print(a != b)   # True
print(a < b)    # True
print(a <= b)   # True
print(a > b)    # False
print(a >= b)   # False

# Logika
a = 3
b = 9
print(a < 5 and b > 6)        # True
print(a < 5 and b < 6)        # False
print(a < 5 or b > 6)         # True
print(a > 5 or b < 6)         # False
print(not (a < 5 or b > 6))   # False
print(not (a > 5 or b < 6))   # True











# ===== BAB 4: Kondisi If Else =====
# Python memakai indentation untuk menentukan blok kode
if True:
    print("Benar.")

x = 5
y = 10
if x < y:
    print("nilai x lebih kecil dari y.")
if x > y:
    print("nilai x lebih besar dari y.")   # tidak dijalankan

a = 80
if a > 90:
    print("Dapat nilai A.")
elif a > 70:
    print("Dapat nilai B.")                 # dijalankan

a = 60
if a > 90:
    print("Dapat nilai A.")
elif a > 70:
    print("Dapat nilai B.")
else:
    print("Dapat nilai C.")                 # dijalankan



