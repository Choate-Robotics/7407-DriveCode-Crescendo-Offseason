from wpimath.geometry import Transform3d, Translation3d, Rotation3d 


#cameraas
robotToLeftCam = Transform3d(
    Translation3d(0.25, -0.25, 0.25),
    Rotation3d(0, 0, 0)
)
robotToRightCam = Transform3d(
    Translation3d(0.25, 0.25, 0.25),
    Rotation3d(0, 0, 0)
)
robotToZoomCam = Transform3d(
    Translation3d(0, 0, 0.5),
    Rotation3d(0, 0, 0)
)