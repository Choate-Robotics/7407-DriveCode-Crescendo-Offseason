import ntcore

from photonlibpy.photonCamera import PhotonCamera
from photonlibpy.photonPoseEstimator import PhotonPoseEstimator, PoseStrategy
from robotpy_apriltag import AprilTagField, loadAprilTagLayoutField
from wpimath.geometry import Transform3d
from wpilib import TimedRobot


class PhotonCamCustom:
    def __init__(self, name: str, robot_to_camera: Transform3d):
        self.cam = PhotonCamera(name)
        self.name = name
        self.robot_to_camera = robot_to_camera
        self.estimator = PhotonPoseEstimator(
            loadAprilTagLayoutField(AprilTagField.k2024Crescendo),
            PoseStrategy.MULTI_TAG_PNP_ON_COPROCESSOR,
            self.cam,
            self.robot_to_camera
        )
        self.table = ntcore.NetworkTableInstance.getDefault().getTable("Cameras")

    def init(self):
        pass

    def update_tables(self):
        if not TimedRobot.isSimulation():
            result = self.cam.getLatestResult()
            self.estimator.update(result)
            pose = self.estimator.lastPose
            if pose:
                self.table.putNumberArray(
                    f"{self.name} estimated pose",
                    [
                        pose.X(),
                        pose.Y(),
                        pose.rotation()
                    ]
                )

    def get_estimated_robot_pose(self):
        self.estimator.update(self.cam.getLatestResult())
        return self.estimator.lastPose


class CamerasController:
    def __init__(self):
        self.cam_r = PhotonCamCustom("cam_r", Transform3d())
        self.cam_l = PhotonCamCustom("cam_l", Transform3d())
        self.cam_back = PhotonCamCustom("cam_back", Transform3d())

    def init(self):
        pass

    def update_tables(self):
        self.cam_r.update_tables()
        self.cam_l.update_tables()
        self.cam_back.update_tables()

    def get_robot_poses(self):
        return [
            self.cam_r.get_estimated_robot_pose(),
            self.cam_l.get_estimated_robot_pose(),
            self.cam_back.get_estimated_robot_pose()
        ]

