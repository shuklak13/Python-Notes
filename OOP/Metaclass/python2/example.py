# EXAMPLE: a metaclass that makes all attributes uppercase

# the metaclass, `upper_attr`, will be passed the same args as `type()`
def upper_attr(future_class_name, future_class_parents, future_class_attr):
    """pick up any attribute that doesn't start with '__' and uppercase it"""
    uppercase_attr = {}
    for name, val in future_class_attr.items():
        if not name.startswith('__'):
            uppercase_attr[name.upper()] = val
        else:
            uppercase_attr[name] = val
    return type(future_class_name, future_class_parents, uppercase_attr)

# all classes in this module will use the `upper_attr` metaclass
__metaclass__ = upper_attr

class Class_Example():
  bar = 'bip'

print(hasattr(Class_Example, 'bar'))    # False
print(hasattr(Class_Example, 'BAR'))    # True
c = Class_Example()
print(c.BAR)                            # 'bip'