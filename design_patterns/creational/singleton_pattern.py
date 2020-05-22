class Singleton:
    class __Singleton:
        def __init__(self, arg):
            self.val = arg

    instance = None

    def __init__(self, arg):
        if not Singleton.instance:
            print("[INFO] Constructing new instance", "\n")
            Singleton.instance = Singleton.__Singleton(arg)
        else:
            Singleton.instance.val = arg

    def __repr__(self):
        return f"{Singleton.instance.__repr__()} : {Singleton.instance.val}"

if __name__ == "__main__":
    singleton = Singleton("Red")
    print(singleton, "\n\n")

    singleton = Singleton("Green")
    print(singleton, "\n\n")

    singleton = Singleton("Blue")
    print(singleton, "\n\n")

    singleton = Singleton("Purple")
    print(singleton, "\n\n")

    singleton = Singleton("Orange")
    print(singleton, "\n\n")