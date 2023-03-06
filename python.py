for num in range(151):
    print(num)


for num2 in range(5, 1001, 5):
    print(num2)


for l in range(1, 101):
    if l % 10 == 0:
        print("Coding Dojo")
    elif l % 5 == 0:
        print ("Coding")
    else:
        print (l)


total = 0
for i in range(1, 500000, 2):
    total += i
print(total)
# OR
total = 0
for i in range(0, 500000):
    if i % 2 == 1:
        total += i
print(total)


for j in range(2018, 0, -4):
    print(j)


lowNum = 0
highNum = 101
mult = 5
for w in range(lowNum, highNum, mult):
    print(w)
