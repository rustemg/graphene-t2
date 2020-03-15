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
