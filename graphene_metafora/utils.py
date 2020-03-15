from graphene import Argument, Field, InputField, List, Scalar


def get_metafora_cls(cls):
    return getattr(cls, 'Metafora', None)

def get_metafora_obj(cls):
    return getattr(cls, '_metafora', None)

def metafora_cls_to_obj(cls, opts):
    if hasattr(cls, 'Metafora'):
        delattr(cls, 'Metafora')
    setattr(cls, '_metafora', opts)


def get_resolver(cls, field_name):
    return getattr(cls, f'resolve_{field_name}', None)


def get_fields(cls):
    fields = {}
    for name in dir(cls):
        if name.startswith('_'):
            continue
        attr = getattr(cls, name)
        if isinstance(attr, (Argument, Field, InputField, List, Scalar)):
            fields[name] = attr
    return fields
