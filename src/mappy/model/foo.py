from dataclasses import dataclass
from typing import List

#@dataclass
class Bar:
    def __init__(self):
        pass

    id: int
    version: int
    name: str

    def __hash__(self):
        return id


#@dataclass
class Foo:
    def __init__(self):
        pass

    id: int
    name: str
    bars: List[Bar]

    def __hash__(self):
        return id