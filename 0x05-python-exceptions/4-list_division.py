#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """Divides two lists element by element.

    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The number of elements to divide.

    Returns:
        A new list of length list_length containing all the divisions.
    """
    new_list = []
    for number in range(0, list_length):
        try:
            output = my_list_1[number] / my_list_2[number]
        except TypeError:
            print("wrong type")
            output = 0
        except ZeroDivisionError:
            print("division by 0")
            output = 0
        except IndexError:
            print("out of range")
            output = 0
        finally:
            new_list.append(output)
    return (new_list)
