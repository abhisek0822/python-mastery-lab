from src.commands import pwd, ls, cd, mkdir, touch, cat, clear


def main():
    while True:
        user_input = input("mini-shell> ").strip()

        if not user_input:
            continue

        parts = user_input.split()

        command = parts[0]
        argument = parts[1] if len(parts) > 1 else None

        if command == "pwd":
            print(pwd())

        elif command == "ls":
            files = ls()

            if not files:
                print("Directory is empty.")
            else:
                for file in files:
                    print(file)

        elif command == "cd":
            if argument:
                cd(argument)
            else:
                print("Usage: cd <directory>")

        elif command == "mkdir":
            if argument:
                mkdir(argument)
            else:
                print("Usage: mkdir <directory>")

        elif command == "touch":
            if argument:
                touch(argument)
            else:
                print("Usage: touch <filename>")

        elif command == "cat":
            if argument:
                print(cat(argument))
            else:
                print("Usage: cat <filename>")

        elif command == "clear":
            clear()

        elif command == "help":
            print("""
Available Commands

pwd
ls
cd <directory>
mkdir <directory>
touch <filename>
cat <filename>
clear
help
exit
""")

        elif command == "exit":
            print("Exiting mini shell...")
            break

        else:
            print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()