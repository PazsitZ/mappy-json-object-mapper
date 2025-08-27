import json
import logging
from types import SimpleNamespace

from mappy.mapping_tools import is_primitive
from mappy.model.trait_key_matching import matchingKeys

logger = logging.getLogger(__name__)

class DynamicClassMapper:
    def __init__(self, baseClass):
        self.baseClass = baseClass
        pass

    def do_mapping (self, jsonStr):
        dict = json.loads(jsonStr)
        return self.__map(dict)

    def __map(self, data, classNotation = None):
        if (classNotation == None and matchingKeys(data.keys(), self.baseClass)):
            baseClassInstance = self.baseClass()
            return self.__map(data, self.baseClass)
        elif type(data) == type(list()):
            dataList = []
            for obj in data:
                dataList.append(self.__map(obj, classNotation))
            return dataList
        else:
            obj = data
            clazzInstance = classNotation()
            if (matchingKeys(obj.keys(), classNotation)):
                for k in obj.keys():
                    if type(obj[k]) == type(dict()) or type (obj[k]) == type(list()):
                        if (hasattr(classNotation.__annotations__[k], "__args__")):
                            typeNot = classNotation.__annotations__[k].__args__[0]
                        elif (type(classNotation.__annotations__[k]) == type(list())):
                            typeNot = classNotation.__annotations__[k][0]
                        else:
                            typeNot = None

                        setattr(clazzInstance, k, self.__map(obj [k], typeNot))
                    else:
                        try:
                            setattr(clazzInstance, k, type(obj[k])(obj[k]))
                        except Exception:
                            logger.debug(f"error occured while type transformation from {type(obj[k])} to {type(k)} on value: {obj[k]}")
                            setattr(clazzInstance, k, obj[k])

                return clazzInstance

            logger.debug("No class match: " + str(obj.keys()) + "; typeNotation: ["+ str(classNotation) + "];")
            if (is_primitive(classNotation)):
                return str(data)
            else:
                return SimpleNamespace (**obj)
