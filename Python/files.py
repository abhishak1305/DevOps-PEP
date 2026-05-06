# Write mode
f = open("file.txt" , "w")
f.write("This is new text 2")
f.close()

# Append mode
f2 = open("file.txt" , "a")
a = f2.write(" from user")
f2.close()


# Read mode
f1 = open("file.txt" , "r")
r = f1.read()
print(r)