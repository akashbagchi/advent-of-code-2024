list1 = []
list2 = []

with open('input.txt', 'r') as file:
    for line in file:
        num1, num2 = map(int, line.split())
        list1.append(num1)
        list2.append(num2)

list1.sort()
list2.sort()

differences = [abs(a-b) for a, b in zip(list1, list2)]
total = sum(differences)

print(total)
