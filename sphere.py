radius = float(input("enter your desired radius"))
def calculatevolume(radius) :
    volume = (4/3 * 3.14 * radius**3)
    return volume
sphere = calculatevolume(radius)
print(round(sphere, 0))