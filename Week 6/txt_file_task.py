import os


# This function prints the current working directory
def cwd():
    path = os.getcwd()
    print(f"The current working directory is {path}")
    print(f"The directory contains the following: ")
    for file in os.listdir(path):
        print(file)


def run():
    print("Processing...")
    cwd()


if __name__ == "__main__":
    run()

print()


# This function prints the first numbers of characters specified in the parameters
def display_chars(file_path, numb_chars):
    print(f"The first {numb_chars} characters are: ")
    with open(file_path) as file:
        data = file.read(numb_chars)
        print(data)


# This function displays the first line of the file
def display_line(file_path):
    print("The first line is: ")
    with open(file_path) as file:
        data = file.readline().strip()
        print(data)


# This function displays the whole file
def display_text(file_path):
    print(f"The full text is: ")
    with open(file_path) as file:
        data = file.read()
        print(data)


def run_task2():
    display_chars("library.txt", 10)
    print()
    display_line("library.txt")
    print()
    display_text("library.txt")


if __name__ == "__main__":
    run_task2()

print()


# This function reads the file line by line and displays the message "Looked in..." before each line
def search(file_path):
    print("Searching...")
    with open(file_path) as file:
        for location in file:
            print(f"Looked in {location.strip()}")
    print("...Done!")


def run_task3():
    search("library.txt")


if __name__ == "__main__":
    run_task3()

print()


# This function will organise text and return it as a variable
def search_books(file_path):
    print("Searching...")

    sections = ""
    books = "Books:\n"

    with open(file_path) as file:
        for line in file:
            if line.startswith("Section"):
                sections = sections + line
            else:
                books = books + line

    print("Done!")

    return f"{sections}\n\n{books}"


# This function will save the variable of the previous function in a new file
def save(file_path, data):
    print("Saving...")
    with open(file_path, "w") as file:
        file.write(data)
    print("Done!")


def run_task4():
    data = search_books("books.txt")
    print()
    save("exported_books.txt", data)


if __name__ == "__main__":
    run_task4()
