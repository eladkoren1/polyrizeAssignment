from dataclasses import dataclass

class MagicList(list):

    def __init__(self, cls_type=object):
        self.append(cls_type)


@dataclass()
class Person:
    age: int = 0

    def __init__(self):
        self.age: int = 0

        pass