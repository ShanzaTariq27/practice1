numbers = (4, 8, 15, 16, 23, 42)

def stats(nums):
    return min(nums), max(nums), sum(nums) / len(nums)

lo, hi, avg = stats(numbers)
print(f"{lo} {hi} {avg}")

def grade(marks, passing=50):
    if marks >= passing:
        return "Pass"
    else:
        return "Fail"

print(f"{grade(55)} {grade(35)}")
