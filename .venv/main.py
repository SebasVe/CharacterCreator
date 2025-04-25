'''Sebastian Vela & Sydney Agbakoba 4/24/2025
This program is a character creator meant to help the user make a character of their choosing'''
import bard
import warrior
import wizard
import character
import cloak
import ring
import shield
import decorator
import check_input
import random


def main():
    '''character = bard.Bard()
    character = ring.Ring(character)
    character = shield.Shield(character)
    print(character)'''

    #Variables/tuples used in the code
    trial_iterator = 0
    trials_passed = 0
    monsters = [("Spiked Dragon", 0, 6),("Orc Warlord", 1, 5), ("Shadow Knight", 2, 4),
    ("Lava Monster", 3, 3), ("Fiendish Ghoul", 4, 2),
    ("Goblin Mage", 5, 1), ("Dark Magician", 6, 0)]


    print("Character Maker!\nChoose a starting character:")
    #Getting the player class from their choice
    player_chosen_class = check_input.get_int_range("1. Bard\n2. Warrior\n3. Wizard\n> ",1,3)
    if player_chosen_class == 1:
        player_character = bard.Bard()
    elif player_chosen_class == 2:
        player_character = warrior.Warrior()
    elif player_chosen_class == 3:
        player_character = wizard.Wizard()

    #Choosing the first item
    print(player_character)
    list_items = ["Sturdy Shield", "Magic Ring", "Protective Cloak"]
    print("\nChoose 2 items:")
    item1 = check_input.get_int_range(f"1. {list_items[0]}\n2. {list_items[1]}\n3. {list_items[2]}\n> ",1,3)
    if item1 == 1:
        player_character = shield.Shield(player_character)
        list_items.remove("Sturdy Shield")
    elif item1 == 2:
        player_character = ringer.Ring(player_character)
        list_items.remove("Magic Ring")
    elif item1 == 3:
        player_character = cloak.Cloak(player_character)
        list_items.remove("Protective Cloak")

    #Choose the second item
    print(player_character)
    print("\nChoose 1 item:")
    item2 = check_input.get_int_range(f"1. {list_items[0]}\n2. {list_items[1]}\n> ",1,2)
    second_item = list_items[item2 - 1]
    if second_item == "Sturdy Shield":
        player_character = shield.Shield(player_character)
    elif second_item == "Magic Ring":
        player_character = ring.Ring(player_character)
    elif second_item == "Protective Cloak":
        player_character = cloak.Cloak(player_character)
    print(player_character)


    #3 trials
    print("\nYou must pass two of the following three trials!")
    opponent_monster = random.sample(monsters, 3)

    while trial_iterator < 3:
        print(f"\nTrial {trial_iterator+1} of 3:")
        print(f"You encounter a {opponent_monster[trial_iterator][0]}")
        print(f"MR: {opponent_monster[trial_iterator][1]}\nSTR: {opponent_monster[trial_iterator][2]}\n")

        #Fight Phase
        action_int = check_input.get_int_range("Fight:\n1. Battle\n2. Dodge\n> ", 1, 2)
        if action_int == 1:
            total_monster_strength = opponent_monster[trial_iterator][1] + opponent_monster[trial_iterator][2]
            total_player_strength = player_character.strength() + player_character.magic_resistance()
            if total_monster_strength <= total_player_strength:
                print(f"You battle with the {opponent_monster[trial_iterator][0]} and easily defeat it.")
                print("You have passed this trial.")
                trials_passed += 1
            else:
                print(f"You battle with the {opponent_monster[trial_iterator][0]} and lose pathetically.")
                print("You have failed this trial.")
        elif action_int == 2:
            dodge_factor = random.randint(0,3)
            if dodge_factor == 0:
                print(f"You successfully manage to dodge the {opponent_monster[trial_iterator][0]}, and counter.")
                print("You have passed this trial.")
                trials_passed += 1
            else:
                print(f"You attempt to dodge the {opponent_monster[trial_iterator][0]}, but it manages to hit you.")
                print("You have failed this trial.")

        trial_iterator += 1

    #Counting up all the wins and printing the last message
    if trials_passed >= 2:
        print("\nYou have passed the three trials...barely.")
    else:
        print("\nYou have failed the three trials and are now trapped forever.....")


if __name__ == '__main__':
    main()