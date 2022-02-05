import random


def GetRndElement(in_list):
    if len(in_list):
        return random.choice(in_list)

    return None


Some_list = [1, 2, 3, 4, 6, 7, 3, 4, 6, 99]
EmptyList = []
print(GetRndElement(EmptyList))
