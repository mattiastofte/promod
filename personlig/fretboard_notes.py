from colorama import Fore
from colorama import Style
import os
import random


notes = ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"]

def check_note(x,y,spacing,string):
    if y+string[1] == x or y+string[1] == x+12:
        if y < 12:
            print(f"  {Fore.GREEN}*{Style.RESET_ALL}  |"+str(" "*spacing), end = '')
        else:
            print(f"  {Fore.GREEN}*{Style.RESET_ALL}  "+str(" "*spacing), end = '')
    else:
        if y < 12:
            print("     |"+str(" "*spacing), end = '')
        else:
            pass


def print_fretboard(note):
    print("    ", end = '')
    for count in range(13):
        if count < 12:
            print(" ["+str(count)+"] |", end = '')
        else:
            print(" ["+str(count)+"]")
    print("     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    for string in [("E",7),("B",2),("G",10),("D",5),("A",0),("E",7)]:
        print("["+string[0]+"] ", end = '')
        for count in range(13):
            if count < 9:
                check_note(note,count,0,string)
            elif count == 12:
                check_note(note,count,1,string)
            else:
                check_note(note,count,1,string)
        print("\n     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            
while True:
    os.system('cls')
    note = random.randint(0,11)
    print("Du skal spille i alle "+notes[note]+"-er på fretboardet.\n")
    input("Trykk enter for å få fasit!")
    os.system('cls')
    print("\n")
    print_fretboard(note)
    input("\nTrykk enter for å få en ny note!")