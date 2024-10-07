def introspection_info(obj):

    obj_type = type(obj).__name__

    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith('__')]

    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith('__')]

    if hasattr(obj, '__module__'):
        module = obj.__module__
    else:
        module = '__main__'

    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': module
    }

    if obj_type == 'str':
        info['length'] = len(obj)
    elif obj_type == 'list':
        info['length'] = len(obj)

    return info

number_info = introspection_info(55)
print(number_info)