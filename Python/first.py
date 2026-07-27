# 1. ----------------------------------------Taking User Input-----------------------------------------------

var1 = input("Enter 1: ")
var2 = input("Enter 2: ")

print("Answer:", var1 + var2)

## Adding Numbers Correctly

var1 = int(input("Enter 1: "))
var2 = int(input("Enter 2: "))

print("Answer:", var1 + var2)

# 2. ------------------------------------------------Loops----------------------------------------------------

## For Loop

for i in range(1, 10):
    print(i)

## While Loop

i = 1

while(i < 10):
    print(i)
    i += 1

# 3. -----------------------------------------------File Operations----------------------------------------------

## Create or Write to a File


f = open("file.txt", "w")

## Explanation

# * `"w"` = write mode
# * Creates file if it does not exist
# * Removes old content if file already exists

---

## Read a File

f = open("file1.txt", "r")

## Explanation

# * `"r"` = read mode
# * File must already exist
# * Otherwise error occurs

## Open and Print File Object

f = open("file.txt", "r")
print(f)

# Better File Reading Example

f = open("file.txt", "r")

content = f.read()
print(content)

f.close()

## Explanation

# * `read()` reads file content
# * `close()` closes the file properly


# Quick Summary Table

# | Mode  | Meaning         |
# | ----- | --------------- |
# | `"r"` | Read file       |
# | `"w"` | Write file      |
# | `"a"` | Append to file  |
# | `"x"` | Create new file |

# ------------------------------------------------ try - exception --------------------------------------

# try:
#     num1 = int(input("Enter number: "))
#     print(10 / num1)

# except:
#     print("Error occurred")