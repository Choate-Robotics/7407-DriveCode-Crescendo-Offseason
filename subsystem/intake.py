import config
import constants
from toolkit.subsystem import Subsystem
from toolkit.motors.ctre_motors import TalonFX

class Intake(Subsystem):

    def __init__(self):
        super().__init(self)

        self.motor: TalonFX = TalonFX(
            can_id=config.intake_id,
            config=config.INTAKE_CONFIG,
            inverted=False
        )

        self.note_exists_within: bool = False

    def start_motor(self):
        self.motor.set_raw_output(1) #placeholder
    
    def stop_motor(self):
        self.motor.set_raw_output(0)
        