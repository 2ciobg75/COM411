# This function creates a set of values
def observed():
    observations = {"Car", "Sky Scraper", "Sky Scraper", "Bike", "House", "House"}
    return observations


def run_task1():
    print(observed())


if __name__ == "__main__":
    run_task1()


# This function will store 7 values from the user in a list
def observed_items():
    observations = []

    for count in range(7):
        print("Please enter an observation: ")
        observations.append(input())

    return observations


def run_task2():
    print("Counting observations...")
    observations = observed_items()

    observations_set = set()
    for observation in observations:
        data = (observation, observations.count(observation))
        observations_set.add(data)

    for data in observations_set:
        print(f"{data[0]} observed {data[1]} times.")


if __name__ == "__main__":
    run_task2()
