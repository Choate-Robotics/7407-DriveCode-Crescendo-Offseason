from utils import LocalLogger

import commands2
import command, config, constants
from robot_systems import Robot, Sensors, Field
from oi.keymap import Keymap
import wpilib
from math import radians

log = LocalLogger("OI")

class OI:

    @staticmethod
    def init() -> None:
        log.info("Initializing OI...")

    @staticmethod
    def map_controls():
        log.info("Mapping controls...")
        # Arm keymapping
        Keymap.Arm.SET_ARM_SPEAKER.onTrue(
            command.arm.SetSpeakerPosition(Robot.arm)
        ).onFalse(
            command.arm.SetIntakePosition(Robot.arm)
        )
        Keymap.Arm.SET_ARM_AMP.onTrue(
            command.arm.SetAmpPosition(Robot.arm)
        ).onFalse(
            command.arm.SetIntakePosition(Robot.arm)
        )
        # No one is actually going to use this button XD
        Keymap.Arm.SET_ARM_INTAKE.onTrue(
            command.arm.SetIntakePosition(Robot.arm)
        )
