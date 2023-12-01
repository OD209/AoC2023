WordDigits = {
    "one":"o1e",
    "two":"t2o",
    "three":"t3e",
    "four":"f4r",
    "five":"f5e",
    "six":"s6x",
    "seven":"s7n",
    "eight":"e8t",
    "nine":"n9e",
    "zero":"z0o"
}

Digits = "0123456789"

with open("Hrdy\Day1\Day1.txt","r") as f:
    Map = []

    for line in f:
        NewLine = ""
        for c in line:
            NewLine += c                
            for word in WordDigits:
                NewLine = NewLine.replace(word,WordDigits[word])
        Map.append([x for x in NewLine if x in Digits])

Solution = 0
for line in Map:
    Solution += int(line[0]+line[-1])

print(Solution)

