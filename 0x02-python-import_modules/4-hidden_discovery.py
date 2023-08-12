#!/usr/bin/python3

if __name__ == "__main__":
    """This prints all the names imported from hidden_4 """
    import hidden_4

    namz = dir(hidden_4)
    for nam in namz:
        if nam[:2] != "__":
            print(nam)
