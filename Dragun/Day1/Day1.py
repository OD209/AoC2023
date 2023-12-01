with open("day1.txt") as f:
    calibrations = [line.strip() for line in f.readlines()]

total = 0

for cal in calibrations:
    score = ""
    for chr in cal:
        if chr.isdigit():
            score += chr
            break
    for chr in cal[::-1]:
        if chr.isdigit():
            score += chr
            break
    total += int(score)
print(total)


nums = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
total = 0

for cal in calibrations:
    for num in nums.keys():
        if num in cal:
            cal = cal.replace(num, num[:len(num)//2]+ nums[num]+ num[len(num)//2:])
    score = ""
    for chr in cal:
        if chr.isdigit():
            score += chr
            break
    for chr in cal[::-1]:
        if chr.isdigit():
            score += chr
            break
    total += int(score)
print(total)
