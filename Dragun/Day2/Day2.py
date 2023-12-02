with open("day2.txt") as f:
    games = [i.strip() for i in f.readlines()]

red, green, blue = 12, 13, 14
total1 = 0

for game in games:
    possible = True
    game = game.split(": ")
    id =  int(game[0].split(" ")[1])
    rounds = [x.split(", ") for x in game[1].split("; ")]
    
    for round in rounds:
        for cube in round:
            value, color = int(cube.split(" ")[0]), cube.split(" ")[1]
            if color == "red" and value > red or color == "green" and value > green or color == "blue" and value > blue:
                possible = False
    if possible:
        total1 += id

print(total1)

total2 = 0

for game in games:
    rounds = [x.split(", ") for x in game.split(": ")[1].split("; ")]
    reds, greens, blues = 0, 0, 0

    for round in rounds:
        for cube in round:
            value, color = int(cube.split(" ")[0]), cube.split(" ")[1]
            if color == "red":
                if value > reds:
                    reds = value
            elif color == "green":
                if value > greens:
                    greens = value
            elif color == "blue":
                if value > blues:
                    blues = value

    total2 += reds * greens * blues

print(total2)
