PASS_MARK = 50
DISTINCTION_BAND = 70

scores = [72, 38, 55, 91, 40, 27, 66, 83, 45, 39]

distinction = []
passed = []
failed = []

for score in scores:
    if score >= DISTINCTION_BAND:
        distinction.append(score)
    elif score >= PASS_MARK:
        passed.append(score)
    else:
        failed.append(score)

print(f"{len(scores)} learners sat the paper")
print(f"{(len(passed) + len(distinction))} passed, {len(failed)} did not")

average = sum(scores) / len(scores)
print(f"Average: {average:.1f}")
print(f"Highest: {max(scores)}")
print(f"Lowest: {min(scores)}")

passing_average = sum(passed) / len(passed)
print(f"Passing average: {passing_average}")

pass_rate = (len(passed) + len(distinction)) / len(scores) * 100
print(f"Pass rate: {pass_rate:.0f}%")

print(f"Needs support: {sorted(failed)}")
