import random

hero_hp = 50
dragon_hp = 100
hero_max_dmg = 20
dragon_max_dmg = 10

while True:
    check = int(input("How many hp does the hero have?"))
    if check == hero_hp:
        print("that's correct")
        break
    print("that's wrong")

print("Now the game beggins: \n \n The dragon with", dragon_hp, "hp attacks out hero with", hero_hp, "hp")

dragon_attack = random.randint(1, dragon_max_dmg)
print("the dragon attack has the strength of", dragon_attack)
hero_hp = int(50 - dragon_attack)
print("The dragon does", dragon_attack, "damage and the hero has", hero_hp, "hp left")

while True:
    if hero_hp <= 0:
        print("The hero lost")
        break
    print("now the hero attacks")
    print("  \n  ")
    print("Now, the hero with",hero_hp, "hp attacks the dragon with 100 hp")
    hero_attack = random.randint(1, hero_max_dmg)
    print("The hero's attack has the strenght of", hero_attack)
    dragon_hp = 100 - hero_attack
    print("The hero now does", hero_attack, "damage and the dragon has", dragon_hp, "left")
    while True:
        if dragon_hp <=0:
            print("the dragon lost")
            break
        print("now the dragon attacks")
        print(" \n ")
        print("Now, the dragon with", dragon_hp, "hp attacks the hero with", hero_hp)
        dragon_attack = random.randint(1, dragon_max_dmg)
        print("The dragon's attack has the strenght of", dragon_attack)
        hero_hp = hero_hp - dragon_attack
        print("The dragon now does", dragon_attack, "damage and the hero has", hero_hp, "left")
        break
