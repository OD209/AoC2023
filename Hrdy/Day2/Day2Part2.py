Power = 0

with open("Hrdy\Day2\Day2.txt","r") as f:
    Games = []
    for line in f:
        Round = []
        Red,Green,Blue = 0,0,0
        Id = int(line.split(":")[0].split(" ")[1])
        for Game in [line.split(":")[1].strip().split("; ")]:          
            for g in Game:                
                Play= {}
                for p in g.split(", "):
                    Play[p.split(" ")[1].strip()] = int(p.split(" ")[0].strip())
                    if p.split(" ")[1].strip() == "red" and int(p.split(" ")[0].strip()) > Red:
                        Red = int(p.split(" ")[0].strip())
                    elif p.split(" ")[1].strip() == "green" and int(p.split(" ")[0].strip()) > Green:
                        Green = int(p.split(" ")[0].strip())
                    elif p.split(" ")[1].strip() == "blue" and int(p.split(" ")[0].strip()) > Blue:
                        Blue = int(p.split(" ")[0].strip())
                Round.append(Play)
            Power += Red*Blue*Green           
        Games.append(Round)
print(Power)