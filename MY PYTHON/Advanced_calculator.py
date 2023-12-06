numbers = [5, 22, 29, 39, 19, 51, 78, 96, 84]
i = 0
while (i < len(numbers) - 1) and (numbers[i] < numbers[i+1]):
    i += 1
print(i)
print(numbers[i])

numbers[i] = numbers[i-1]
numbers[i-1] = numbers[i]

print(numbers)
