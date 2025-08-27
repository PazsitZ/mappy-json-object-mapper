
def matchingKeys(list:list, clazz):
    if len(list) != len(clazz.__annotations__.keys()):
        return False

    for attr in clazz.__annotations__.keys():
        if (attr not in list):
            return False

    return True