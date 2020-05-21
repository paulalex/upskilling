from abc import ABC, abstractmethod

class Light:
    is_on = False

    def switch_on(self):
        self.is_on = True
        print("On")

    def switch_off(self):
        self.is_on = False
        print("Off")

class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

class LightOnCommand(Command):
    _light = None

    def __init__(self, light):
        super().__init__()
        self._light = light
        
    def execute(self) -> None:
        self._light.switch_on()


class LightOffCommand(Command):
    _light = None
    
    def __init__(self, light):
        super().__init__()
        self._light = light

    def execute(self) -> None:
        self._light.switch_off()
        

class LightSwitch:
    _command = None

    def set_command(self, command):
        self._command = command

    def press_switch(self):
        self._command.execute()

if __name__ == "__main__":
    light = Light()
    light_off_command = LightOffCommand(light)
    light_on_command = LightOnCommand(light)
    light_controller = LightSwitch()

    # Turn the light on
    light_controller.set_command(light_on_command)
    light_controller.press_switch()

    # Turn the light off
    light_controller.set_command(light_off_command)
    light_controller.press_switch()