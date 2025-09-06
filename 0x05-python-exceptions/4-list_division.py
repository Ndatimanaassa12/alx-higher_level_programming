#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:
            # Try to get elements at index i
            num = my_list_1[i]
            den = my_list_2[i]

            # Check type of elements
            if not (isinstance(num, (int, float)) and isinstance(den, (int, float))):
                print("wrong type")
                result.append(0)
                continue

            # Try division
            div = num / den

        except ZeroDivisionError:
            print("division by 0")
            result.append(0)

        except IndexError:
            print("out of range")
            result.append(0)

        except Exception:
            # Catch any other unexpected exceptions, also append 0
            result.append(0)

        else:
            # Division successful
            result.append(div)

    return result

