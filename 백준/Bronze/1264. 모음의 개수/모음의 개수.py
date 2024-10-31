import re

while True:
    text = input().strip()
    if text == "#":
        break
    pattern = r"[aeiouAEIOU]"
    vowels_count = len(re.findall(pattern, text))
    print(vowels_count)
