import subsystem
import sensors
import wpilib
import config
import constants


class Robot:
    drivetrain = subsystem.Drivetrain()


class Pneumatics:
    pass


class Sensors:
    left_cam = sensors.PhotonCamCustom(config.left_cam_name, constants.robotToLeftCam)
    right_cam = sensors.PhotonCamCustom(config.right_cam_name, constants.robotToRightCam)
    zoom_cam = sensors.PhotonCamCustom(config.zoom_cam_name, constants.robotToZoomCam)


class LEDs:
    pass


class PowerDistribution:
    pass


class Field:
    pass
