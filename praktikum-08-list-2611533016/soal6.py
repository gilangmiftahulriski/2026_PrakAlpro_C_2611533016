LAST_DIGIT = 6  # change to the last digit of your NIM
daily_limit = 30000 + LAST_DIGIT * 1000
expenses = []
# Write your code below

for day in range (7):
    nilai = int(input(f"Day{day}: "))
    expenses.append(nilai)

total = 0
highest = expenses[0]
highest_day = 1
days_above_limit = 0

for i in range(len(expenses)):
    current = expenses[i]
    total += current

    if current > highest:
        highest = current
        highest_day = i + 1

    if current > daily_limit:
        days_above_limit += 1

average = total / len(expenses)

print(f"Daily limit: {daily_limit}")
print(f"Total: {total}")
print(f"Average: {average:.1f}")
print(f"Highest: day {highest_day}")
print(f"Days above limit: {days_above_limit}")