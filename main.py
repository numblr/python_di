from component.default import DefaultComponentContainer
from service.simple import SimpleServiceContainer
from service.elaborate import ElaborateServiceContainer
from service.singleton import SingletonServiceContainer

class SimpleApplicationContainer(DefaultComponentContainer, SimpleServiceContainer):
    pass

class ElaborateApplicationContainer(ElaborateServiceContainer, DefaultComponentContainer):
    pass

class SingletonApplicationContainer(SingletonServiceContainer, DefaultComponentContainer):
    pass


def main():
    print("")
    print("Simple Application:")
    component_1 = SimpleApplicationContainer().component()
    component_2 = SimpleApplicationContainer().component()
    print("Component 1: ", component_1.print())
    print("Component 2: ", component_2.print())
    print("")
    print("Elaborate Application:")
    component_1 = ElaborateApplicationContainer().component()
    component_2 = ElaborateApplicationContainer().component()
    print("Component 1: ", component_1.print())
    print("Component 2: ", component_2.print())
    print("")
    print("Singleton Application:")
    component_1 = SingletonApplicationContainer().component()
    component_2 = SingletonApplicationContainer().component()
    print("Component 1: ", component_1.print())
    print("Component 2: ", component_2.print())


if __name__ == '__main__':
    main()
