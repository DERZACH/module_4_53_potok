import os


current_path = os.path.abspath(__file__)

parent_path = os.path.join(current_path, '..', '..')
# print(parent_path)


def recursion(count):
    print(count)
    if count == 5:
        return
    recursion(count + 1)
    print(count)


recursion(0)