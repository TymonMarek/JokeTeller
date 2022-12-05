from random import choice
from os import system, name

JOKE_FILE = "jokes.txt"
QUIT_KEY = "Q"

def main():
    try:
        system(("cls" if name == "nt" else "clear"))
    except Exception as error:
        CLEAR_COMMAND = ""
        print(f"The clear command \"{CLEAR_COMMAND}\" is not supported on this system, with reason: {error}. Execution will continue, but the console may not be cleared.")

    jokes = []

    try:
        with open(JOKE_FILE, "r", encoding="utf8") as jokeFile:
            for line in jokeFile:
                if line.startswith("#"):
                    continue

                try:
                    joke, answer = line.split("|")
                    jokes.append({"joke": joke.strip(), "answer": answer.strip()})
                except Exception as error:
                    print(f"An error has occured while parsing the joke file, with reason: {error}.")
                    continue

    except Exception as error:
        print(f"An error has occurred trying to open {JOKE_FILE}, with reason: {error}.")
        exit(1)

    while True:
        userInput = input(f"Press enter to hear a joke, or \"{QUIT_KEY}\" to quit: ")

        if userInput.upper() == QUIT_KEY:
            print("Goodbye!")
            system(("cls" if name == "nt" else "clear"))
            exit(0)
        else:
            currentJoke = choice(jokes)
            print(currentJoke["joke"])

            userInput = input(f"Press enter to see the answer, or \"{QUIT_KEY}\" to quit: ")

            if userInput.upper() == QUIT_KEY:
                print("Goodbye!")
                system(("cls" if name == "nt" else "clear"))
                exit(0)
            else:
                print(currentJoke["answer"])
                input("Press enter to continue...")
                system(("cls" if name == "nt" else "clear"))

if __name__ == "__main__":
    main()