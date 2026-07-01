def main():
    while(True):
        command = input("mini-shell>")

        if(command == "exit"):
            print("Existing mini-shell")
            break

        print(f"You entered: {command}")

if __name__ == "__main__":
    main()