Digits = "0123456789"
with open("Hrdy\Day1\Day1.txt","r") as f:
    Map = []
    for line in f:
        Map.append([x for x in line if x in Digits])
Result = 0
for line in Map:
    Result += int(line[0] + line[-1])

print(Result)