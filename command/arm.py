import math
import wpilib
from commands2 import SequentialCommandGroup
import config
import constants
import utils
from oi.keymap import Controllers
from subsystem import Arm
from toolkit.command import SubsystemCommand
from units.SI import radians
from enum import Enum


# cmds: set arm (angle), zero arm, specific positions that inherit from set arm

class SetArm(SubsystemCommand[Arm]):
    """
    Sets the wrist to a given angle (radians).
    param: radians in radians
    """

    def __init__(self, subsystem: Arm, radians: float):
        super().__init__(subsystem)
        self.subsystem = subsystem
        self.radians = radians

    def initialize(self):
        # change to actual name
        self.subsystem.extend(self.radians)
        self.subsystem.arm_moving = True

    def execute(self):
        pass

    def isFinished(self):
        return self.subsystem.is_extended(self.radians)

    def end(self, interrupted: bool):
        if interrupted:
            arm_radians = self.subsystem.get_radians()
            print(f"Stuck at {arm_radians} radians")

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
        if interrupted:
            self.subsystem.zeroed = False


class SetSpeakerPosition(SetArm):
    def __init__(self, subsystem: Arm):
        super().__init__(subsystem, math.radians(config.speaker_angle))


class SetAmpPosition(SetArm):
    def __init__(self, subsystem: Arm):
        super().__init__(subsystem, math.radians(config.amp_angle))


class SetIntakePosition(SetArm):
    def __init__(self, subsystem: Arm):
        super().__init__(subsystem, math.radians(config.intake_angle))
