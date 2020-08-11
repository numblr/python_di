class ComponentContainer:
    def component(self):
        raise ValueError()


class Component:
    def print(self):
        raise NotImplementedError()