from di import singleton
from .api import Service, ServiceContainer

class DecoratedServiceContainer(ServiceContainer):
    @property
    @singleton
    def service(self):
        return DecoratedService()


class DecoratedService(Service):
    def print(self):
        return "Decorated singleton service [id=" + str(id(self)) + "]"