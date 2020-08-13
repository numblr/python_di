from service.api import ServiceContainer
from .api import Component, ComponentContainer


class DecoratedComponentContainer(ComponentContainer, ServiceContainer):
    @property
    def component(self):
        return DecoratedComponent(self.service)


class DecoratedComponent(Component):
    def __init__(self, service):
        self._service = service

    def print(self):
        return "Decorated Component [id=" + str(id(self)) + "] with " + self._service.print()