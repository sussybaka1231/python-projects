from colorama import Fore
from keyboard import *
from os import *
import getpass
import sys
import shutil

chdir("/")

print(f"""{Fore.GREEN}Welcome to LightOS, {getpass.getuser()}!
------------------------------
| Press Ctrl+Enter to login! |
| Press Ctrl+S to exit!      |
------------------------------""")
while True:
    if is_pressed("ctrl+enter"):
        user_command = input(f"Enter \"help\" to view all commands!\n{getcwd()}@{getpass.getuser()}> ")
        break
    elif is_pressed("ctrl+s"):
        print(f"{Fore.LIGHTRED_EX}Exiting.")
        exit(0)

while True:
    if user_command.lower() == "help":
        print("""List of commands:
<<<<<--------------------------------------------
    help - display this message

    nf - make a new file

    rmf - remove a file

    mkdir - make a new directory

    rmdir - remove a directory

    cd - change directory

    cwd - get current working directory

    exec - execute a command in your local shell

    ls - list files and directories

    exit - exit
<<<<<-------------------------------------------""")
    elif user_command.lower().startswith("nf"):
        if sys.platform.startswith('win'):
            system(f"echo >> \"{user_command[3:]}\"")
        else:
            system(f"touch \"{user_command[3:]}\"")
        print("Success!")
    elif user_command.lower().startswith("rmf"):
        try:
            remove(user_command[4:])
            print("Success!")
        except Exception as e:
            print(f"Error {e}")
    elif user_command.lower().startswith("mkdir"):
        try:
            mkdir(user_command[6:])
            print("Success!")
        except Exception as e:
            print(f"Error {e}")
    elif user_command.lower().startswith("rmdir"):
        try:
            if len(listdir(user_command[5:])) > 0:
                shutil.rmtree(user_command[5:])
            else:
                rmdir(user_command[5:])
            print("Success!")
        except Exception as e:
            print(f"Error {e}")
    elif user_command.lower().startswith("cd"):
        try:
            chdir(user_command[3:])
        except Exception as e:
            print(f"Error {e}")
    elif user_command.lower() == "cwd":
        print(f"Current working directory: {getcwd()}")
    elif user_command.lower().startswith("exec"):
        try:
            system(user_command[5:])
        except Exception as e:
            print(f"Error {e}")
    elif user_command.lower().startswith("ls"):
        try:
            if user_command[2:].strip() == "":
                result = ', \n'.join(listdir("."))
                print(result)
            else:
                result = ', \n'.join(listdir(user_command[3:]))
                print(result)
        except Exception as e:
            print(f"Error {e}")
    elif user_command.lower() == "exit":
        print(f"{Fore.LIGHTRED_EX}Exiting.")
        exit(0)
    else:
        list_of_user_command = user_command.split(" ")
        string_form_of_list_of_user_command = ''.join(list_of_user_command[0])
        run_in_shell = input(f'"{string_form_of_list_of_user_command}" is not recognized as a command, run in local shell? (y/n): ')
        if run_in_shell.lower() == "y":
            system(user_command)
        elif run_in_shell.lower() == "n":
            print("Not running in shell...")
        else:
            print("Invalid option.")
    user_command = input(f"{getcwd()}@{getpass.getuser()}> ")
