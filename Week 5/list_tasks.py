# A list of directions
def directions():
    steps = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return steps


print(directions())


# A list of directions and numbers
def movements():
    path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return path


# A function that uses items from a list to display a message
def run_task2():
    print("Moving...")
    direction = movements()

    for items in range(0, len(direction), 2):
        print(f"{direction[items]} for {direction[items+1]} steps")


run_task2()


# A function that displays a menu of directions
def menu():
    print("Please select a direction: ")
    path = directions()
    for items in range(0, len(path), 1):
        print(f"{items}: {path[items]}")


def run_task3():
    menu()


run_task3()
