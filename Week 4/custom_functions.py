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


# Function that helps the user escape the boulder
def escape_by(plan):
    if plan == "jumping over":
        print("We cannot escape that way! The boulder is too big!")
    elif plan == "running around":
        print("We cannot escape that way! The boulder is moving too fast!")
    elif plan == "cross bridge ahead":
        print("That might just work! Let's go!")
    else:
        print("Not sure what the plan is.")


escape_by("jumping over")
escape_by("running around")
escape_by("cross the bridge ahead")
