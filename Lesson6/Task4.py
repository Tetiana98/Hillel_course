# Task4
def change_list(abc):
    if len(abc) < 2:
        return abc
    abc[0], abc[-1] = abc[-1], abc[0]
    return abc
