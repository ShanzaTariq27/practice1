marks = [88, 45, 92, 67, 30, 75]

passed = sum(1 for m in marks if m >= 50)
avg = sum(marks) / len(marks)
highest = max(marks)
lowest = min(marks)

print(f"Passed: {passed}")
print(f"Average: {avg:.1f}")
print(f"Highest: {highest} Lowest: {lowest}")
