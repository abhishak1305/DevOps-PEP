# Python Practice 

## 1. Input and Output

```python
c = int(input("Enter number: "))
d = int(input("Enter number: "))

print(c, d, sep)
```

## 2. condition and ternary operator

```python
if 20 <= temp <= 50: print("Temperature is in range")
status = "Adult" if age >= 18 else "Minor"

print(temp , status)
```
## 3. function

```python
def solved(age,name,list1):
    return (len(list1),name,age)

list1 = [1,20,3,44,5]
list1.sort()
ans = solved(12,"abhishak",list1)
print (ans)

output: (5, 'abhishak', 12) // because it treat as tuple

def solved(age, name, list1):
    return f"{len(list1)},{name},{age}"

list1 = [1, 20, 3, 44, 5]
ans = solved(12, "abhi", list1)
print(ans)

output: 5,abhi,12
```
## 4. ASCII, stoi, itos

```python
# =========================
# ASCII
# =========================

# Character -> ASCII value
ch = "a"
ascii_value = ord(ch)

print("ASCII of", ch, "=", ascii_value)

# ASCII value -> Character
ascii_value = 97
ch = chr(ascii_value)

print("Character of", ascii_value, "=", ch)


# =========================
# stoi (string -> integer)
# =========================

s = "123"
num = int(s)

print("String:", s)
print("Integer:", num)
print("Type:", type(num))


# =========================
# itos / to_string (integer -> string)
# =========================

num = 456
s = str(num)

print("Integer:", num)
print("String:", s)
print("Type:", type(s))
```
## 5. In-built

```python
# Built-in functions
len()
type()
id()
print()
input()
int()
float()
str()
bool()
list()
tuple()
set()
dict()
range()
sum()
min()
max()
abs()
round()
pow()
divmod()
sorted()
reversed()
enumerate()
zip()
map()
filter()
any()
all()
ord()
chr()
bin()
oct()
hex()
repr()
format()
open()
help()
dir()
isinstance()
issubclass()
callable()

# List methods
arr.append()
arr.extend()
arr.insert()
arr.remove()
arr.pop()
arr.clear()
arr.index()
arr.count()
arr.sort()
arr.reverse()
arr.copy()

# String methods
s.upper()
s.lower()
s.capitalize()
s.title()
s.swapcase()
s.strip()
s.lstrip()
s.rstrip()
s.split()
s.rsplit()
s.join()
s.replace()
s.find()
s.rfind()
s.index()
s.count()
s.startswith()
s.endswith()
s.isalpha()
s.isdigit()
s.isalnum()
s.isspace()
s.islower()
s.isupper()
s.istitle()

# Dictionary methods
d.keys()
d.values()
d.items()
d.get()
d.update()
d.pop()
d.popitem()
d.setdefault()
d.clear()
d.copy()
d.fromkeys()

# Set methods
s.add()
s.remove()
s.discard()
s.pop()
s.clear()
s.copy()
s.update()
s.union()
s.intersection()
s.difference()
s.symmetric_difference()
s.issubset()
s.issuperset()
s.isdisjoint()

# Tuple methods
t.count()
t.index()

# File methods
file.read()
file.readline()
file.readlines()
file.write()
file.writelines()
file.seek()
file.tell()
file.flush()
file.close()

# Useful object methods
obj.__str__()
obj.__repr__()
obj.__len__()
obj.__iter__()
obj.__next__()
```
