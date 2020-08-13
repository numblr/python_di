def singleton(method):
    def decorated(self, *args, **kwargs):
        static_type = type(self)
        singleton_attr = "_" + method.__name__
        if not hasattr(static_type, singleton_attr):
            setattr(static_type, singleton_attr, method(self, *args, **kwargs))

        return getattr(static_type, singleton_attr)

    return decorated
