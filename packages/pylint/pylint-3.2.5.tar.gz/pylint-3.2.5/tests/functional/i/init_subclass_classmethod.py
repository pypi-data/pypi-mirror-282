# pylint: disable=too-few-public-methods, missing-docstring

class PluginBase:
    subclasses = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)


class Plugin1(PluginBase):
    pass


class Plugin2(PluginBase):
    pass
