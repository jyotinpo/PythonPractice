# =========================
# Hackerrank RegEx problems
# =========================

# Problem-1
# You are given a string consisting only of digits 0-9, commas and dots. 
# Your task is to complete the regex_pattern defined below, which will be used to re.split() all of the , and . symbols

regex_pattern = r"[,|.]"	# 'r' is used to specify raw string and not evaluate \ character sequences. 

import re
print("\n".join(re.split(regex_pattern, raw_input())))

# Problem-2
# Detect Floating Point Number

import re
for i in range(int(raw_input())):
    print bool(re.search(r"^[+|-]?\d*\.\d+$",raw_input().strip()))

# Problem - 3
# Find the first occurrence of an alphanumeric character in  (read from left to right) that has consecutive repetitions.

import re
m = re.search(r'([0-9]|[a-z]|[A-Z])\1+', input().strip())
print(m.group(1) if m else -1)
