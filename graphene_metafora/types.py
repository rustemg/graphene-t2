import graphene
from graphene.pyutils.init_subclass import InitSubclassMeta

from .features import changes, ordering, required
from .options import InputObjectOptions
from .utils import (
    get_fields,
    get_metafora_cls,
    get_metafora_obj,
    metafora_cls_to_obj,
)


class InputObjectType(graphene.InputObjectType):
    @classmethod
    def __init_subclass_with_meta__(cls, container=None, _meta=None, **options):
        cls._handle_metafora()
        super().__init_subclass_with_meta__(container, _meta, **options)

    @classmethod
    def _handle_metafora(cls):
        own_fields = {}
        fields = get_fields(cls)

        super_opts = get_metafora_obj(cls)
        metafora_cls = get_metafora_cls(cls)
        opts = InputObjectOptions.from_meta(metafora_cls).merge(super_opts)
        metafora_cls_to_obj(cls, opts)
        if opts.abstract:
            return
        changes.update_description(opts, fields, own_fields)
        required.apply_required(opts, fields, own_fields)
        for field_name, field in own_fields.items():
            setattr(cls, field_name, field)


class Queries(metaclass=InitSubclassMeta):
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        meta = get_metafora_cls(cls)
        if meta:
            fields = get_fields(cls)
            ordering.enable_ordering(cls, meta, fields)
