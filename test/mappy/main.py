import sys
sys.path.append('../../src')

from pprint import pprint

#from class_mapper import ClassMapper
from model.foo import Foo, Bar
from mappy.dynamic_class_mapper import DynamicClassMapper
from mappy.model.dynamic.foo import Foo as DynFoo


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('PyCharm')

    jsonStr = """{"id":1, "name":"first Name", "bars":[ { "id": 11, "version": 1, "name": "first bar" }, { "id": 12, "version": 4, "name": "second bar" }, { "id": 15, "version": 6, "name": "another bar" } ] }"""
    #mapper = ClassMapper([Foo, Bar])

    mapper = DynamicClassMapper(DynFoo)

    mapped:Foo = mapper.do_mapping(jsonStr)

    print("mapped:")
    pprint((mapped))
    pprint(vars(mapped))
    pprint(vars(mapped.bars[0]))
    pprint(vars(mapped.bars[1]))
    pprint(vars(mapped.bars[2]))

