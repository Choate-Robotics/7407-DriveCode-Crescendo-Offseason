from toolkit.oi import (
    XBoxController,
    LogitechController,
    JoystickAxis,
    DefaultButton,
    Joysticks
)

import wpilib
import commands2.button

controllerOPERATOR = XBoxController

class Controllers:
#    DRIVER: int
    OPERATOR: int = 1


class Keymap:
    class Intake:
        INTAKE_TOGGLE = commands2.button.JoystickButton(Joysticks.joysticks[Controllers.OPERATOR], controllerOPERATOR.A)