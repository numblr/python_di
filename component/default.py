from .api import Component, ComponentContainer
from service.api import ServiceContainer


class DefaultComponentContainer(ComponentContainer, ServiceContainer):
    def component(self):
        return DefaultComponent(self.service())


class DefaultComponent(Component):
    def __init__(self, service):
        self._service = service

    def print(self):
        return "Default Component [id=" + str(id(self)) + "] with " + self._service.print()