import config
import constants

from units.SI import radians
from toolkit.motors.ctre_motors import TalonFX
from toolkit.subsystem import Subsystem
import math


class Arm(Subsystem):

    # Initialize class
    def __init__(self):
        super().__init__()
        self.arm_motor = TalonFX(can_id=config.arm_motor_id, config=config.arm_config)
        self.arm_motor_follower = TalonFX(can_id=config.arm_follower_id, config=config.arm_config)

        self.zeroed = False
        self.arm_moving = False

    # Start motors
    def init(self) -> None:
        self.arm_motor.init()
        self.arm_motor_follower.init()
        self.arm_motor_follower.follow(self.arm_motor, inverted=True)

    # Zero the arm
    def zero(self) -> None:
        self.arm_motor.set_target_position(self.arm_motor.get_sensor_position() * constants.arm_gear_ratio)
        self.arm_motor.set_sensor_position(constants.lower_arm_bound / constants.arm_gear_ratio)
        self.zeroed = True

    # Extends arm to an radians
    # bounding angles (10 - 180 degrees, LB & UB in constants file)
    def extend(self, angle: radians) -> None:
        # added bounding angles to prevent arm from going too far, change in constants file
        self.arm_motor.set_target_position(max(min(angle, math.radians(constants.upper_arm_bound)), math.radians(constants.lower_arm_bound)) * constants.arm_gear_ratio)
        self.arm_moving = True

    def get_radians(self) -> radians:
        return radians(self.arm_motor.get_sensor_position() / constants.arm_gear_ratio)

    # Checks if extended
    def is_extended(self, angle: radians) -> bool:

        # Compare current sensor position with target position
        if self.arm_moving and round((self.arm_motor.get_sensor_position() / constants.arm_gear_ratio), 2) == round(
                angle, 2):
            self.arm_moving = False
            return True
        else:
            return False

    def get_motor_current(self):
        return (self.arm_motor.get_motor_current() + self.arm_motor_follower.get_motor_current()) / 2

    def set_raw_output(self, raw_value: float):
        """
        Set the raw output of the arm motor
        """
        self.arm_motor.set_raw_output(raw_value)
        self.arm_motor_follower.set_raw_output(raw_value)

