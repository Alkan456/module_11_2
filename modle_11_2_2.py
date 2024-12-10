def introspection_info(name):
    name_type = type(name).__name__

    attributes = dir(name)

    methods = [method for method in attributes if callable(getattr(name,method))]

    module = name.__class__.__module__

    info =  {'type': name_type, 'attributes': attributes, 'methods': methods, 'module': module}

    return info

number_info = introspection_info(42)
print(number_info)


