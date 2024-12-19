from wpimath.geometry import Transform3d, Translation3d, Rotation3d
from units.SI import inches_to_meters
import math
import math
from units.SI import (
    degrees_per_second__to__radians_per_second,
    feet_to_meters,
    inches_to_meters,
    meters,
    rotations_per_minute,
    degrees_to_radians,
    meters_per_second_squared,
)

#cameraas
robotToLeftCam = Transform3d(
    Translation3d(8.052*inches_to_meters, 10.247*inches_to_meters, 8.514*inches_to_meters),
    Rotation3d(0, math.radians(-61.875), math.radians(30))
)
robotToRightCam = Transform3d(
    Translation3d(8.052*inches_to_meters, -10.247*inches_to_meters, 8.514*inches_to_meters),
    Rotation3d(0, math.radians(-61.875), math.radians(-30))
)
robotToZoomCam = Transform3d(
    Translation3d(0, 0, 0.5),
    Rotation3d(0, 0, 0)
)

#drivetrain
drivetrain_turn_gear_ratio: float = 150 / 7
drivetrain_wheel_gear_ratio: float = 5.9
track_width: meters = 19.75 * inches_to_meters # distance between the center of the wheels on the front
wheel_base: meters = 18.25 * inches_to_meters # distance between center of wheels from the side
drivetrain_length: meters = 20 #length of one side of the robot, placeholder
bumper_thickness: float = 3.5
drivetrain_length_with_bumpers = drivetrain_length + (2 * bumper_thickness)

drivetrain_move_motor_free_speed: rotations_per_minute = (
    6000 #6000 is the free speed RPM of the Kraken without FOC
)

drivetrain_wheel_diameter: meters = (
        4 * inches_to_meters
)  
 

drivetrain_max_vel: meters = (
    ((drivetrain_move_motor_free_speed / 60) / drivetrain_wheel_gear_ratio) * (drivetrain_wheel_diameter * math.pi)
    )
# drivetrain_max_vel = 5.4 m/s, 17.7 ft/s, 12.1 mph
drivetrain_max_accel: meters_per_second_squared = 0 # setting to 0 will set to default motor accel
drivetrain_max_angular_vel = 720 * degrees_per_second__to__radians_per_second
drivetrain_max_angular_accel = 720 * degrees_per_second__to__radians_per_second


# the below variable is the rotation the motor rotates per meter of wheel movement
drivetrain_move_gear_ratio_as_rotations_per_meter: float = (
    1 / (drivetrain_wheel_diameter * math.pi)
) * drivetrain_wheel_gear_ratio
