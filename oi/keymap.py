import wpilib
import commands2.button

from toolkit.oi import (
    XBoxController,
    LogitechController,
    JoystickAxis,
    Joysticks,
    DefaultButton,
)

controllerDRIVER = XBoxController

class Controllers:
    DRIVER: int = 0
    OPERATOR: int

    DRIVER_CONTROLLER = wpilib.Joystick(0)


class Keymap:
    class Arm:
        SET_ARM_SPEAKER = commands2.button.JoystickButton(
            Joysticks.joysticks[Controllers.DRIVER], controllerDRIVER.Y
        )

        SET_ARM_AMP = commands2.button.JoystickButton(
            Joysticks.joysticks[Controllers.DRIVER], controllerDRIVER.B
        )

        SET_ARM_INTAKE = commands2.button.JoystickButton(
            Joysticks.joysticks[Controllers.DRIVER], controllerDRIVER.A
        )
