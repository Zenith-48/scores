scores = input("Enter scores separated by space: ").split()
scores = list(map(int, scores))

total = sum(scores)
average = total / len(scores)

print("Sum of scores:", total)
print("Average of scores:", average)
