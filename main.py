from colorama import Fore, Back, Style
import base64


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


def convertToBase64():
    with open('token.txt') as f:
        token = f.readlines()
        f.close()

    token = token[0].strip()
    token_bytes = token.encode('ascii')

    base64_token = base64.b64encode(token_bytes).decode('utf-8')

    f = open("encodeTokenToBase64.txt", "a")
    f.write(base64_token)
    f.close()

    return base64_token


while True:
    wish = int(input(
        "Hello, what would you like to do?\n" + "1. Format a curl command to a single line\n" + "2. Encode API Token to Base64\n" + Fore.RED + "3. Exit\n" + Fore.RESET))

    if wish == 1:
        formatToSingleLine()
        print(Fore.GREEN + "Done!\n" + Fore.RESET)
    elif wish == 2:
        convertToBase64()
        print(Fore.GREEN + "Encoded!\n" + Fore.RESET)
    elif wish == 3:
        break
