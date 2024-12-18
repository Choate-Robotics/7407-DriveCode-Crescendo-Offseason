from wpimath.geometry import Transform3d, Translation3d, Rotation3d
from units.SI import inches_to_meters
import math


#cameraas
robotToLeftCam = Transform3d(
    Translation3d(8.052*inches_to_meters, 10.247*inches_to_meters, 8.514*inches_to_meters),
    Rotation3d(0, -math.radians(61.875), math.radians(30))
)
robotToRightCam = Transform3d(
    Translation3d(8.052*inches_to_meters, -10.247*inches_to_meters, 8.514*inches_to_meters),
    Rotation3d(0, -math.radians(61.875), -math.radians(30))
)
robotToZoomCam = Transform3d(
    Translation3d(0, 0, 0.5),
    Rotation3d(0, 0, 0)
)