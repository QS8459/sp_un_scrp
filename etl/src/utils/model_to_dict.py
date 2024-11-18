from sqlalchemy.orm import class_mapper
from sqlalchemy.orm.properties import ColumnProperty


def model_to_dict(obj, max_depth=1, current_depth=0):
    if current_depth > max_depth:
        return str(obj)

    if isinstance(obj, list):
        return [model_to_dict(item, max_depth, current_depth + 1) for item in obj]

    if not hasattr(obj, '__table__'):
        return str(obj)

    result = {}
    for prop in class_mapper(obj.__class__).iterate_properties:
        if isinstance(prop, ColumnProperty):
            result[prop.key] = getattr(obj, prop.key)
        else:
            # Handle relationships
            value = getattr(obj, prop.key)
            if value is not None:
                result[prop.key] = model_to_dict(value, max_depth, current_depth + 1)
    return result