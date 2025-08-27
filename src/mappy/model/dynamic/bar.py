
class Bar:
    def __init__(self):
        pass

    id: int
    version: int
    name: str

    def __hash__(self):
        return id