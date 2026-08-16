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
