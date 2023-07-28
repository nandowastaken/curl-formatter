from colorama import Fore, Back, Style


def formatToSingleLine():
    with open('command.txt') as f:
        lines = f.readlines()

    command = ''
    for line in lines:
        command += line.strip() + ' '

    return command


while True:
    wish = int(input(
        "Hello, what would you like to do?\n" + "1. Format a curl command to a single line\n" + Fore.RED + "2. Exit\n" + Fore.RESET))

    if wish == 1:
        print(Fore.YELLOW + formatToSingleLine() + Fore.RESET)

    if wish == 2:
        break
