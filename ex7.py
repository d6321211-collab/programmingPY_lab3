n = int(input("Enter n (at least 2): "))

first = float(input("Enter value: "))
second = float(input("Enter value: "))

if second > first:
 first, second = second, first

for i in range(n - 2):
    x = float(input("Enter value: "))
    if x > first:
      second = first
      first = x
    elif x > second:
      second = x

print("Two largest values:", first, second)
