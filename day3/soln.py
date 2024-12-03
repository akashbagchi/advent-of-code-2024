import re

input = []
with open('./input.txt', 'r') as file:
    for line in file:
        input.append(line)

disabledPattern = r'don\'t\(\).*?do\(\)'
cleanedInput = re.sub(disabledPattern, '', ''.join(input), flags=re.DOTALL)

pattern = r'mul\(([0-9]+),([0-9]+)\)'
matches = re.findall(pattern, cleanedInput)

products = []
for num1, num2 in matches:
    products.append(int(num1) * int(num2))

print(sum(products))
