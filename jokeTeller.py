# Disclamer: All code is my own, except for the joke file, which was found online (Because I'm not funny).
# Note: All code is overcommented, as I'm unsure how advanced the reader is and I want them to understand what is happening (I'm not a fan of overcommenting, but I'm trying to be helpful).
# Note: Some of this code uses new Python features, If any errors occur, please check that you have Python 3.11 or higher installed.
# Note: An uncommented version of this code can be found attached.

# Modules are imported at the top of the file, so that they are available to the entire program.
# Import only the required methods from the modules, saves time and memory by not importing the entire module.
from random import choice
from os import system, name

# Constants are declared at the top of the file, and are in all caps for easier readability.
JOKE_FILE = "jokes.txt"  # Name of the file containing the "jokes".
QUIT_KEY = "Q"  # The key which will be used to quit the program.

def main(): # The main function is the entry point of the program.
    system(("cls" if name == "nt" else "clear"))  # Clear the console.

    jokes = [] # Create an empty list to store the jokes in.

    try: # Try to open the joke file.
        with open(JOKE_FILE, mode="r", encoding="utf8") as jokeFile: # Open the joke file in read mode, and set the encoding to utf8.
            for line in jokeFile: # Loop through each line in the file.
                if line.startswith("#") or line.isspace(): # If the line starts with a "#", then it is a comment, so skip it. If the line is empty, then skip it.
                    continue # Skip to the next line.

                try: # Try to split the line into a joke and an answer.
                    joke, answer = line.split("|") # Split the line into a joke and an answer, using the "|" character as a separator.
                    jokes.append( {"joke": joke.strip(), "answer": answer.strip()} ) # Add the joke and answer to the jokes list, as a dictionary.
                except Exception as error: # If an error occurs, then the line is not formatted correctly.
                    print(f"An error has occured while parsing the joke file, with reason: {error}.")
                    continue # Skip to the next line.

    except Exception as error: # If an error occurs, then the joke file could not be opened.
        print(f"An error has occurred trying to open {JOKE_FILE}, with reason: {error}.")
        exit(1) # Exit the program with error code 1.

    while True: # Loop forever or until the user quits using the quit key.
        userInput = input(f"Press enter to hear a joke, or \"{QUIT_KEY}\" to quit: ")

        if userInput.upper() == QUIT_KEY: # If the user input is equal to the quit key, then quit.
            print("Goodbye!") # Print a goodbye message.
            system(("cls" if name == "nt" else "clear")) # Again, lazy way of clearing the console.
            exit(0) # Exit the program with success code 0.
        else:
            currentJoke = choice(jokes) # Choose a random joke from the jokes list.
            print(currentJoke["joke"]) # Print the joke.

            userInput = input(f"Press enter to see the answer, or \"{QUIT_KEY}\" to quit: ")

            if userInput.upper() == QUIT_KEY: # If the user input is equal to the quit key, then quit.
                print("Goodbye!")
                system(("cls" if name == "nt" else "clear")) # Again, lazy way of clearing the console.
                exit(0) # Exit the program with success code 0.
            else: 
                print(currentJoke["answer"]) # Print the answer.
                input("Press enter to continue...") # Wait for the user to press enter before continuing.
                system(("cls" if name == "nt" else "clear")) # Again, lazy way of clearing the console.


if __name__ == "__main__": # If the file is being run directly, then run the main function.
    main() 
