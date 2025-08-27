from typing import List

from mappy.model.dynamic.bar import Bar


class Foo:
    def __init__(self):
        pass

    id: int
    name: str
    bars: [Bar]

    def __hash__(self):
        return id