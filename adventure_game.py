import time
import random


def print_pause(msg_print):
    print(msg_print)
    time.sleep(2)


def intro():
    print_pause("Hi I Mosab, welcom to challenging game.")
    print_pause("We have two challenges, we will test information with one "
                "of them and the other in which we will test your strength.")
    print_pause("To win the game you must win both challenges.")
    print_pause("Are youy ready !")


def choose_gate(items):
    print_pause("\nFrom which gate do you want to start?")
    chos = input("Select number, 1-information gate    2-strength gate.\n")
    if chos == '1':
        print_pause("\nYou will test your knowledge..")
        infor_gate(items)
    elif chos == '2':
        strength_gate(items)
    else:
        choose_gate(items)


def infor_gate(items):
    a = "Who is a Python programming language creator?"
    b = "In what language did this game wrote?"
    qus = random.choice([a, b])
    if 'done2' in items:
        print_pause("\nAnswer the question to win the game...!")
        print_pause("Whatch out!")
        print_pause("(Selecting an invalid value will bring you back "
                    "to selecting gates.)")
        if qus == a:
            answer = input(qus + "\nenter number, 1.Guido van Rossum. "
                           "2.Brendan Eich:\n")
            if answer == '1':
                print_pause("\nYou are strong and smart, you win ..")
                play_again()
            elif answer == '2':
                print_pause("\nUnfortunate, you were close to winning, "
                            "don't be sad.")
                play_again()
            else:
                print_pause("please enter a valid option!")
                choose_gate(items)
        elif qus == b:
            answer = input(qus + "\nchoose number, 1.'Js'   2.'Python':\n")
            if answer == '1':
                print_pause("\nUnfortunate, you were close to winning, "
                            "don't be sad.")
                play_again()
            elif answer == '2':
                print_pause("\nYou are strong and smart, you win .. ")
                play_again()
            else:
                print_pause("please enter a valid option!")
                choose_gate(items)
    if 'done2' not in items:
        print_pause("\nAnswer the question !")
        print_pause("Whatch out!")
        print_pause("Selecting an invalid value will bring you back "
                    "to selecting gates.")
        if qus == a:
            answer = input(qus + "\nenter number, 1.Guido van Rossum. "
                           "2.Brendan Eich:\n")
            if answer == '1':
                print_pause("\nyou are amazing, "
                            "go to the other challenge to win ..")
                items.append("done1")
                strength_gate(items)
            elif answer == '2':
                print_pause("\nUnfortunate, you lost...")
                play_again()
            else:
                print_pause("please enter a valid option!")
                choose_gate(items)
        elif qus == b:
            answer = input(qus + "\nchoose number, 1.'Js'   2.'Python':\n")
            if answer == '1':
                print_pause("\nUnfortunate, you lost...")
                play_again()
            elif answer == '2':
                print_pause("\nYou are amazing smart, "
                            "go to the other challenge to win ..")
                items.append("done1")
                strength_gate(items)
            else:
                print_pause("please enter a valid option!")
                choose_gate(items)


def strength_gate(items):
    if 'done2' in items:
        print_pause("You won this challenge, will go to the other gate "
                    "to complete the game.")
        infor_gate(items)
    hit = str(random.randint(1, 2))
    print_pause("\nYou will face one of the best professional wrestlers.!")
    print_pause("The Rock, that to win it must hit him by two hits.")
    print_pause("The number of hits will be randomly selected for you.")
    if 'done1' in items:
        print_pause("\nLet's see your luck how many hit gave you:  \n" + hit)
        if hit == '2':
            print_pause("\nYou are strong and smart, you win .. ")
            play_again()
        else:
            print_pause("\nUnfortunate, you were close to winning, "
                        "don't be sad.")
            play_again()
    elif 'done1' not in items:
        print_pause("\nLuck never comes to cowards.")
        print_pause("Let's see your luck how many hit gave you:  \n" + hit)
        if hit == '2':
            print_pause("You are strong, "
                        "go to the other challenge to win ..")
            items.append("done2")
            infor_gate(items)
        else:
            print_pause("\nUnfortunate, you lost...")
            play_again()


def play_again():
    again = input("\n DO you want play again? enter 'y' or 'n':\n").lower()
    if again == 'n':
        exit(print_pause("\nOK, see you soon..!"))
    elif again == 'y':
        print_pause("\nThis is a great.. Let's go!\n")
        play_game()
    else:
        print_pause("Please enter 'y' or 'n' !!")
        play_again()


def play_game():
    items = []
    intro()
    choose_gate(items)


play_game()
