import random
import os

noter = ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"]
modes = ["Ionian (major)","Dorian (minor)","Phygrian (minor)","lydian (major)","mixolydian (major)","aeolian (natural-minor)","locerian (minor)"]

while True:
    os.system('cls')
    x = random.randint(0,11)
    y = random.randint(0,6)
    print("Du skal spille i "+noter[x]+"-major skala med",modes[y],"["+str(y+1)+"] som mode")
    input("Trykk enter for å få ny skala!")