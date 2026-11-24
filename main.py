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






# ===== BAB 5: Perulangan =====
for x in range(5):
    print("Halo Python.")

fruits = ['Apple', 'Banana', 'Mango', 'Durian']
for fruit in fruits:
    print(fruit)

for x in "indonesia":
    print(x)

counter = 0
while counter < 5:
    print(counter)
    counter += 1

for x in range(5):          # break
    print(x)
    if x == 3:
        break

for x in range(10):         # continue: hanya cetak ganjil
    if x % 2 == 0:
        continue
    print(x)









# ===== BAB 6: Lists dan Dictionaries =====
animals = ["Ayam", "Bebek", "Cicak"]
print(animals[1])     # Bebek
print(animals[-1])    # Cicak
print(animals[-2])    # Bebek

animals.append("Domba")
animals.insert(2, "Buaya")
print(animals)        # ['Ayam', 'Bebek', 'Buaya', 'Cicak', 'Domba']

animals = ["Ayam", "Bebek", "Cicak"]
animals.remove("Bebek")
print(animals)        # ['Ayam', 'Cicak']

animals = ["Ayam", "Bebek", "Cicak"]
animals.pop()
print(animals)        # ['Ayam', 'Bebek']
animals.pop(0)
print(animals)        # ['Bebek']
animals.clear()
print(animals)        # []

animals = ["Ayam", "Bebek", "Cicak"]
animals.extend(["Domba", "Elang", "Gajah"])
print(animals)
print(["Apel", "Mangga"] + ["Durian", "Jeruk"])

# Dictionaries
firstPerson = {"first_name": "Hana", "last_name": "Malika", "age": 10}
print(firstPerson['first_name'])   # Hana
print(firstPerson.get('age'))      # 10
print(firstPerson.keys())          # dict_keys(['first_name', 'last_name', 'age'])
print(firstPerson.values())        # dict_values(['Hana', 'Malika', 10])

firstPerson['weight'] = 12
firstPerson['age'] = 15
firstPerson.update({"hair_color": "black"})
print(firstPerson)

firstPerson.pop("age")
print(firstPerson)
firstPerson.clear()
print(firstPerson)                 # {}








# ===== BAB 7: Function =====
def belajar_python():
    print("Halo")

belajar_python()

def belajar_python(name):
    print("Halo, Saya %s" % name)

belajar_python("Rizqi")

def belajar_python(name, age):
    print("Halo, Saya %s. Umur saya %d" % (name, age))

belajar_python("Rizqi", 30)
belajar_python(age=25, name="Fika")     # keyword arguments

def belajar_python(*names):             # arbitrary arguments
    for name in names:
        print("Halo, Saya %s" % name)

belajar_python("Rizqi", "Fika", "Yudi")

def belajar_python(**student):          # arbitrary keyword arguments
    print("Halo, Saya %s. Umur Saya %d" % (student['name'], student['age']))

belajar_python(age=20, name="Rizqi")

def belajar_python(name="Alien"):       # default value
    print("Halo, Saya %s" % name)

belajar_python()








# ===== BAB 8: Class dan Object =====
class Cat:
    color = "black"

cat1 = Cat()
print(cat1.color)      # black

class Cat:
    color = "black"

    def __init__(self, color):
        self.color = color

cat1 = Cat("orange")
print(cat1.color)      # orange

class Cat:
    def say(self):
        print("Meong..meong")

cat1 = Cat()
cat1.say()

class Cat:
    color = "black"

    def say(myParam):  # "self" boleh diganti nama lain
        print("My color is %s" % myParam.color)

cat1 = Cat()
cat1.say()