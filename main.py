import random
import os


def check_timeline(timeline: list, new_event: list, pos: int) -> None:
    """A function that checks a timeline and adds a new event at given position

    Args:
        timeline (list): A List of events that itself
        contains a list of two items, a year and a name.

        new_event (list): A list containing a year and a name,
        that should be added to the timeline.

        position (int): An integer representing the
        index where in the timeline the new event should be added.


    Returns:
        None: The function only modifies the timeline
    """

    event_year = int(new_event[0])
    last_timeline_year = int(timeline[-1][0])
    first_timeline_year = int(timeline[0][0])

    # If the inputted position is less than the length of the timeline
    if pos <= len(timeline) - 1:
        if pos == -1:
            if event_year > int(timeline[-1][0]):
                timeline.append(new_event)
            else:
                timeline.clear()
        # The inputted position is the first in the list
        if pos == 0:
            if event_year < 0 and first_timeline_year < 0:
                if event_year < first_timeline_year:
                    timeline.insert(0, new_event)
                else:
                    timeline.clear()
            elif event_year < first_timeline_year:
                timeline.insert(0, new_event)
            else:
                timeline.clear()
        # The position is between 1 and last index of the list
        elif (pos > 0) and (pos < len(timeline) - 1):
            timeline_left = int(timeline[pos - 1][0])
            if event_year in range(timeline_left + 1, int(timeline[pos][0])):
                timeline.insert(pos, new_event)
            else:
                timeline.clear()
        # The position is at the last index of the list
        elif pos == len(timeline) - 1:
            if pos == -1 and event_year < last_timeline_year:
                timeline.clear()
            elif event_year <= last_timeline_year and event_year >= int(
                timeline[pos - 1][0]
            ):
                timeline.insert(pos, new_event)
            else:
                timeline.clear()
    # The position is after the last index
    elif pos == len(timeline):
        if event_year < 0 and last_timeline_year < 0:
            if event_year > last_timeline_year:
                timeline.append(new_event)
            else:
                timeline.clear()
        elif event_year >= last_timeline_year:
            timeline.append(new_event)
        else:
            timeline.clear()
    # The index is out of range
    else:
        print(f"Error! The maximum index of the list is {len(timeline)-1}")
        timeline.clear()


def drawEvent(event_list: list) -> list:
    """Draw random event from the event_list,
    remove it from the event_list, and return it
    as a list of two items (year, name).

    Returns:
        list: A list containing a historic event
    """
    new_event = random.choice(event_list)
    event_list.remove(new_event)
    return new_event.split(" ", 1)


def make_event_list(events: str) -> list:
    """Splits a string into a list of events on the newline character

    Args:
        events (str): String of events where every event starts on new line.

    Returns:
        list: Turns the string into a list of events.
    """
    event_list = events.split("\n")
    return event_list


def openHistoryData() -> str:
    """Open the text file containing the historic events and read the content

    Returns:
        str: Returns the content of the text file
    """
    with open("events.txt", "r") as f:
        file_content = f.read()
    return file_content


def play_game() -> None:
    """A function that starts a new game of Timeline!"""
    # Clears the console
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")
    # List of all events possible
    list_of_events = make_event_list(openHistoryData())
    # # Container for list of drawn events
    timeline = []
    while len(list_of_events) > 0:
        new_event = drawEvent(list_of_events)
        # Check if this is the first event in the list
        if len(timeline) < 1:
            timeline.append(new_event)
            print(f"{timeline.index(new_event)} {new_event[1]}")
            print("▹▹▹▹▹▹▹▹▹▹▹▹▹▹▹▹▹▹▹▹▹▹▹▹▹▹▹▹▹▹▹▹▹▹▹▹")
        else:
            print(new_event[1])
            check_timeline(timeline, new_event, user_placement())
            print_timeline(timeline)
            print("▹▹▹▹▹▹▹▹▹▹▹▹▹▹▹▹▹▹▹▹▹▹▹▹▹▹▹▹▹▹▹▹▹▹▹▹")
        if len(timeline) < 1:
            break
    if len(list_of_events) == 0 and len(timeline) != 0:
        print("You Win!!")
    else:
        print("You Lose!")


def print_timeline(timeline: list) -> None:
    """A function that loops over the index, year, and name of an event.
    Then it prints the index and the event

    Args:
        timeline (list): A timeline of events containing a year and a name
    """
    for index, [time, event] in enumerate(timeline, start=0):
        print(index, event)


def user_placement() -> int:
    """Takes an integer input from the user.

    Returns:
        int: input from user
    """
    position = int(input("Enter index: "))
    return position


if __name__ == "__main__":
    play_game()
