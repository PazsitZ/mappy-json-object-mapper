import json
import logging
from types import SimpleNamespace

from mappy.mapping_tools import is_primitive
from mappy.model.trait_key_matching import matchingKeys

logger = logging.getLogger(__name__)

class ClassMapper:
    def __init__(self, supported_classes_for_mapping):
        self.supported_classes_for_mapping = supported_classes_for_mapping
        pass

    def do_mapping (self, jsonStr):
        dict = json.loads(jsonStr)
        return self.map(dict)

    def map(self, data, typeNotation = None):
        if type(data) == type(list()):
            dataList = []
            for obj in data:
                dataList.append(self.map(obj, typeNotation))
            return dataList
        else:
            obj = data
            for clazz in self.supported_classes_for_mapping:
                if (matchingKeys(obj.keys(), clazz)):
                    clazzInstance = clazz()
                    for k in obj.keys():
                        if type(obj[k]) == type(dict()) or type (obj[k]) == type(list()):
                            if (hasattr(clazz.__annotations__[k], "__args__")):
                                typeNot = clazz.__annotations__[k].__args__[0]
                            elif (type(clazz.__annotations__[k]) == type(list())):
                                typeNot = clazz.__annotations__[k][0]
                            else:
                                typeNot = None
                            #classNotation.__annotations__[k][0]
                            setattr(clazzInstance, k, self.map(obj [k], typeNot))
                        else:
                            try:
                                setattr(clazzInstance, k, type(k)(obj[k]))
                            except Exception:
                                logger.debug(f"error occured while type transformation from {type(obj[k])} to {type(k)} on value: {obj[k]}")
                                setattr(clazzInstance, k, obj[k])

                    return clazzInstance

            logger.debug("No class match: " + str(obj.keys()) + "; typeNotation: ["+ str(typeNotation) + "];")
            if (is_primitive(typeNotation)):
                return str(data)
            else:
                return SimpleNamespace (**obj)
