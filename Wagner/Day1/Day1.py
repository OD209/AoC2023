#part 1
with open("adventofcode2023\Day1\input.txt","r") as file:

    digits = ["1","2","3","4","5","6","7","8","9"]

    number = ""
    result = 0

    for line in file:
        for character in line:
            if character in digits:
                number += character
                break
        for character in line[::-1]:
            if character in digits:
                number += character
                break
        result += int(number)
        number = ""

print(f"Task1: {result}")


#part 2
with open("adventofcode2023\Day1\input.txt","r") as file:

    numerical_digits = ["1","2","3","4","5","6","7","8","9"]
    worded_digits = ["one","two","three","four","five","six","seven","eight","nine"]
    reversed_worded_digits = [x[::-1] for x in worded_digits]

    result = 0

    for line in file:

        end = 0
        number = ""
        worded_number = ""

        for character in line.strip():
            if character in digits:
                number += character
                break
            else:
                worded_number += character
                for i in worded_digits:
                    if i in worded_number:
                        while True:
                            if i == worded_number:
                                number += str((worded_digits.index(i) + 1))
                                end = 1
                                break
                            else:
                                worded_number = worded_number[1:]
                        break
                if end == 1:
                    break 
        
        end = 0
        worded_number = ""

        for character in line.strip()[::-1]:
            if character in digits:
                number += character
                break
            else:
                worded_number += character
                for i in reversed_worded_digits:
                    if i in worded_number:
                        while True:
                            if i == worded_number:
                                number += str((reversed_worded_digits.index(i) + 1))
                                end = 1
                                break
                            else:
                                worded_number = worded_number[1:]
                        break
                if end == 1:
                    break 

        result += int(number)

print(f"Task2: {result}")
