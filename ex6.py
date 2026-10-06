n = int(input("Enter n: "))

ascending = True
descending = True

previous = int(input("Enter number: "))

for i in range(n - 1):
 current = int(input("Enter number: "))
if current <= previous:
 ascending = False
if current >= previous:
 descending = False
previous = current

if ascending:
 print("ascending sequence")
elif descending:
 print("descending sequence")
else:
 print("neither ascending nor descending sequence")
