from .utils import get_metafora_cls


class InputObjectOptions:
    def __init__(self, abstract=False, changes=None, required=None):
        self.abstract = abstract
        self.changes = changes or []
        self.required = required or {}

    def merge(self, super_opts):
        if super_opts:
            self.changes += super_opts.changes
        return self

    @classmethod
    def from_meta(cls, meta):
        if meta:
            kwargs = {k: v for k, v in meta.__dict__.items() if not k.startswith('_')}
        else:
            kwargs = {}
        return cls(**kwargs)


class OrderingOptions:
    def __init__(self, parent_cls):
        meta = get_metafora_cls(parent_cls)
        self.can_order_by = meta.__dict__['can_order_by']
        self.default_ordering = meta.__dict__.get('default_ordering', None)
        if isinstance(self.default_ordering, str):
            self.default_ordering = [self.default_ordering]

        assert isinstance(self.can_order_by, (list, tuple))
        assert isinstance(self.default_ordering, (list, tuple, type(None)))
        assert all([name in parent_cls._meta.fields for name in self.can_order_by])
        if self.default_ordering:
            assert all([
                name in self.can_order_by
                for name in self._cleaned_names(self.default_ordering)
            ])


    @classmethod
    def _cleaned_names(cls, ordering):
        return [name.replace('-', '') for name in ordering]

    def validate_ordering(self, ordering):
        return all([item in self.can_order_by for item in self._cleaned_names(ordering)])
