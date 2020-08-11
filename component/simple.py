from .api import Component, ComponentContainer
from service.api import ServiceContainer


class SimpleComponentContainer(ComponentContainer, ServiceContainer):
    def component(self):
        return SimpleComponent(self.service())


class SimpleComponent(Component):
    def __init__(self, service):
        self._service = service

    def print(self):
        return "Simple Component with " + self._service.print()