from __future__ import annotations

class EuropeanWallSocket:
    """
    The Target defines the domain-specific interface used by the client code, this case its a European two pin socket.
    """

    def plugin(self, european_plug) -> str:
        return f"{european_plug.two_pin_plug()}"

class UKPlug:
    """
    The Adaptee contains some useful behavior, but its interface is incompatible
    with the existing client code. In this case its a UK plug adapter
    
    The Adaptee needs some adaptation before the client code can use it.
    """

    def three_pin_plug(self) -> str:
        return "Three Pin Plug"

class EuropeanPlug:
    """
    Standard plug, works out of the box with the socket in question and requires no adaption.
    """

    def two_pin_plug(self) -> str:
        return "Two Pin Plug"


class UkToEuroPlugAdapter(EuropeanPlug):
    """
    The Adapter makes the Adaptee's interface compatible with the Target's
    interface.
    """
    def __init__(self, adaptee: UKPlug) -> None:
        self.adaptee = adaptee

    def two_pin_plug(self) -> str:
        return f"(ADAPTED) {self.adaptee.three_pin_plug()}"


def charge_phone(socket: EuropeanWallSocket, plug: EuropeanPlug) -> None:
    """
    The client code supports all classes that follow the Target interface. 
    
    We want to charge our phone but the charger's plug is incompatible with a European plug socket.
    """
    print("[INFO] Charging Phone....", end="\n")
    print(socket.plugin(plug), end="")


if __name__ == "__main__":
    print("[INFO] I need to charge my phone using a charger which has a European style plug")

    # Define a target interface, in this case its a plug socket of the European style
    socket = EuropeanWallSocket()
    european_plug = EuropeanPlug()
    charge_phone(socket, european_plug)
    print("\n")

    print("[INFO] The Adaptee class doesnt present a compatible interface")
    uk_plug = UKPlug()
    print(f"{uk_plug.three_pin_plug()}", end="\n\n")

    # Clearly this is never going to work, we need to charge our phone, we have a perfectly good method of doing so that works and it might be the only way we are ever
    # going to be able to charge it but we are not compatible with the interface that is exposed. 
    #
    # In this instance we are in Europe so we are not going to change the way the Europeans deal with electricity and plugs just to suit our specific use-case
    # (ie we are not going to be able to rewrite some legacy code we want to call if we don't own the API) and we have a perfectly good object already that 
    # is going to encapsulate all of the data and functionality we need (Our chargers UK Plug), we are also not going to rewrite\change this and duplicate our code base for
    # specific use cases, so instead we will ensure we can be compatible with interface by using an adapter.
    try:
        charge_phone(socket, uk_plug)
    except Exception as e:
        print(e, end="\n\n")

    print("[INFO] Client: A plugin adapter can enable compatibility")
    adapter = UkToEuroPlugAdapter(uk_plug)
    charge_phone(socket, adapter)

    print("\n\n")