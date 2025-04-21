import sys

# Read input values (all 15 selections at once)
inputs = list(map(int, sys.stdin.read().split()))

chpt_list = [None] * 16  # Index 1 to 15 are valid
at_least_one = False
output = ""

# Fill chapter selection (1 = selected, 0 = not selected)
for i in range(1, 16):
    chpt_list[i] = inputs[i - 1] == 1
    if chpt_list[i]:
        at_least_one = True

# Build output
i = 1
while i <= 15:
    if chpt_list[i]:
        start = i
        end = i
        # Look ahead to find consecutive selected chapters
        while end + 1 <= 15 and chpt_list[end + 1]:
            end += 1

        if end - start + 1 >= 3:
            output += f"{start}-{end} "
            i = end + 1
        else:
            output += f"{i} "
            i += 1
    else:
        i += 1

# Final print
if not at_least_one:
    print("None ")
else:
    print(output)
