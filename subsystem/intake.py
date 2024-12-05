import config
import constants
from toolkit.subsystem import Subsystem
from toolkit.motors.rev_motors import TalonFX

class Intake(Subsystem):

    def __init__(self):
        super().__init(self)

        self.motor: TalonFX = TalonFX(
            can_id=config.intake_id,
            config=config.INTAKE_CONFIG,
            inverted=False
        )

    def start_intake(self):
        self.motor.set_raw_output(10) #placeholder
    
    def stop_intake(self):
        self.motor.set_raw_output(0)
        