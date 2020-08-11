class ServiceContainer:
    def service(self):
        raise ValueError()

class Service:
    def print(self):
        raise NotImplementedError()