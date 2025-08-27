import unittest
from pprint import pprint

from mappy.dynamic_class_mapper import DynamicClassMapper
from mappy.model.dynamic.foo import Foo as DynFoo


class TestDynamicMapper(unittest.TestCase):
    def testMapper(self):
        jsonStr = """{"id":1, "name":"first Name", "bars":[ { "id": 11, "version": 1, "name": "first bar" }, { "id": 12, "version": 4, "name": "second bar" }, { "id": 15, "version": 6, "name": "another bar" } ] }"""

        mapper = DynamicClassMapper(DynFoo)
        result = mapper.do_mapping(jsonStr)

        print("mapped:")
        pprint(result)
        pprint(vars(result))
        pprint(vars(result.bars[0]))
        pprint(vars(result.bars[1]))
        pprint(vars(result.bars[2]))
