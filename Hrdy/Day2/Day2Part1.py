RED = 12
GREEN = 13
BLUE = 14

SumID = 0

with open("Hrdy\Day2\Day2.txt","r") as f:
    Games = []
    for line in f:
        Round = []
        Possible = True  
        Id = int(line.split(":")[0].split(" ")[1])
        for Game in [line.split(":")[1].strip().split("; ")]:          
            for g in Game:                
                Play= {}
                for p in g.split(", "):
                    Play[p.split(" ")[1].strip()] = int(p.split(" ")[0].strip())
                    if p.split(" ")[1].strip() == "red" and int(p.split(" ")[0].strip()) > 12:
                        Possible = False
                    elif p.split(" ")[1].strip() == "green" and int(p.split(" ")[0].strip()) > 13:
                        Possible = False
                    elif p.split(" ")[1].strip() == "blue" and int(p.split(" ")[0].strip()) > 14:
                        Possible = False
            if Possible:
                SumID +=Id                
                Round.append(Play)
        Games.append(Round)
print(SumID)