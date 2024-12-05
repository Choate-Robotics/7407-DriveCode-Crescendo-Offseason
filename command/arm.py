import math

import wpilib  # noqa
from commands2 import SequentialCommandGroup  # noqa

import config
import constants  # noqa
import utils  # noqa
from oi.keymap import Controllers  # noqa
from subsystem import Arm
from toolkit.command import SubsystemCommand
from units.SI import radians
from enum import Enum


# cmds: set arm (angle), zero arm, specific positions that inherit from set arm

class SetArm(SubsystemCommand[Arm]):
    """
    Sets the wrist to a given angle (radians).
    param: angle in radians
    """

    def __init__(self, subsystem: Arm, angle: float):
        super().__init__(subsystem)
        self.subsystem = subsystem
        self.angle = angle

    def initialize(self):
        # change to actual name
        self.subsystem.extend(self.angle)
        self.subsystem.arm_moving = True

    def execute(self):
        pass

    def isFinished(self):
        return self.subsystem.isExtended(self.angle)

    def end(self, interrupted: bool):
        if interrupted:
            arm_angle = self.subsystem.get_angle()

        self.subsystem.arm_moving = False


class ZeroArm(SubsystemCommand[Arm]):
    """
    Zeros the arm.
    """

    def __init__(self, subsystem: Arm):
        super().__init__(subsystem)
        self.subsystem = subsystem

    def initialize(self):
        # change to actual name
        self.subsystem.zero()

    def execute(self):
        pass

    def isFinished(self):
        return self.subsystem.zeroed

    def end(self, interrupted: bool):
        if not interrupted:
            self.subsystem.zeroed = True
        else:
            ...


class SetSpeakerPosition(SetArm):
    def __init__(self, subsystem: Arm):
        super().__init__(subsystem, radians(config.speaker_angle))


class SetAmpPosition(SetArm):
    def __init__(self, subsystem: Arm):
        super().__init__(subsystem, radians(config.amp_angle))


class SetIntakePosition(SetArm):
    def __init__(self, subsystem: Arm):
        super().__init__(subsystem, radians(config.intake_angle))
