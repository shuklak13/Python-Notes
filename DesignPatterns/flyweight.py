# http://book.pythontips.com/en/latest/__slots__magic.htmlhttp://book.pythontips.com/en/latest/__slots__magic.html
# https://stackoverflow.com/questions/472000/usage-of-slots


import sys
def attemptDynamicAssignment(s):
    """tests if a class is compatible w/ dynamic assignment"""
    print("\n"+s.__class__.__name__)
    try:
        s.attribute = 1
        s.attribute2 = 2
    except:
        print(sys.exc_info()[0])
    else:
        print("no error!")


class SlotsOnly(object):
    """ The flyweight design pattern suppresses the internal dictionary __dict__
        and instead uses a tuple, called __slots__.
        This dramatically increasing time + memory efficiency 
        by allowing Python to allocate a static amount of memory 
        during object creation."""
    __slots__ = ('attribute')   # ['attribute'] works as well
    def __init__(self):
        attribute = "hi"

# Because this is a tuple, not a dict, dynamic assignment is impossible
so = SlotsOnly()
attemptDynamicAssignment(so)    # will error b/c SlotsOnly has no attribute2


class SlotsAndDict(object):
    """ To allow dynamic assignment, add __dict__ to __slots__.
        This kills a lot of the time + memory benefits of __slots__,
            but is still faster than pure __dict__ ."""
    __slots__ = ('__dict__', 'attribute')
    def __init__(self):
        attribute = "hi"

sad = SlotsAndDict()
attemptDynamicAssignment(sad)   # will dynamically assign attribute2, no error


# Slots seem awesome! When would I not want to use them?
    # Don't use slots when you want to mess around with multiple inheritance
    # Python can't combine multiple parents w/ nonempty __slots__

# some numbers:
    # attrs  __slots__    no slots declared + __dict__
    # none       16        64 (+ 280 if __dict__ instantiated)
    # one        56        64 + 280
    # two        64        64 + 280
    # six        96        64 + 1048
    # 22        224        64 + 3352