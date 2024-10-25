class Enginee:
    def __init__(self) -> None:
        pass
    def start(self):
        return 'Engine Started'

class Driver:
    def __init__(self) -> None:
        pass

# car has a enginee
class Cars:
    def __init__(self) -> None:
        self.enginee = Enginee()
        self.driver = Driver()

    def start(self):
        self.enginee.start()