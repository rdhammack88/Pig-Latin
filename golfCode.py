#Golf Score Card

#function to determine how well you scored per hole 
def golfScore(par, strokes):
    if strokes == 1:
        print("Hole-in-one!")
    elif strokes <= par - 3:
        print("Double Eagle")
    elif strokes <= par - 2:
        print("Eagle")
    elif strokes == par - 1:
        print("Birdie")
    elif strokes == par:
        print("Par")
    elif strokes == par + 1:
        print("Bogey")
    elif strokes == par + 2:
        print("Double Bogey")
    elif strokes >= par + 3:
        print("Go Home!")
    else:
        print("Change Me")
  

#user input for hole "par" & "stroke count"
holePar = input("What is the par of the current hole? ")
holeStrokes = input("How many strokes did it take? ")
par = int(holePar)
strokes = int(holeStrokes)
#prints hole stats
golfScore(par, strokes)

#prints hole close message
if int(holeStrokes) <= par and int(holeStrokes) > 1:
    print("Great Job Champ! You're on your way to being the next Tiger Woods!") 
elif int(holeStrokes) == 1:
    print("Amazing Job Champ! Are you sure you're not Tiger!")
elif int(holeStrokes) == par + 2:
    print("Better go back to the practice course!")
