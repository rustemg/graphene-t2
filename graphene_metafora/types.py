import graphene
import graphene_django
from graphene.pyutils.init_subclass import InitSubclassMeta

from .features import changes, ordering, required
from .options import (
    DjangoObjectTypeOptions,
    InputObjectOptions,
    QueriesOptions,
)
from .utils import (
    get_fields,
    get_metafora_cls,
    get_metafora_obj,
    metafora_cls_to_obj,
)


def _init_options(cls, options_cls):
    super_opts = get_metafora_obj(cls)
    metafora_cls = get_metafora_cls(cls)
    opts = options_cls.from_meta(metafora_cls).merge(super_opts)
    metafora_cls_to_obj(cls, opts)
    return opts


class InputObjectType(graphene.InputObjectType):
    @classmethod
    def __init_subclass_with_meta__(cls, container=None, _meta=None, **options):
        cls._handle_metafora(InputObjectOptions)
        super().__init_subclass_with_meta__(container, _meta, **options)

    @classmethod
    def _handle_metafora(cls, options_cls):
        opts = _init_options(cls, options_cls)
        if opts.abstract:
            return

        own_fields = {}
        fields = get_fields(cls)
        changes.update_description(opts, fields, own_fields)
        required.apply_required(opts, fields, own_fields)
        for field_name, field in own_fields.items():
            setattr(cls, field_name, field)


class Queries(metaclass=InitSubclassMeta):
    def __init_subclass__(cls):
        opts = _init_options(cls, QueriesOptions)
        fields = get_fields(cls)
        ordering.enable_ordering(cls, opts, fields)


class DjangoObjectType(graphene_django.DjangoObjectType):
    class Meta:
        abstract = True

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        opts = _init_options(cls, DjangoObjectTypeOptions)
