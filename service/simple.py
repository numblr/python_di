from .api import Service, ServiceContainer


class SimpleServiceContainer(ServiceContainer):
    def service(self):
        return SimpleService()


class SimpleService(Service):
    def print(self):
        return "Simple service"