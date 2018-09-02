# https://docs.python.org/2/tutorial/classes.html#tut-private

# Normally, MappingSubclass.update() would overwrite Mapping.update()
    # This is desired behavior, because we want each subclass the flexibility to implement its functions as it wants
# HOWEVER, we also may want to use Mapping.update() elsewhere in our code
    # when MappingSubclass is initialized, it will used MappingSubclass.update()
    # In this circumstance, however, we want to use Mapping.update()
# We can fix this by assigning a private copy of Mapping.update(), Mapping.__update()
    # Mapping.__update() is internally referred as Mapping.__Mapping__update()
    # So, even if MappingSubclass creates its own __update(), there will be no name conflict between __Mapping__update() and __MappingSubclass_update()


class Mapping:
    def __init__(self, iterable):
        self.item_list = []
        # self.update(iterable) #bad!
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.item_list.append(item)

    __update = update   # private copy of update()


class MappingSubclass(Mapping):
    # provides new signature for update()
    # but does not break __init__()
    def update(self, keys, values):
        for item in zip(keys, values):
            self.item_list.append(item)


ms = MappingSubclass([1, 2, 3])
print(ms.item_list)