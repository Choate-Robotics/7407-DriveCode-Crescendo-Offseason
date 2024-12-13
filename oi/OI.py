from oi.keymap import Keymap
from utils import LocalLogger
import commands2
from robot_systems import Robot

log = LocalLogger("OI")

class OI:
    
    
    
    @staticmethod
    def init() -> None:
        log.info("Initializing OI...")

    @staticmethod
    def map_controls():
        log.info("Mapping controls...")
        Keymap.Intake.INTAKE_TOGGLE.onTrue(
            commands2.InstantCommand(lambda: Robot.intake.start_motor())
        ).onFalse(
            commands2.InstantCommand(lambda: Robot.intake.stop_motor())
        )
        
