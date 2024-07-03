class Action:
    def __init__(self, author: str = '11625D9061021010', target: str = '123') -> None:
        self.author: str = author
        self.target: str = target

class Sanction(Action):
    def __init__(self, author: str, target: str) -> None:
        super().__init__(author, target)