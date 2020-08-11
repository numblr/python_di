from component.simple import SimpleComponentContainer
from service.simple import SimpleServiceContainer
from service.elaborate import ElaborateServiceContainer

class SimpleApplicationContainer(SimpleServiceContainer, SimpleComponentContainer):
    pass

class ElaborateApplicationContainer(ElaborateServiceContainer, SimpleComponentContainer):
    pass


def main():
    print("")
    print("Simple Application:")
    print(SimpleApplicationContainer().component().print())
    print("")
    print("Elaborate Application:")
    print(ElaborateApplicationContainer().component().print())


if __name__ == '__main__':
    main()
