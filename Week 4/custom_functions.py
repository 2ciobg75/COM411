# Function that listens
def listen():
    print("What sound did you hear?")
    sound = input()
    print(f"That was a loud {sound}!")


# Calling the function "listen"
listen()


# Function that ask the user what is in front of us
def identify():
    print("What lies before us?")
    word = input()
    if word == "a large boulder":
        print("It's time to run!")
    else:
        print("We will be fine.")


# Calling the function "identify"
identify()
