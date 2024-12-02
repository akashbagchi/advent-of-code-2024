def check_sequence(numbers):
    if len(numbers) < 2:
        return True

    previousNumber = numbers[0]
    increasing = None

    for i in range(1, len(numbers)):
        currentNumber = numbers[i]
        if increasing is None:
            increasing = currentNumber > previousNumber
        elif increasing and currentNumber <= previousNumber:
            return False
        elif not increasing and currentNumber >= previousNumber:
            return False

        diff = abs(currentNumber - previousNumber)
        if diff < 1 or diff > 3:
            return False

        previousNumber = currentNumber

    return True

reports = []
with open('./input.txt', 'r') as file:
    for line in file:
        reports.append([int(x) for x in line.split()])

safeCount = 0

for report in reports:
    if check_sequence(report):
        safeCount += 1
        continue

    for i in range(len(report)):
        modifiedReport = report[:i] + report[i+1:]
        if check_sequence(modifiedReport):
            safeCount += 1
            break

print(safeCount)
