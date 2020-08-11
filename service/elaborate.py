from .api import Service, ServiceContainer


class ElaborateServiceContainer(ServiceContainer):
    def service(self):
        return ElaborateService()


class ElaborateService(Service):
    def print(self):
        return "Elaborate service"