import inspect

def introspection_info(obj):
    obj_type = type(obj)
    obj_module = inspect.getmodule(obj)
    obj_attrs = []
    obj_methods = []
    for val in dir(obj):
        if callable(getattr(obj, val)):
            obj_methods.append(val)
        else:
            obj_attrs.append(val)
    return {'type': obj_type,
            'attributes': obj_attrs,
            'methods': obj_methods,
            'module': obj_module
    }


class Human:
    def __init__(self, name, age=0, is_alive=True):
        self.name = name
        self.age = age
        self.is_alive = is_alive

    def be_born(self):
        self.age = 0
        self.is_alive = True

    def grow(self):
        self.age += 1

    def die(self):
        self.is_alive = False


if __name__ == '__main__':
    number_info = introspection_info(42)
    print(number_info)
    print(introspection_info(Human))
    test_human = Human('John')
    print(introspection_info(test_human))