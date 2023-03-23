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
        playing_game = False
        print("You Win!")
        return playing_game


def user_placement() -> int:
    """Takes an integer input from the user.

    Returns:
        int: input from user
    """
    position = int(input("Enter index: "))
    return position


def check_timeline(timeline: list, position: int) -> list:
    """_summary_

    Args:
        timeline (list): _description_
        position (int): _description_

    Returns:
        list: _description_
    """
    if position <= len(timeline) - 1:
        if pos == 0:
            if new_item[0] < timeline[0][0]:
                print(new_item[0])
                print(timeline[0][0])
                timeline.insert(0, new_item)
                print(timeline)
            else:
                print("You lose")
                playing_game = False
        elif (pos > 0) and (pos < len(timeline) - 1):
            print("Position is not the first in the list, and not the last")
        elif pos == len(timeline) - 1:
            if new_item[0] <= timeline[-1][0]:
                timeline.append(new_item)
                print(timeline)
            else:
                print("You lose")
                playing_game = False
    elif pos == len(timeline):
        if new_item[0] >= timeline[-1][0]:
            timeline.append(new_item)
            print(timeline)
        else:
            print("You lose")
            playing_game = False
    else:
        print(f"Error! The maximum index of the list is {len(list)-1}")
    return 

if __name__ == "__main__":
    # List of all events possible
    list_of_events = make_event_list(openHistoryData())
    # List of drawn events
    timeline = []
    playing_game = True
    while playing_game:
        
    # while playing_game:
    #     new_event = drawEvent(list_of_events)
    #     # Check if this is the first event in the list
    #     if len(timeline) < 1:
    #         timeline.append(new_event.split(" ", 1))
    #     user_placement = user_placement()
    #     check_timeline(timeline, user_placement)

    # Check if there are any events left in the list of events
    # else:
    #     timeline.append(new_event.split(" ", 1))
    #     print(timeline)

# Cover index 0 med minst en ting til i lista //
# Cover index over 0 og mindre enn siste index
# Cover index siste spot i lista (-1 OR list.length -1)
# for event in 
list = [[1700, "Joe"], [1800, "Stein"]]

new_item = [1700, "Jolo"]
pos = 3





# if 0 == 0:
#     print(len(list) - 1)
#     print(list[0])
# if list[pos - 1][0] in list:
#     print(list[pos - 1][0])
#     list.insert(pos, new_item)
# else:
#     print("You Lose")


# for item in list:
# print(new_item[0])
# print(list)
# print(list)
# if new_item[0] < list[pos][0]:
