from colorama import*
from random import*
from os import*
from codecs import*
from time import*

startMsg = "BrawlBox Emulator BSE v1\nCommands:\n   c (view coins)\n   Boxes:\n      b (open box)\n      g (open big box)\n      m (open mega box)\n   d (debug mode)\n   p (view brawlers)\n   u (upgrade the brawler)\n   e (execute python script)\n   / (clear console)\n   s (view source code)"
print(startMsg)
coins = [0]
powerPoints = [{}]
debugMode = False

def read(key):
    try:
        f = open(key+'.py', 'r')
        data = f.read()
        f.close()
        exec(key + '[0]=' + data)
    except:
        f = open(key+'.py', 'w')
        f.close()

def save(key, val):
    f = open(key+'.py', 'w')
    f.write(val)
    f.close()

rare_perc = ["El Primo", "Barley", "Poco", "Rosa"]
d_rare_chance = 2.5
rare_chance = d_rare_chance

superrare_perc = ["Jacky", "Penny", "Rico", "Carl"]
d_superrare_chance = 1
superrare_chance = d_superrare_chance

epic_perc = ["Piper", "Edgar", "Pam", "Frank","Bea", "Grom", "Bibi", "Griff"]
d_epic_chance = 0.5
epic_chance = d_epic_chance

mythic_perc = ["Bairon", "Squik", "Mortis", "Tara", "Gene", "Max", "Sprout", "Mister pi"]
d_mythic_chance = 0.1
mythic_chance = d_mythic_chance

lega_perc = ["Spike", "Crow", "Leon", "Sandy", "Amber", "Meg"]
d_lega_chance = 0.05
lega_chance = d_lega_chance

perc = [[]]
perc_levels = [{}]

max_perc_count = len(rare_perc) + len(superrare_perc) + len(epic_perc) + len(mythic_perc) + len(lega_perc)
            
read("coins")
read("powerPoints")
read("perc")
read("perc_levels")

brawler_str = "Brawler: "

lvl2_coin_cost = 50
lvl2_star_cost = 25

lvl3_coin_cost = 100
lvl3_star_cost = 50

lvl4_coin_cost = 150
lvl4_star_cost = 75

lvl5_coin_cost = 200
lvl5_star_cost = 100

lvl6_coin_cost = 400
lvl6_star_cost = 200

lvl7_coin_cost = 800
lvl7_star_cost = 400

lvl8_coin_cost = 1600
lvl8_star_cost = 800

lvl9_coin_cost = 3200
lvl9_star_cost = 1600

box_count = [0]
big_box_count = [0]
mega_box_count = [0]
read("box_count")
read("big_box_count")
read("mega_box_count")

time_ = [-1]
read("time_")

def brawler():
    global rare_chance
    global superrare_chance
    global epic_chance
    global mythic_chance
    global lega_chance
    global perc_levels
    
    r = randint(0, int(100/lega_chance) - 1)
    if r == 0:
        p = choice(lega_perc)
        if (p in perc[0]) == False:
            perc[0].append(p)
            print(Fore.YELLOW + brawler_str + p)
            print(Fore.WHITE, end="")
            save("perc", str(perc[0]))
            perc_levels[0][p] = 1
            powerPoints[0][p] = 1
            save("perc_levels", str(perc_levels[0]))
            save("powerPoints", str(powerPoints[0]))
            
            rare_chance /= 2
            superrare_chance /= 2
            epic_chance /= 2
            mythic_chance /= 2
            lega_chance /= 2
            
            return True
    elif randint(0, int(100/mythic_chance) - 1) == 0:
        p = choice(mythic_perc)
        if (p in perc[0]) == False:
            perc[0].append(p)
            print(Fore.RED + brawler_str + p)
            print(Fore.WHITE, end="")
            save("perc", str(perc[0]))
            perc_levels[0][p] = 1
            powerPoints[0][p] = 1
            save("perc_levels", str(perc_levels[0]))
            save("powerPoints", str(powerPoints[0]))
            
            rare_chance /= 1.5
            superrare_chance /= 1.5
            epic_chance /= 1.5
            mythic_chance /= 1.5
            lega_chance /= 1.5
            
            return True
    elif randint(0, int(100/epic_chance) - 1) == 0:
        p = choice(epic_perc)
        if (p in perc[0]) == False:
            perc[0].append(p)
            print(Fore.MAGENTA + brawler_str + p)
            print(Fore.WHITE, end="")
            save("perc", str(perc[0]))
            perc_levels[0][p] = 1
            powerPoints[0][p] = 1
            save("perc_levels", str(perc_levels[0]))
            save("powerPoints", str(powerPoints[0]))
            
            rare_chance /= 1.2
            superrare_chance /= 1.2
            epic_chance /= 1.2
            mythic_chance /= 1.2
            lega_chance /= 1.2
            
            return True
    elif randint(0, int(100/superrare_chance) - 1) == 0:
        p = choice(superrare_perc)
        if (p in perc[0]) == False:
            perc[0].append(p)
            print(Fore.CYAN + brawler_str + p)
            print(Fore.WHITE, end="")
            save("perc", str(perc[0]))
            perc_levels[0][p] = 1
            powerPoints[0][p] = 1
            save("perc_levels", str(perc_levels[0]))
            save("powerPoints", str(powerPoints[0]))
            
            rare_chance /= 1.1
            superrare_chance /= 1.1
            epic_chance /= 1.1
            mythic_chance /= 1.1
            lega_chance /= 1.1
            
            return True
    elif randint(0, int(100/rare_chance) - 1) == 0:
        p = choice(rare_perc)
        if (p in perc[0]) == False:
            perc[0].append(p)
            print(Fore.GREEN + brawler_str + p)
            print(Fore.WHITE, end="")
            save("perc", str(perc[0]))
            perc_levels[0][p] = 1
            powerPoints[0][p] = 1
            save("perc_levels", str(perc_levels[0]))
            save("powerPoints", str(powerPoints[0]))
            
            rare_chance /= 1.05
            superrare_chance /= 1.05
            epic_chance /= 1.05
            mythic_chance /= 1.05
            lega_chance /= 1.05
            
            return True
    return False
def view_perc(perc):
    print("\nBrawlers: " + str(len(perc[0])) + " / " + str(max_perc_count) + "\n")
    for el in perc[0]:
        if el in rare_perc:
            print(Fore.GREEN, end="")
        if el in superrare_perc:
            print(Fore.CYAN, end="")
        if el in epic_perc:
            print(Fore.MAGENTA, end="")
        if el in mythic_perc:
            print(Fore.RED, end="")
        if el in lega_perc:
            print(Fore.YELLOW, end="")
        print(el + " (level " + str(perc_levels[0][el]) + ")")
    print(Fore.WHITE)

def open_box(min = 5, withBrawler = True):
    global rare_chance
    global superrare_chance
    global epic_chance
    global mythic_chance
    global lega_chance
    global coins
    global powerPoints
    
    b = False
    if withBrawler == True:
        b = brawler()
    
    if b == False:
        r = randint(0, 1)
        if r == 0 or len(perc[0]) == 0:
            plus = randint(min, min*3)
            coins[0] += plus
            print("Coins: " + str(plus))
            save("coins", str(coins[0]))
        else:
            p = choice(perc[0])
            plus = randint(min - 2, (min - 2) * 2)
            powerPoints[0][p] += plus
            print("Power points (" + p + "): " + str(plus))
            save("powerPoints", str(powerPoints[0]))
        cPlus = 1.01
        if rare_chance < d_rare_chance:
            rare_chance *= cPlus
        if superrare_chance < d_superrare_chance:
            superrare_chance *= cPlus
        if epic_chance < d_epic_chance:
            epic_chance *= cPlus
        if mythic_chance < d_mythic_chance:
            mythic_chance *= cPlus
        if lega_chance < d_lega_chance:
            lega_chance *= cPlus
    if debugMode == True:
        print("Rare chance: " + str(rare_chance))

if time_[0] != -1:
    t = time() - time_[0]
    box_count[0] += int(t / 120)
    big_box_count[0] += int(t / 480)
    mega_box_count[0] += int(t / 1920)
    save("box_count", str(box_count[0]))
    save("big_box_count", str(big_box_count[0]))
    save("mega_box_count", str(mega_box_count[0]))

print("Boxes: " + str(box_count[0]))
print("Big boxes: " + str(big_box_count[0]))
print("Mega boxes: " + str(mega_box_count[0]))

while True:
    save("time_", str(time()))
    save("box_count", str(box_count[0]))
    save("big_box_count", str(big_box_count[0]))
    save("mega_box_count", str(mega_box_count[0]))
    print(">>> ", end="")
    cm = input()
    cm_ = cm.split(" ")
    if cm == "c":
        print(str(coins[0]))
    elif cm == "b":
        if box_count[0] > 0:
            box_count[0] -= 1
            open_box()
        else:
            print("No boxes!")
    elif cm == "g":
        if big_box_count[0] > 0:
            big_box_count[0] -= 1
            for x in range(0, 3):
                print("items left: " + str(3-x)+", ", end="")
                open_box(8, x > 0)
                input()
        else:
            print("No boxes!")
    elif cm == "m":
        if mega_box_count[0] > 0:
            mega_box_count[0] -= 1
            count = 5
            if randint(0, 5) == 0:
                count = 6
            if randint(0, 15) == 0:
                count = 7
            for x in range(0, count):
                print("items left: " + str(count-x)+", ", end="")
                open_box(10, x > 2)
                input()
        else:
            print("No boxes!")
    elif cm == "d":
        debugMode = True
    elif cm == "p":
        view_perc(perc)
    elif cm == "e":
        print("Type 'end' to execute")
        code = ""
        line = ""
        while True:
            line = input()
            if line == "end":
                break
            code += line
        exec(code)
    elif cm == "/":
        system("clear")
        print(startMsg)
        print("Boxes: " + str(box_count[0]))
        print("Big boxes: " + str(big_box_count[0]))
        print("Mega boxes: " + str(mega_box_count[0]))
    elif cm == "s":
        code = open('main.py', 'r').read()
        print('\n' + code)
    elif cm_[0] == "u":
        b = cm_[1]
        try:
            b += cm_[2]
        except:
            pass
        lvl = perc_levels[0][b]
        if lvl == 1:
            if coins[0] >= lvl2_coin_cost and powerPoints[0][b] >= lvl2_star_cost:
                coins[0] -= lvl2_coin_cost
                powerPoints[0][b] -= lvl2_star_cost
                perc_levels[0][b] += 1
            else:
                print("Coins or star points is not enough! Need coins: " + str(lvl2_coin_cost) + ", star points: " + str(lvl2_star_cost))
        elif lvl == 2:
            if coins[0] >= lvl3_coin_cost and powerPoints[0][b] >= lvl3_star_cost:
                coins[0] -= lvl3_coin_cost
                powerPoints[0][b] -= lvl3_star_cost
                perc_levels[0][b] += 1
            else:
                print("Coins or star points is not enough! Need coins: " + str(lvl3_coin_cost) + ", star points: " + str(lvl3_star_cost))
        elif lvl == 3:
            if coins[0] >= lvl4_coin_cost and powerPoints[0][b] >= lvl4_star_cost:
                coins[0] -= lvl4_coin_cost
                powerPoints[0][b] -= lvl4_star_cost
                perc_levels[0][b] += 1
            else:
                print("Coins or star points is not enough! Need coins: " + str(lvl4_coin_cost) + ", star points: " + str(lvl4_star_cost))
        elif lvl == 4:
            if coins[0] >= lvl5_coin_cost and powerPoints[0][b] >= lvl5_star_cost:
                coins[0] -= lvl5_coin_cost
                powerPoints[0][b] -= lvl5_star_cost
                perc_levels[0][b] += 1
            else:
                print("Coins or star points is not enough! Need coins: " + str(lvl5_coin_cost) + ", star points: " + str(lvl5_star_cost))
        elif lvl == 5:
            if coins[0] >= lvl6_coin_cost and powerPoints[0][b] >= lvl6_star_cost:
                coins[0] -= lvl6_coin_cost
                powerPoints[0][b] -= lvl6_star_cost
                perc_levels[0][b] += 1
            else:
                print("Coins or star points is not enough! Need coins: " + str(lvl6_coin_cost) + ", star points: " + str(lvl6_star_cost))
        elif lvl == 6:
            if coins[0] >= lvl7_coin_cost and powerPoints[0][b] >= lvl7_star_cost:
                coins[0] -= lvl7_coin_cost
                powerPoints[0][b] -= lvl7_star_cost
                perc_levels[0][b] += 1
            else:
                print("Coins or star points is not enough! Need coins: " + str(lvl7_coin_cost) + ", star points: " + str(lvl7_star_cost))
        elif lvl == 7:
            if coins[0] >= lvl8_coin_cost and powerPoints[0][b] >= lvl8_star_cost:
                coins[0] -= lvl8_coin_cost
                powerPoints[0][b] -= lvl8_star_cost
                perc_levels[0][b] += 1
            else:
                print("Coins or star points is not enough! Need coins: " + str(lvl8_coin_cost) + ", star points: " + str(lvl8_star_cost))
        elif lvl == 8:
            if coins[0] >= lvl9_coin_cost and powerPoints[0][b] >= lvl9_star_cost:
                coins[0] -= lvl9_coin_cost
                powerPoints[0][b] -= lvl9_star_cost
                perc_levels[0][b] += 1
            else:
                print("Coins or star points is not enough! Need coins: " + str(lvl9_coin_cost) + ", star points: " + str(lvl9_star_cost))
        else:
            print("Max level!")
        save("perc_levels", str(perc_levels[0]))
                
    else:
        print("Undefined command!")