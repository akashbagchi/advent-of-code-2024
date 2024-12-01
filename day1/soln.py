list1 = []
list2 = []

with open('./input.txt', 'r') as file:
    for line in file:
        num1, num2 = map(int, line.split())
        list1.append(num1)
        list2.append(num2)

list1.sort()
list2.sort()

differences = [abs(a-b) for a, b in zip(list1, list2)]
total = sum(differences)

print('Difference between the two lists: ', total)

counts = {}
similarityScore = 0
for item in list2:
    counts[item] = counts.get(item, 0) + 1

for item in list1:
    if item in list2:
       similarityScore += item * counts[item]

print('The similarity score is: ', similarityScore)
