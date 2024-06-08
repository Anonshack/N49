from colorama import Fore


# mevalar = ["apple", "apricot", "banana"]
#
# raqam = input("Enter the fruit's index number: ")
#
# try:
#     raqam = int(raqam)
#
#     if 0 <= raqam < len(mevalar):
#         print(Fore.LIGHTRED_EX + mevalar[raqam])
#     else:
#         print(Fore.RED + "Error! No such number exists.")
# except ValueError:
#     print(Fore.RED + "Error! You must enter a number.")
while 1:
    manu1 = input("""
        1) Small game, first latter
        2) Quite !
    >>>> """)
    if manu1 == '1':
        text = input(Fore.BLUE + "enter words: ")
        x = text[0]
        wanna = input(Fore.BLUE + f"[{x}] you have to enter a word to this latter: ")
        if wanna[0] == x:
            print(Fore.GREEN + 'yes it\'s correct')
        else:
            print(Fore.LIGHTRED_EX + 'no it\'s incorrect')
        manu2 = input("""Do you wanna play again?
            1) Yes
            2) No
        >>>> """)
        if manu2 != "Yes":
            print(True)
        elif manu2 != "No":
            print(Fore.LIGHTRED_EX + "You don't wanna play this why the light of before you said about that !!!\a")
            break

    elif manu1 == '2':
        print(Fore.GREEN + 'you are logout successfully')
        break

    else:
        print(Fore.LIGHTRED_EX + "Pls choice correct number in a manu !!!\a")
