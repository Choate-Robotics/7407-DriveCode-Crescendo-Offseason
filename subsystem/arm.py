import config
import constants

from units.SI import radians
from toolkit.motors.ctre_motors import TalonFX
from toolkit.subsystem import Subsystem

class Arm(Subsystem):

    # Initialize class
    def __init__(self):
        super().__init__()
        self.arm_motor = TalonFX(can_id=constants.ARM_MOTOR_ID, config=config.arm_config)
        self.arm_motor_follower = TalonFX(can_id=constants.ARM_MOTOR_ID, inverted=True, config=config.arm_config)

        self.zeroed = False
        self.arm_moving = False

    # Start motors
    def init(self) -> None:
        self.arm_motor.init()
        self.arm_motor_follower.init()
        self.arm_motor_follower.follow(self.arm_motor)

    # Zero the arm
    def zero(self) -> None:
        self.arm_motor.set_target_position(self.arm_motor.get_sensor_position() * constants.arm_gear_ratio)
        self.zeroed = True

    # Extends arm to an radians
    def extend(self, radians: radians) -> None:
        self.arm_motor.set_target_position(radians * constants.arm_gear_ratio)
        self.arm_moving = True

    def getRadians(self) -> radians:
        return radians(self.arm_motor.get_sensor_position() / constants.arm_gear_ratio)

    # Checks if extended
    def isExtended(self, radians: radians) -> bool:
        
        # Compare current sensor position with target position
        if self.arm_moving and round((self.arm_motor.get_sensor_position() / constants.arm_gear_ratio), 2) == round(radians, 2):
            self.arm_moving = False
            return True
        else:
            return False