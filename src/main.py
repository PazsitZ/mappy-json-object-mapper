from pprint import pprint

from mappy.class_mapper import ClassMapper
from mappy.dynamic_class_mapper import DynamicClassMapper
from mappy.model.foo import Foo, Bar
from mappy.model.dynamic.foo import Foo as DynFoo

DYNAMIC_MAPPER = True

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('PyCharm')

    jsonStr = """{"id":1, "name":"first Name", "bars":[ { "id": 11, "version": 1, "name": "first bar" }, { "id": 12, "version": 4, "name": "second bar" }, { "id": 15, "version": 6, "name": "another bar" } ] }"""
    if (DYNAMIC_MAPPER):
        mapper = DynamicClassMapper(DynFoo)
    else:
        mapper = ClassMapper([Foo, Bar])

    mapped: Foo = mapper.do_mapping(jsonStr)

    print("mapped:")
    pprint(mapped)
    pprint(vars(mapped))
    pprint(vars(mapped.bars[0]))
    pprint(vars(mapped.bars[1]))
    pprint(vars(mapped.bars[2]))
