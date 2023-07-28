from colorama import Fore, Back, Style


def formatToSingleLine():
    with open('command.txt') as f:
        lines = f.readlines()
        f.close()

    command = ''
    for line in lines:
        command += line.strip() + ' '

    f = open("formattedToSingleLine.txt", "a")
    f.write(command)
    f.close()

    return command


while True:
    wish = int(input(
        "Hello, what would you like to do?\n" + "1. Format a curl command to a single line\n" + Fore.RED + "2. Exit\n" + Fore.RESET))

    if wish == 1:
        formatToSingleLine()
        print(Fore.GREEN + "Done!\n" + Fore.RESET)

    if wish == 2:
        break
