import random


def openHistoryData() -> str:
    """Open the text file containing the historic events and read the content

    Returns:
        str: Returns the content of the text file
    """
    file = open("events.txt", "r")
    return file.read()


def make_event_list(events: str) -> list:
    """Splits a string into a list of events on the newline character

    Args:
        events (str): String of events where every event starts on new line.

    Returns:
        list: Turns the string into a list of events.
    """
    event_list = events.split("\n")
    return event_list


def drawEvent(event_list: list) -> str:
    """If there are events in the list, draw random event from the event_list,
    remove it from the event_list, and return it as a string.
    If there are no events in the list, return "You Win".

    Returns:
        str: An event or "You Win".
    """
    if len(event_list) > 0:
        new_event_index = event_list.index(random.choice(event_list))
        new_event = event_list.pop(new_event_index)
        return new_event
    else:
        return "You Win!"


def placement() -> int:
    """Takes an integer input from the user.

    Returns:
        int: input from user
    """
    position = int(input("Enter index: "))
    return position


def checkTimeline(timeline: list, position: int) -> list:
    """_summary_

    Args:
        timeline (list): _description_
        position (int): _description_

    Returns:
        list: _description_
    """
    pass


if __name__ == "__main__":
    # List of all events possible
    list_of_events = make_event_list(openHistoryData())
    # List of drawn events
    timeline = []
    new_event = drawEvent(list_of_events)

    # Check if there are any events left in the list of events
    if "You Win" in new_event:
        print(new_event)
    else:
        timeline.append(new_event.split(" ", 1))
        print(timeline)


list = [[1700, "Joe"], [1800, "Jonas"], [1990, "Furby"]]

new_item = [1680, "Jolo"]
pos = 1


if list[pos - 1][0] in list:
    print(list[pos - 1][0])
    list.insert(pos, new_item)
else:
    print("You Lose")
# for item in list:
# print(new_item[0])
# print(list)
# print(list)
# if new_item[0] < list[pos][0]:
