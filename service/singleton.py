from .api import Service, ServiceContainer


class SingletonServiceContainer(ServiceContainer):
    __singleton = None

    def service(self):
        if SingletonServiceContainer.__singleton is None:
            SingletonServiceContainer.__singleton = SingletonService()

        return SingletonServiceContainer.__singleton


class SingletonService(Service):
    def print(self):
        return "Singleton service [id=" + str(id(self)) + "]"